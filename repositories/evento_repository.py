from sqlalchemy.orm import Session
from models import Evento
from datetime import datetime

class EventoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_evento_by_id(self, evento_id: int):
        return self.db.query(Evento).filter(Evento.id == evento_id).first()

    def get_all_eventos(self):
        return self.db.query(Evento).all()

    def create_evento(self, nome: str, odds: float, data_inicio: datetime, ativo: bool):
        novo_evento = Evento(nome=nome, odds=odds, data_inicio=data_inicio, ativo=ativo)
        self.db.add(novo_evento)
        self.db.commit()
        return novo_evento

    def update_evento(self, evento_id: int, nome: str, odds: float, data_inicio: datetime, ativo: bool):
        evento = self.get_evento_by_id(evento_id)
        if evento:
            evento.nome = nome
            evento.odds = odds
            evento.data_inicio = data_inicio
            evento.ativo = ativo
            self.db.commit()
        return evento

    def delete_evento(self, evento_id: int):
        evento = self.get_evento_by_id(evento_id)
        if evento:
            self.db.delete(evento)
            self.db.commit()
        return evento
