from flask import Blueprint, render_template

from utils.helpers import is_background_request
from .crud import Clicker

clicker_app = Blueprint(
    "clicker_app",
    __name__,
)

app = clicker_app

clicker = Clicker()


# It's better to keep all data on server side (not client's)


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

    # Check if it is background or not
    template_name = "clicker/index.html"
    if is_background_request():
        template_name = ("clicker/clicker-components/click-count.html",)

    # Here we increase the number of clicks +1
    return render_template(
        # We use "clicker/index.html" below working with HTML only, without HTMX
        # "clicker/index.html",
        template_name,
        count=clicker.count,
    )
