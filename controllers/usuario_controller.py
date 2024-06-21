from flask_restful import Resource, reqparse
from services.usuario_service import UsuarioService

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('email')
parser.add_argument('senha')
parser.add_argument('cpf')
parser.add_argument('saldo', type=float)

class UsuarioResource(Resource):
    def get(self, usuario_id):
        usuario = UsuarioService.get_usuario_by_id(usuario_id)
        if usuario:
            return {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email,
                'cpf': usuario.cpf,
                'saldo': usuario.saldo
            }
        return {'message': 'Usuario não encontrado'}, 404

    def put(self, usuario_id):
        args = parser.parse_args()
        usuario = UsuarioService.update_usuario(usuario_id, args['nome'], args['email'], args['senha'], args['cpf'], args['saldo'])
        if usuario:
            return {'message': 'Usuario atualizado com sucesso'}
        return {'message': 'Usuario não encontrado'}, 404

    def delete(self, usuario_id):
        usuario = UsuarioService.delete_usuario(usuario_id)
        if usuario:
            return {'message': 'Usuario deletado com sucesso'}
        return {'message': 'Usuario não encontrado'}, 404

class UsuarioListResource(Resource):
    def get(self):
        usuarios = UsuarioService.get_all_usuarios()
        return [{'id': u.id, 'nome': u.nome, 'email': u.email, 'cpf': u.cpf, 'saldo': u.saldo} for u in usuarios]

    def post(self):
        args = parser.parse_args()
        UsuarioService.create_usuario(args['nome'], args['email'], args['senha'], args['cpf'], args['saldo'])
        return {'message': 'Usuario criado com sucesso'}, 201
