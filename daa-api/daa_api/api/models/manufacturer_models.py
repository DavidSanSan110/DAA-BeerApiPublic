from flask_restx import fields

from daa_api.api.v1 import api

fabricante = api.model('fabricante', {
    'id': fields.String(required=True, description='Fabricante ID'),
    'nombre': fields.String(required=True, description='Fabricante name'),
    'logo': fields.String(required=True, description='Fabricante logo'),
})

get_fabricantes_output = api.model('get_fabricantes_output', {
    'fabricantes': fields.List(fields.Nested(fabricante)),
    'message': fields.String(required=True, description='Fabricantes retrieved message'),
})

delete_fabricante_input = api.model('delete_fabricante_input', {
    'id_fabricante': fields.String(required=True, description='Fabricante ID'),
})

delete_fabricante_output = api.model('delete_fabricante_output', {
    'deleted': fields.Boolean(required=True, description='Fabricante deleted'),
    'message': fields.String(required=True, description='Fabricante deleted message'),
})

add_fabricante_input = api.model('add_fabricante_input', {
    'nombre': fields.String(required=True, description='Fabricante name'),
    'logo': fields.String(required=True, description='Fabricante logo'),
})

add_fabricante_output = api.model('add_fabricante_output', {
    'added': fields.Boolean(required=True, description='Fabricante added'),
    'message': fields.String(required=True, description='Fabricante added message'),
})