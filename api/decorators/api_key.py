from functools import wraps
from flask import request, abort

def require_apikey(view_function):
    @wraps(view_function)
    def decored_function(*args, **kwargs):
        if request.headers.get('x-api-key') == "chave_api_key":
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decored_function()
