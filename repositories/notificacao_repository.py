from sqlalchemy.orm import Session
from models import Notificacao
from datetime import datetime

class NotificacaoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_notificacao_by_id(self, notificacao_id: int):
        return self.db.query(Notificacao).filter(Notificacao.id == notificacao_id).first()

    def get_all_notificacoes(self):
        return self.db.query(Notificacao).all()

    def create_notificacao(self, usuario_id: int, mensagem: str):
        nova_notificacao = Notificacao(usuario_id=usuario_id, mensagem=mensagem, data=datetime.utcnow())
        self.db.add(nova_notificacao)
        self.db.commit()
        return nova_notificacao

    def update_notificacao(self, notificacao_id: int, usuario_id: int, mensagem: str):
        notificacao = self.get_notificacao_by_id(notificacao_id)
        if notificacao:
            notificacao.usuario_id = usuario_id
            notificacao.mensagem = mensagem
            self.db.commit()
        return notificacao

    def delete_notificacao(self, notificacao_id: int):
        notificacao = self.get_notificacao_by_id(notificacao_id)
        if notificacao:
            self.db.delete(notificacao)
            self.db.commit()
        return notificacao
