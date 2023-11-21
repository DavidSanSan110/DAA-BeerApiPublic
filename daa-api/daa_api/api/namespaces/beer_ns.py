import flask
import datetime
from time import sleep

import json
from flask_restx import Resource

from daa_api import logger
from daa_api.api.v1 import api
from daa_api.core import cache, limiter
from daa_api.utils import handle400error, handle404error, handle500error

from daa_api.api.models.beer_models import get_cervezas_input, delete_cerveza_input, delete_cerveza_output, add_ceveza_input, add_ceveza_output, update_ceveza_input, update_ceveza_output
from daa_api.api.parsers.beer_parsers import get_cervezas_parser, delete_cerveza_parser, add_ceveza_parser, update_ceveza_parser
from daa_api.model.beer_model import BeerModel

model = BeerModel()

beer_ns = api.namespace('cerveza', description='Beer related operations')
    
@beer_ns.route('/getCervezas')
class GetCervezas(Resource):
    """
    This class handles the GET request for the GetCervezas resource.
    """
    @api.expect(get_cervezas_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    #@api.marshal_with(get_cervezas_output)
    def get(self):
        """
        This function handles the GET request for the GetCervezas resource.
        """
        
        global model

        try:
            params = get_cervezas_parser.parse_args()
            api_key = flask.request.headers.get('X-API-KEY')
        except Exception as e:
            return handle400error(beer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            data, message = model.get_cervezas(api_key, params['id_fabricante'])
        except Exception as e:
            return handle500error(beer_ns, 'Internal server error')
        
        return {'cervezas': data, 'message': message}, 200
    
@beer_ns.route('/deleteCerveza')
class DeleteCerveza(Resource):
    """
    This class handles the DELETE request for the DeleteCerveza resource.
    """
    @api.expect(delete_cerveza_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(delete_cerveza_output)
    def delete(self):
        """
        This function handles the DELETE request for the DeleteCerveza resource.
        """
        
        global model

        try:
            params = delete_cerveza_parser.parse_args()
        except Exception as e:
            return handle400error(beer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            success, message = model.delete_cerveza(params['id_cerveza'])
        except Exception as e:
            return handle500error(beer_ns, 'Internal server error')
        
        return {'deleted': success, 'message': message}, 200
    
@beer_ns.route('/addCerveza')
class AddCerveza(Resource):
    """
    This class handles the POST request for the AddCerveza resource.
    """
    @api.expect(add_ceveza_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(add_ceveza_output)
    def post(self):
        """
        This function handles the POST request for the AddCerveza resource.
        """
        
        global model

        try:
            params = add_ceveza_parser.parse_args()
        except Exception as e:
            return handle400error(beer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            success, message = model.add_cerveza(params['id_fabricante'], params['nombre'], params['tipo'], params['logo'], params['descripcion'], params['grados'])
        except Exception as e:
            return handle500error(beer_ns, 'Internal server error')
        
        return {'added': success, 'message': message}, 200
    
@beer_ns.route('/updateCerveza')
class UpdateCerveza(Resource):
    """
    This class handles the PUT request for the UpdateCerveza resource.
    """
    @api.expect(update_ceveza_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(update_ceveza_output)
    def put(self):
        """
        This function handles the PUT request for the UpdateCerveza resource.
        """
        
        global model

        try:
            params = update_ceveza_parser.parse_args()
        except Exception as e:
            return handle400error(beer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            success, message = model.update_cerveza(params['id_cerveza'], params['nombre'], params['tipo'], params['logo'], params['descripcion'], params['grados'])
        except Exception as e:
            return handle500error(beer_ns, 'Internal server error')
        
        return {'updated': success, 'message': message}, 200