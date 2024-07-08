from flask import Blueprint, render_template

from .crud import Clicker

clicker_app = Blueprint(
    "clicker_app",
    __name__,
)

app = clicker_app

clicker = Clicker()


@app.get("/", endpoint="index")
def show_clicker_page():
    """
    Keep all the state on backend, and show new info to client
    """
    # This shows the number of clicks
    return render_template(
        "clicker/index.html",
        count=clicker.count,
    )


@app.post("/", endpoint="inc-click")
def handle_each_click():
    clicker.inc_count()
    # Here we increase the number of clicks +1
    return render_template(
        "clicker/index.html",
        count=clicker.count,
    )
