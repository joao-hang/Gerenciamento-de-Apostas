from flask_restful import Resource, reqparse
from services.evento_service import EventoService
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('nome')
parser.add_argument('odds', type=float)
parser.add_argument('data_inicio')
parser.add_argument('ativo', type=bool)

class EventoResource(Resource):
    def get(self, evento_id):
        evento = EventoService.get_evento_by_id(evento_id)
        if evento:
            return {
                'id': evento.id,
                'nome': evento.nome,
                'odds': evento.odds,
                'data_inicio': evento.data_inicio.isoformat(),
                'ativo': evento.ativo
            }
        return {'message': 'Evento não encontrado'}, 404

    def put(self, evento_id):
        args = parser.parse_args()
        evento = EventoService.update_evento(evento_id, args['nome'], args['odds'], datetime.fromisoformat(args['data_inicio']), args['ativo'])
        if evento:
            return {'message': 'Evento atualizado com sucesso'}
        return {'message': 'Evento não encontrado'}, 404

    def delete(self, evento_id):
        evento = EventoService.delete_evento(evento_id)
        if evento:
            return {'message': 'Evento deletado com sucesso'}
        return {'message': 'Evento não encontrado'}, 404

class EventoListResource(Resource):
    def get(self):
        eventos = EventoService.get_all_eventos()
        return [{'id': e.id, 'nome': e.nome, 'odds': e.odds, 'data_inicio': e.data_inicio.isoformat(), 'ativo': e.ativo} for e in eventos]

    def post(self):
        args = parser.parse_args()
        EventoService.create_evento(args['nome'], args['odds'], datetime.fromisoformat(args['data_inicio']), args['ativo'])
        return {'message': 'Evento criado com sucesso'}, 201
