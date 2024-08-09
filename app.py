# from logging import DEBUG

from flask import Flask

from csrf_protection import csrf
from rest.index import index_app
from rest.examples import examples_app
from rest.clicker import clicker_app
from rest.products import products_app


def create_app():
    app = Flask(__name__)
    # if DEBUG:
    app.config.update(
        # TEMPLATES_AUTO_RELOAD=True,  # this method refreshes the running code if any html template is changed
        # To get your key print in console: python -c "import secrets; print(secrets.token_hex())"
        SECRET_KEY="8148b7148634eeb37192a3d9ebcac7f877a8db21763f667ddaae3d065ba41ce0",
    )
    csrf.init_app(app)  # csrf initialization

    app.register_blueprint(index_app)
    app.register_blueprint(
        examples_app,
        url_prefix="/examples",
    )
    app.register_blueprint(
        clicker_app,
        url_prefix="/clicker",
    )
    app.register_blueprint(
        products_app,
        url_prefix="/products",
    )
    return app


def main():
    app = create_app()
    app.run(
        debug=True,
        port=5050,
    )


# To run via PyCharm button
if __name__ == "__main__":
    main()
