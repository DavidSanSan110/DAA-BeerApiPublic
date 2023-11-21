from flask_restx import reqparse, inputs

get_cervezas_parser = reqparse.RequestParser()
get_cervezas_parser.add_argument('id_fabricante', type=str, required=True, help='Fabricante ID')

delete_cerveza_parser = reqparse.RequestParser()
delete_cerveza_parser.add_argument('id_cerveza', type=str, required=True, help='Cerveza ID')

add_ceveza_parser = reqparse.RequestParser()
add_ceveza_parser.add_argument('id_fabricante', type=str, required=True, help='Fabricante ID', location='json')
add_ceveza_parser.add_argument('nombre', type=str, required=True, help='Cerveza name', location='json')
add_ceveza_parser.add_argument('tipo', type=str, required=True, help='Cerveza type', location='json', choices=['pilsen', 'amber', 'bock', 'pale_ale', 'ipa', 'porter', 'lager', 'stout'])
add_ceveza_parser.add_argument('logo', type=str, required=True, help='Cerveza logo', location='json')
add_ceveza_parser.add_argument('descripcion', type=str, required=True, help='Cerveza description', location='json')
add_ceveza_parser.add_argument('grados', type=float, required=True, help='Cerveza alcohol content', location='json')

update_ceveza_parser = reqparse.RequestParser()
update_ceveza_parser.add_argument('id_cerveza', type=str, required=True, help='Cerveza ID', location='json')
update_ceveza_parser.add_argument('nombre', type=str, required=True, help='Cerveza name', location='json')
update_ceveza_parser.add_argument('tipo', type=str, required=True, help='Cerveza type', location='json', choices=['pilsen', 'amber', 'bock', 'pale_ale', 'ipa', 'porter', 'lager', 'stout'])
update_ceveza_parser.add_argument('logo', type=str, required=True, help='Cerveza logo', location='json')
update_ceveza_parser.add_argument('descripcion', type=str, required=True, help='Cerveza description', location='json')
update_ceveza_parser.add_argument('grados', type=float, required=True, help='Cerveza alcohol content', location='json')
