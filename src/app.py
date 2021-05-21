import random
from flask import Flask, request
from .application.routes.routes import REQUEST_API
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/v1/reference'
API_URL = '/static/swagger.yaml'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Crud of users"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(REQUEST_API)

@app.route('/')
def inicio():
    return "<h1>WELCOME THE API</h1>"


