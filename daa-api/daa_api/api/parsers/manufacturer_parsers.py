from flask_restx import reqparse, inputs

delete_fabricante_parser = reqparse.RequestParser()
delete_fabricante_parser.add_argument('id_fabricante', type=str, required=True, help='Fabricante ID')

add_fabricante_parser = reqparse.RequestParser()
add_fabricante_parser.add_argument('nombre', type=str, required=True, help='Fabricante name', location='json')
add_fabricante_parser.add_argument('logo', type=str, required=True, help='Fabricante logo', location='json')