from flask import request


# We check if it is background or not
def is_background_request():
    is_hx_request = request.headers.get("Hx-Request")

    return bool(is_hx_request)
