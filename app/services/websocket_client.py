import websocket
import json
from app.services.orderbook_processor import process_tick
from app.utils.logger import logger

URL = "wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP"

def on_message(ws, message):
    data = json.loads(message)
    process_tick(data)

def on_error(ws, error):
    logger.error(f"WebSocket error: {error}")

def on_close(ws):
    logger.warning("WebSocket closed")

def on_open(ws):
    logger.info("WebSocket connection opened")

def start_websocket():
    ws = websocket.WebSocketApp(URL,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
