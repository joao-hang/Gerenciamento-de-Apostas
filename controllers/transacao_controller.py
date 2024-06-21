from flask_restful import Resource, reqparse
from services.transacao_service import TransacaoService
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('usuario_id', type=int)
parser.add_argument('tipo')
parser.add_argument('valor', type=float)

class TransacaoResource(Resource):
    def get(self, transacao_id):
        transacao = TransacaoService.get_transacao_by_id(transacao_id)
        if transacao:
            return {
                'id': transacao.id,
                'usuario_id': transacao.usuario_id,
                'tipo': transacao.tipo,
                'valor': transacao.valor,
                'data': transacao.data.isoformat()
            }
        return {'message': 'Transação não encontrada'}, 404

    def put(self, transacao_id):
        args = parser.parse_args()
        transacao = TransacaoService.update_transacao(transacao_id, args['usuario_id'], args['tipo'], args['valor'])
        if transacao:
            return {'message': 'Transação atualizada com sucesso'}
        return {'message': 'Transação não encontrada'}, 404

    def delete(self, transacao_id):
        transacao = TransacaoService.delete_transacao(transacao_id)
        if transacao:
            return {'message': 'Transação deletada com sucesso'}
        return {'message': 'Transação não encontrada'}, 404

class TransacaoListResource(Resource):
    def get(self):
        transacoes = TransacaoService.get_all_transacoes()
        return [{'id': t.id, 'usuario_id': t.usuario_id, 'tipo': t.tipo, 'valor': t.valor, 'data': t.data.isoformat()} for t in transacoes]

    def post(self):
        args = parser.parse_args()
        TransacaoService.create_transacao(args['usuario_id'], args['tipo'], args['valor'])
        return {'message': 'Transação criada com sucesso'}, 201
