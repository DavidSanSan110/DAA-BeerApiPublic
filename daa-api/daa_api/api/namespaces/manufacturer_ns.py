import flask
import datetime
from time import sleep

import json
from flask_restx import Resource

from daa_api import logger
from daa_api.api.v1 import api
from daa_api.core import cache, limiter
from daa_api.utils import handle400error, handle404error, handle500error

from daa_api.api.models.manufacturer_models import get_fabricantes_output, delete_fabricante_input, delete_fabricante_output, add_fabricante_input, add_fabricante_output
from daa_api.api.parsers.manufacturer_parsers import delete_fabricante_parser, add_fabricante_parser
from daa_api.model.manufacturer_model import ManufacturerModel

model = ManufacturerModel()

manufacturer_ns = api.namespace('fabricante', description='Manufacturer related operations')

@manufacturer_ns.route('/getFabricantes')
class GetFabricantes(Resource):
    """
    This class handles the GET request for the GetFabricantes resource.
    """
    #@api.expect(get_fabricantes_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(get_fabricantes_output)
    def get(self):
        """
        This function handles the GET request for the GetFabricantes resource.
        """
        
        global model

        try:
            api_key = flask.request.headers.get('X-API-KEY')
        except Exception as e:
            return handle400error(manufacturer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            data, message = model.get_fabricantes(api_key)
        except Exception as e:
            return handle500error(manufacturer_ns, 'Internal server error')
        
        return {'fabricantes': data, 'message': message}, 200
    
@manufacturer_ns.route('/deleteFabricante')
class DeleteFabricante(Resource):
    """
    This class handles the DELETE request for the DeleteFabricante resource.
    """
    @api.expect(delete_fabricante_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(delete_fabricante_output)
    def delete(self):
        """
        This function handles the DELETE request for the DeleteFabricante resource.
        """
        
        global model

        try:
            params = delete_fabricante_parser.parse_args()
        except Exception as e:
            return handle400error(manufacturer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            success, message = model.delete_fabricante(params['id_fabricante'])
        except Exception as e:
            return handle500error(manufacturer_ns, 'Internal server error')
        
        return {'deleted': success, 'message': message}, 200
    
@manufacturer_ns.route('/addFabricante')
class AddFabricante(Resource):
    """
    This class handles the POST request for the AddFabricante resource.
    """
    @api.expect(add_fabricante_input)
    @api.response(404, 'User not found')
    @api.response(500, 'Internal server error')
    @api.response(400, 'Bad request')
    @api.marshal_with(add_fabricante_output)
    def post(self):
        """
        This function handles the POST request for the AddFabricante resource.
        """
        
        global model

        try:
            params = add_fabricante_parser.parse_args()
            api_key = flask.request.headers.get('X-API-KEY')
        except Exception as e:
            return handle400error(manufacturer_ns, 'Malformed request. Please, check the request at /v1')
    
        try:
            success, message = model.add_fabricante(params['nombre'], params['logo'], api_key)
        except Exception as e:
            return handle500error(manufacturer_ns, 'Internal server error')
        
        return {'added': success, 'message': message}, 200