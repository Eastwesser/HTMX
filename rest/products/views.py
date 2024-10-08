from dataclasses import asdict
from http import HTTPStatus

from flask import (
    Blueprint,
    render_template,
    Response,
    redirect,
    url_for,
    request,
)
from werkzeug.exceptions import HTTPException, NotFound

from utils.helpers import is_background_request
from .crud import products_storage
from .forms import ProductForm

products_app = Blueprint(
    "products_app",
    __name__,
)

app = products_app

PAGE_DEFAULT = 1
PER_PAGE_DEFAULT = 10


@app.get("/", endpoint="list")
def get_products_list():
    form = ProductForm()
    all_products = products_storage.get_list()
    page = request.args.get("page", PAGE_DEFAULT, type=int)
    per_page = request.args.get(
        "per_page", PER_PAGE_DEFAULT, type=int
    )  # 10 elements listed on 1 page
    to_idx = page * per_page
    from_idx = to_idx - per_page
    products = all_products[from_idx:to_idx]
    next_page = to_idx < len(all_products) and page + 1
    prev_page = to_idx > 1 and page - 1

    template_name = "products/list.html"
    # if request.args.get("only_items"):
    if (
        is_background_request() and request.headers.get("Hx-Target") == "products_list"
    ):  # here we exclude the html body replacement
        template_name = "products/components/items-list-single-page.html"
    return render_template(
        template_name,
        products=products,
        form=form,
        per_page=per_page,  # can be omitted in url address
        next_page=next_page,
        prev_page=prev_page,
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


def get_product(product_id: int):
    product = products_storage.get_by_id(product_id)
    if product:
        return product
    raise NotFound(f"Product with id {product_id} doesn't exist!")


@app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    product = get_product(product_id)
    return render_template(
        "products/details.html",
        product=product,
        form=ProductForm(data=asdict(product)),
    )


@app.put("/<int:product_id>/", endpoint="update")
def update_product(product_id: int):
    product = get_product(product_id)
    form = ProductForm()
    if not form.validate_on_submit():
        response = Response(
            render_template(
                "products/components/form-update.html",
                form=form,
            ),
            status=HTTPStatus.UNPROCESSABLE_ENTITY,
        )
        raise HTTPException(response=response)

    products_storage.update(
        product_id=product_id,
        product_name=form.name.data,
        product_price=form.price.data,
    )
    return render_template(
        "products/components/form-update.html",
        product=product,
        form=form,
    )


@app.delete("/<int:product_id>/", endpoint="delete")  # int is for flask validation
def delete_product(product_id: int):

    # sleep() meme below xD
    d = {}
    for i in range(3_000):
        d[i] = i**i
    # just downgrade to 5_000, 2_000, 1_000

    products_storage.delete(product_id)
    if not request.args.get("redirect"):
        return Response(status=HTTPStatus.NO_CONTENT)  # NO_CONTENT code 204
    url = url_for("products_app.list")
    return redirect(url, code=HTTPStatus.SEE_OTHER)
