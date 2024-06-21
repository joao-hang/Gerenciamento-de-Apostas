from datetime import datetime
from repositories.evento_repository import EventoRepository
from sqlalchemy.orm import Session
from models import Evento

class EventoService:
    def __init__(self, db: Session):
        self.evento_repository = EventoRepository(db)

    def get_evento_by_id(self, evento_id: int):
        return self.evento_repository.get_evento_by_id(evento_id)

    def get_all_eventos(self):
        return self.evento_repository.get_all_eventos()

    def create_evento(self, nome: str, odds: float, data_inicio: datetime, ativo: bool):
        return self.evento_repository.create_evento(nome, odds, data_inicio, ativo)

    def update_evento(self, evento_id: int, nome: str, odds: float, data_inicio: datetime, ativo: bool):
        return self.evento_repository.update_evento(evento_id, nome, odds, data_inicio, ativo)

    def delete_evento(self, evento_id: int):
        return self.evento_repository.delete_evento(evento_id)
