from flask import Flask, render_template
from duku import Duku

app = Flask(__name__)

@app.route("/")
def hello_world():
    thegame = Duku()
    return render_template("index.html", title="Hello", board=thegame.board)
