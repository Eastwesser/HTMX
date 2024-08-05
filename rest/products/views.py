from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)

from .crud import products_storage

products_app = Blueprint(
    "products_app",
    __name__,
)

app = products_app


@app.get("/", endpoint="list")
def get_products_list():
    products = products_storage.get_list()
    return render_template(
        "products/list.html",
        products=products,
    )


@app.post("/", endpoint="create")
def create_product():
    product_name = request.form.get("product-name", "").strip()
    product_price = request.form.get("product-price", "").strip()
    # if product_price.isdigit():
    product = products_storage.add(
        product_name=product_name,
        product_price=int(product_price),
    )
    # products = products_storage.get_list()
    # return render_template(
    #     "products/list.html",
    #     products=products,
    # )
    url = url_for("products_app.list")
    return redirect(url)
