from flask import (
    Blueprint,
    render_template,
    request,
)

# The name of this application is set to "examples_app"
examples_app = Blueprint(
    "examples_app",
    __name__,
)

app = examples_app


# For easier page navigation, set endpoint
@app.get("/", endpoint="index")
def examples_list():
    return render_template("examples/index.html")


@app.route(
    "/ping/",
    methods=["GET", "POST"],
    endpoint="ping",
)
def handle_ping():
    if request.method == "POST":
        return "Pong!"
    return render_template("examples/ping/show-ping.html")
