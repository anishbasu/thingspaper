from flask import Flask, render_template
import things
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def get_todos():
    return render_template('today.html', todos=things.today(), now=datetime.now())
