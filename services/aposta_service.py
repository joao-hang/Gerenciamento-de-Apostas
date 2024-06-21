from repositories.aposta_repository import ApostaRepository
from sqlalchemy.orm import Session
from models import Aposta

class ApostaService:
    def __init__(self, db: Session):
        self.aposta_repository = ApostaRepository(db)

    def get_aposta_by_id(self, aposta_id: int):
        return self.aposta_repository.get_aposta_by_id(aposta_id)

    def get_all_apostas(self):
        return self.aposta_repository.get_all_apostas()

    def create_aposta(self, usuario_id: int, evento_id: int, valor: float):
        return self.aposta_repository.create_aposta(usuario_id, evento_id, valor)

    def update_aposta(self, aposta_id: int, usuario_id: int, evento_id: int, valor: float):
        return self.aposta_repository.update_aposta(aposta_id, usuario_id, evento_id, valor)

    def delete_aposta(self, aposta_id: int):
        return self.aposta_repository.delete_aposta(aposta_id)
