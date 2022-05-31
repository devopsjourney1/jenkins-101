from flask import Flask, json
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<h1>My WebApp!</h1> Hello World! Served from <b>{socket.gethostname()}</b>"
    return html