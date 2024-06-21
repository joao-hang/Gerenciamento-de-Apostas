from flask_restful import Resource, reqparse
from services.notificacao_service import NotificacaoService
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('usuario_id', type=int)
parser.add_argument('mensagem')

class NotificacaoResource(Resource):
    def get(self, notificacao_id):
        notificacao = NotificacaoService.get_notificacao_by_id(notificacao_id)
        if notificacao:
            return {
                'id': notificacao.id,
                'usuario_id': notificacao.usuario_id,
                'mensagem': notificacao.mensagem,
                'data': notificacao.data.isoformat()
            }
        return {'message': 'Notificação não encontrada'}, 404

    def put(self, notificacao_id):
        args = parser.parse_args()
        notificacao = NotificacaoService.update_notificacao(notificacao_id, args['usuario_id'], args['mensagem'])
        if notificacao:
            return {'message': 'Notificação atualizada com sucesso'}
        return {'message': 'Notificação não encontrada'}, 404

    def delete(self, notificacao_id):
        notificacao = NotificacaoService.delete_notificacao(notificacao_id)
        if notificacao:
            return {'message': 'Notificação deletada com sucesso'}
        return {'message': 'Notificação não encontrada'}, 404

class NotificacaoListResource(Resource):
    def get(self):
        notificacoes = NotificacaoService.get_all_notificacoes()
        return [{'id': n.id, 'usuario_id': n.usuario_id, 'mensagem': n.mensagem, 'data': n.data.isoformat()} for n in notificacoes]

    def post(self):
        args = parser.parse_args()
        NotificacaoService.create_notificacao(args['usuario_id'], args['mensagem'])
        return {'message': 'Notificação criada com sucesso'}, 201
