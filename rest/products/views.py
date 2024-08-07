from flask import (
    Blueprint,
    request,
    render_template,
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
    # raise BadRequest("Product abc")
    product = products_storage.add(
        product_name=product_name,
        product_price=int(product_price),
    )
    return render_template(
        "products/components/item-oob.html",
        product=product,
    )  # When requested, we create a new element and return only the new rendered element

    # products = products_storage.get_list()
    # return render_template(
    #     "products/components/items-list.html",
    #     products=products,
    # )
    # url = url_for("products_app.list")
    # return redirect(url)
