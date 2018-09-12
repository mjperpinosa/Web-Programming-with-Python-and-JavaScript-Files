from flask import Flask, request, render_template
import os, SocketIO


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
	return render_template("index.html")


@socketio.on("submit vote")
def vote(data):
	selection = data["selection"]
	emit("announce vote", {"selection": selection}, broadcast=True)
