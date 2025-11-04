from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse, HTMLResponse
from jose import jwt
from datetime import datetime, timedelta
import httpx
import secrets
import uvicorn

app = FastAPI()

# Конфигурация клиента
CLIENT_ID = "test"
CLIENT_SECRET = "test"  # В реальном приложении храните это безопасно!
REDIRECT_URI = "http://127.0.0.1:8081/authorize"
AUTH_SERVER = "http://127.0.0.1:8000"  # URL вашего OAuth-сервера

# Для хранения сессий (вместо БД)
sessions = {}

# OAuth2 схема для защиты эндпоинтов
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{AUTH_SERVER}/authorize",
    tokenUrl=f"{AUTH_SERVER}/token",
    scopes={"read_profile": "Read your profile"},
)


@app.get("/login")
async def login():
    # Генерируем state для защиты от CSRF
    state = secrets.token_urlsafe(16)
    sessions[state] = {"state": state}

    # Перенаправляем пользователя на сервер авторизации
    auth_url = (
        f"{AUTH_SERVER}/authorize?"
        f"response_type=code&"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"scope=openid profile&"
        f"state={state}&"
        # f"nonce={secrets.token_urlsafe(16)}"
    )
    return RedirectResponse(auth_url)


@app.get("/authorize")
async def callback():
    return 'Hello World'
    # if state not in sessions:
    #     raise HTTPException(status_code=400, detail="Invalid state")
    #
    # # Обмениваем код на токен
    # async with httpx.AsyncClient() as client:
    #     response = await client.post(
    #         f"{AUTH_SERVER}/token",
    #         json={
    #             "grant_type": "authorization_code",
    #             "code": code,
    #             "redirect_uri": REDIRECT_URI,
    #             "client_id": CLIENT_ID,
    #             "client_secret": CLIENT_SECRET,
    #         },
    #     )
    #
    # if response.status_code != 200:
    #     raise HTTPException(status_code=400, detail="Failed to get token")
    #
    # token_data = response.json()
    # # sessions[state]["token"] = token_data

    # Получаем данные пользователя
    # userinfo = await get_userinfo(token_data["access_token"])
    # return HTMLResponse(
    #     f"<h1>Welcome, {userinfo['username']}!</h1>"
    #     f"<p>Scopes: {userinfo['scopes']}</p>"
    #     f"<p>Access Token: {token_data['access_token']}</p>"
    # )


async def get_userinfo(access_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{AUTH_SERVER}/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch userinfo")
    return response.json()


@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    userinfo = await get_userinfo(token)
    return {"message": "Access granted", "user": userinfo}


uvicorn.run(app, host='127.0.0.1', port=8081)
