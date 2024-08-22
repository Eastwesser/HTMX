from http import HTTPStatus

from flask import (
    Blueprint,
    render_template,
    Response,
)
from werkzeug.exceptions import HTTPException

from .crud import products_storage
from .forms import ProductForm

products_app = Blueprint(
    "products_app",
    __name__,
)

app = products_app


@app.get("/", endpoint="list")
def get_products_list():
    form = ProductForm()
    products = products_storage.get_list()
    return render_template(
        "products/list.html",
        products=products,
        form=form,
    )


@app.post("/", endpoint="create")
def create_product():
    # For Flask wtf we use this method:
    form = ProductForm()
    if not form.validate_on_submit():
        # """product_name = request.form.get("product-name", "").strip()"""
        # """product_price = request.form.get("product-price", "").strip()"""
        # """if not product_price.isdigit():"""
        # raise BadRequest("Product abc")
        # raise BadRequest("product price should be integer")
        response = Response(
            render_template(
                "products/components/form.html",
                form=form,
                # """ product_name=product_name, """
                # """ error="product price should be integer", """
            ),
            status=HTTPStatus.UNPROCESSABLE_ENTITY,
        )
        raise HTTPException(response=response)

    product = products_storage.add(
        # """ product_name=product_name, """
        product_name=form.name.data,
        # """ product_price=int(product_price), """
        product_price=form.price.data,
    )
    return render_template(
        "products/components/form-and-item-oob.html",
        product=product,
        form=ProductForm(formdata=None),
    )  # When requested, we create a new element and return only the new rendered element

    # products = products_storage.get_list()
    # return render_template(
    #     "products/components/items-list.html",
    #     products=products,
    # )
    # url = url_for("products_app.list")
    # return redirect(url)


@app.delete("/<int:product_id>/", endpoint="delete")  # int is for flask validation
def delete_product(product_id: int):
    products_storage.delete(product_id)
    return Response(status=HTTPStatus.NO_CONTENT)  # NO_CONTENT code 204
