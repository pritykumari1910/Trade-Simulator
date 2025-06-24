from threading import Thread
from app.ui.layout import create_ui
from app.services.websocket_client import start_websocket

def run_app():
    Thread(target=start_websocket, daemon=True).start()
    create_ui()
