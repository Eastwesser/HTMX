# This file is made for rendering index.html template
from flask import Blueprint, render_template

index_app = Blueprint(
    "index_app",
    __name__,
)

app = index_app


@app.route("/", endpoint="index")
def index_view():
    return render_template("index.html")
