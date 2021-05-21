from src.background import ServiceBackground
from src.app import app
def start_app():
    ServiceBackground()
    app.run(host='0.0.0.0',port=5000)
    
start_app()
