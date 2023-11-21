import threading


from flask_cors import CORS
from flask import Flask, Blueprint, redirect, request, g

from daa_api import config, logger
from daa_api.api.v1 import api
from daa_api.api import namespaces
from daa_api.core import cache, limiter

from daa_api.model.db_model import PostgresSingleton

db = PostgresSingleton.getInstance()
db.connect()



app = Flask(__name__)

@app.before_request
def before_request():
    """
    This function is called before each request.
    """

    if "cerveza" in request.url or "fabricante" in request.url:
        try:
            print(f'Before request: {request.method} {request.url}')
            logger.info(f'Before request: {request.method} {request.url}')
            query = "SELECT * FROM public.api_key WHERE api_key = %s"
            params = (request.headers.get('X-API-KEY'),)
            db.execute(query, params)
            result = db.fetchOne()
            print(result)
            if result is None:
                return "Unauthorized", 401
            else:
                print("Authorized")
                query = "UPDATE public.api_key SET requests = CASE WHEN last_time < NOW() - INTERVAL '1 hour' THEN 1 ELSE requests + 1 END, last_time = CASE WHEN last_time < NOW() - INTERVAL '1 hour' THEN NOW() ELSE last_time END WHERE api_key = %s RETURNING requests"
                params = (request.headers.get('X-API-KEY'),)
                db.execute(query, params)
                result = db.fetchOne()
                print(result)
                g.remaining_requests = 50 - result[0]
                logger.info(f'Remaining requests: {g.remaining_requests}')
                if g.remaining_requests < 0:
                    return "Too many requests", 429
        except Exception as e:
            print("Error before request: ", e)
            logger.error(f'Error before request: {e}')
            return "Internal server error", 500
        


VERSION = (1, 0)
AUTHOR = 'DAA'


def get_version():
    """
    This function returns the API version that is being used.
    """

    return '.'.join(map(str, VERSION))


def get_authors():
    """
    This function returns the API's author name.
    """

    return str(AUTHOR)


__version__ = get_version()
__author__ = get_authors()
    

@app.route('/')
def register_redirection():
    """
    Redirects to dcoumentation page.
    """

    return redirect(f'{request.url_root}/{config.URL_PREFIX}', code=302)

def initialize_app(flask_app):
    """
    This function initializes the Flask Application, adds the namespace and registers the blueprint.
    """

    CORS(flask_app)

    v1 = Blueprint('api', __name__, url_prefix=config.URL_PREFIX)
    api.init_app(v1)

    limiter.exempt(v1)
    cache.init_app(flask_app)

    flask_app.register_blueprint(v1)
    flask_app.config.from_object(config)

    for ns in namespaces:
        api.add_namespace(ns)


def main():
    initialize_app(app)
    separator_str = ''.join(map(str, ["=" for i in range(175)]))
    print(separator_str)
    print(f'Debug mode: {config.DEBUG_MODE}')
    print(f'Authors: {get_authors()}')
    print(f'Version: {get_version()}')
    print(f'Base URL: http://localhost:{config.PORT}{config.URL_PREFIX}')
    print(separator_str)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG_MODE)




if __name__ == '__main__':
    main()