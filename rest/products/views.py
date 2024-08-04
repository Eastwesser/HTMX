from flask import Blueprint, request, render_template

products_app = Blueprint(
    "products_app",
    __name__,
)

app = products_app


@app.get("/", endpoint="list")
def get_products_list():
    return render_template("products/list.html")
