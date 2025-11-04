from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
import secrets

import uvicorn

app = FastAPI()

# Конфигурация
SECRET_KEY = secrets.token_hex(32)  # Для подписи JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Хранилище данных (вместо БД для примера)
fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # "secret"
        "scopes": ["read_profile"],
    }
}
fake_codes = {}  # { "code": { "user": "user1", "redirect_uri": "..." } }
fake_tokens = {}  # { "access_token": { "sub": "user1", "scopes": [...] } }

# Утилиты
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="/authorize",
    tokenUrl="/token",
    scopes={"read_profile": "Read your profile"},
)


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str | None = None


class User(BaseModel):
    username: str
    scopes: list[str] = []


# Вспомогательные функции
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(username: str):
    if username in fake_users_db:
        return User(**fake_users_db[username])


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Эндпоинты
@app.get("/authorize")
async def authorize(
        response_type: str,  # Должен быть "code"
        client_id: str,  # ID клиента (игнорируем для примера)
        redirect_uri: str,  # Куда вернуть код
        scope: str = None,  # Запрашиваемые scope (например, "read_profile")
        state: str = None,  # CSRF-защита (необязательно)
):
    if response_type != "code":
        raise HTTPException(status_code=400, detail="Invalid response_type")

    # В реальном приложении здесь будет форма входа
    # Для примера сразу генерируем код для user1
    auth_code = secrets.token_urlsafe(16)
    fake_codes[auth_code] = {
        "user": "user1",
        "redirect_uri": redirect_uri,
        "scopes": scope.split(" ") if scope else [],
    }
    return RedirectResponse(f"{redirect_uri}?code={auth_code}&state={state}")


from pydantic import BaseModel


class ReqBody(BaseModel):
    grant_type: str  # "authorization_code" или "refresh_token"
    code: str | None = None  # Код из /authorize
    refresh_token: str | None = None
    redirect_uri: str | None = None


@app.post("/token")
async def token(req_body: ReqBody):
    if req_body.grant_type == "authorization_code":
        if req_body.code not in fake_codes:
            raise HTTPException(status_code=400, detail="Invalid code")
        user_data = fake_codes.pop(req_body.code)
        user = get_user(user_data["user"])
        access_token = create_access_token(
            data={"sub": user.username, "scopes": user_data["scopes"]},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        refresh_token = create_access_token(
            data={"sub": user.username},
            expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
        )
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "refresh_token": refresh_token,
        }
    elif req_body.grant_type == "refresh_token":
        # Реализуйте обновление токена (проверка refresh_token)
        raise HTTPException(status_code=501, detail="Not implemented")
    else:
        raise HTTPException(status_code=400, detail="Invalid grant_type")


@app.get("/userinfo")
async def userinfo(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username, "scopes": user.scopes}


uvicorn.run(app, host='127.0.0.1', port=8080)
