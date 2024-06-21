from repositories.transacao_repository import TransacaoRepository
from sqlalchemy.orm import Session
from models import Transacao

class TransacaoService:
    def __init__(self, db: Session):
        self.transacao_repository = TransacaoRepository(db)

    def get_transacao_by_id(self, transacao_id: int):
        return self.transacao_repository.get_transacao_by_id(transacao_id)

    def get_all_transacoes(self):
        return self.transacao_repository.get_all_transacoes()

    def create_transacao(self, usuario_id: int, tipo: str, valor: float):
        return self.transacao_repository.create_transacao(usuario_id, tipo, valor)

    def update_transacao(self, transacao_id: int, usuario_id: int, tipo: str, valor: float):
        return self.transacao_repository.update_transacao(transacao_id, usuario_id, tipo, valor)

    def delete_transacao(self, transacao_id: int):
        return self.transacao_repository.delete_transacao(transacao_id)
