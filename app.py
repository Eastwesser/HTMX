from flask import Flask

from rest.index import index_app
from rest.examples import examples_app


def create_app():
    app = Flask(__name__)
    app.register_blueprint(index_app)
    app.register_blueprint(
        examples_app,
        url_prefix="/examples",
    )
    return app


def main():
    app = create_app()
    app.run(debug=True)


# To run via PyCharm button
if __name__ == "__main__":
    main()
