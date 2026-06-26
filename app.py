import os
from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/websocket')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        if message:
            # Ici, le script traite le tunnel
            ws.send(b"Connexion SSH-WebSocket etablie avec succes")

@app.route('/')
def hello():
    return "Serveur en ligne (WORLD/SOLUTION)"

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    port = int(os.environ.get("PORT", 8080))
    server = pywsgi.WSGIServer(('', port), app, handler_class=WebSocketHandler)
    print(f"Serveur lance sur le port {port}")
    server.serve_forever()
