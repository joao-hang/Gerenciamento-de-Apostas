from repositories.notificacao_repository import NotificacaoRepository
from sqlalchemy.orm import Session
from models import Notificacao

class NotificacaoService:
    def __init__(self, db: Session):
        self.notificacao_repository = NotificacaoRepository(db)

    def get_notificacao_by_id(self, notificacao_id: int):
        return self.notificacao_repository.get_notificacao_by_id(notificacao_id)

    def get_all_notificacoes(self):
        return self.notificacao_repository.get_all_notificacoes()

    def create_notificacao(self, usuario_id: int, mensagem: str):
        return self.notificacao_repository.create_notificacao(usuario_id, mensagem)

    def update_notificacao(self, notificacao_id: int, usuario_id: int, mensagem: str):
        return self.notificacao_repository.update_notificacao(notificacao_id, usuario_id, mensagem)

    def delete_notificacao(self, notificacao_id: int):
        return self.notificacao_repository.delete_notificacao(notificacao_id)
