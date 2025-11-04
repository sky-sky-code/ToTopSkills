from authlib.integrations.flask_client import OAuth
from flask import Flask, url_for

app = Flask(__name__)
app.secret_key = 'awdawdawdvfvdfv'

oauth = OAuth(app)

# Правильная конфигурация клиента
oauth.register(
    name='provider',
    client_id='test',
    client_secret='test',
    authorize_url='http://127.0.0.1:8000/authorize',
    access_token_url='http://127.0.0.1:8000/token/',
    userinfo_endpoint='http://127.0.0.1:8000/userinfo/',
    client_kwargs={'scope': 'openid profile'}
)


# Правильный вызов авторизации
@app.route('/login')
def login():
    redirect_uri = url_for('auth_callback', _external=True).replace('https://', 'http://')
    return oauth.provider.authorize_redirect(redirect_uri)


@app.route('/authorize')
def auth_callback():
    token = oauth.provider.authorize_access_token()
    userinfo = oauth.provider.userinfo(token=token)
    return userinfo


app.run(host='127.0.0.1', port=8081)
