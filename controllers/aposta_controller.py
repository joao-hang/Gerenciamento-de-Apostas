from flask_restful import Resource, reqparse
from services.aposta_service import ApostaService
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('usuario_id', type=int)
parser.add_argument('evento_id', type=int)
parser.add_argument('valor', type=float)

class ApostaResource(Resource):
    def get(self, aposta_id):
        aposta = ApostaService.get_aposta_by_id(aposta_id)
        if aposta:
            return {
                'id': aposta.id,
                'usuario_id': aposta.usuario_id,
                'evento_id': aposta.evento_id,
                'valor': aposta.valor,
                'data': aposta.data.isoformat()
            }
        return {'message': 'Aposta não encontrada'}, 404

    def put(self, aposta_id):
        args = parser.parse_args()
        aposta = ApostaService.update_aposta(aposta_id, args['usuario_id'], args['evento_id'], args['valor'])
        if aposta:
            return {'message': 'Aposta atualizada com sucesso'}
        return {'message': 'Aposta não encontrada'}, 404

    def delete(self, aposta_id):
        aposta = ApostaService.delete_aposta(aposta_id)
        if aposta:
            return {'message': 'Aposta deletada com sucesso'}
        return {'message': 'Aposta não encontrada'}, 404

class ApostaListResource(Resource):
    def get(self):
        apostas = ApostaService.get_all_apostas()
        return [{'id': a.id, 'usuario_id': a.usuario_id, 'evento_id': a.evento_id, 'valor': a.valor, 'data': a.data.isoformat()} for a in apostas]

    def post(self):
        args = parser.parse_args()
        ApostaService.create_aposta(args['usuario_id'], args['evento_id'], args['valor'])
        return {'message': 'Aposta criada com sucesso'}, 201
