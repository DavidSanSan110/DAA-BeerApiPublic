from flask_restx import fields

from daa_api.api.v1 import api

cerveza = api.model('cerveza', {
    'id': fields.String(required=True, description='Cerveza ID'),
    'nombre': fields.String(required=True, description='Cerveza name'),
    'tipo': fields.String(required=True, description='Cerveza type'),
    'logo': fields.String(required=True, description='Cerveza logo'),
    'descripcion': fields.String(required=True, description='Cerveza description'),
    'grados': fields.Float(required=True, description='Cerveza alcohol content'),
})

get_cervezas_input = api.model('get_cervezas_input', {
    'id_fabricante': fields.String(required=True, description='Fabricante ID'),
})

get_cervezas_output = api.model('get_cervezas_output', {
    'cervezas': fields.List(fields.Nested(cerveza)),
    'message': fields.String(required=True, description='Cervezas retrieved message'),
})

delete_cerveza_input = api.model('delete_cerveza_input', {
    'id_cerveza': fields.String(required=True, description='Cerveza ID'),
})

delete_cerveza_output = api.model('delete_cerveza_output', {
    'deleted': fields.Boolean(required=True, description='Cerveza deleted'),
    'message': fields.String(required=True, description='Cerveza deleted message'),
})

add_ceveza_input = api.model('add_ceveza_input', {
    'id_fabricante': fields.String(required=True, description='Fabricante ID'),
    'nombre': fields.String(required=True, description='Cerveza name'),
    'tipo': fields.String(required=True, description='Cerveza type', enum=['pilsen', 'amber', 'bock', 'pale_ale', 'ipa', 'porter', 'lager', 'stout']),
    'logo': fields.String(required=True, description='Cerveza logo'),
    'descripcion': fields.String(required=True, description='Cerveza description'),
    'grados': fields.Float(required=True, description='Cerveza alcohol content'),
})

add_ceveza_output = api.model('add_ceveza_output', {
    'added': fields.Boolean(required=True, description='Cerveza added'),
    'message': fields.String(required=True, description='Cerveza added message'),
})

update_ceveza_input = api.model('update_ceveza_input', {
    'id_cerveza': fields.String(required=True, description='Cerveza ID'),
    'nombre': fields.String(required=True, description='Cerveza name'),
    'tipo': fields.String(required=True, description='Cerveza type', enum=['pilsen', 'amber', 'bock', 'pale_ale', 'ipa', 'porter', 'lager', 'stout']),
    'logo': fields.String(required=True, description='Cerveza logo'),
    'descripcion': fields.String(required=True, description='Cerveza description'),
    'grados': fields.Float(required=True, description='Cerveza alcohol content'),
})

update_ceveza_output = api.model('update_ceveza_output', {
    'updated': fields.Boolean(required=True, description='Cerveza updated'),
    'message': fields.String(required=True, description='Cerveza updated message'),
})



