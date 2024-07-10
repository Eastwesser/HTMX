from flask import request


# We check if it is background or not
def is_background_request():
    is_hx_request = request.headers.get("Hx-Request")
    is_hx_boosted = request.headers.get("Hx-Boosted")

    return bool(is_hx_request and not is_hx_boosted)
