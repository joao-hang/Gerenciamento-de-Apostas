from sqlalchemy.orm import Session
from models import Transacao
from datetime import datetime

class TransacaoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_transacao_by_id(self, transacao_id: int):
        return self.db.query(Transacao).filter(Transacao.id == transacao_id).first()

    def get_all_transacoes(self):
        return self.db.query(Transacao).all()

    def create_transacao(self, usuario_id: int, tipo: str, valor: float):
        nova_transacao = Transacao(usuario_id=usuario_id, tipo=tipo, valor=valor, data=datetime.utcnow())
        self.db.add(nova_transacao)
        self.db.commit()
        return nova_transacao

    def update_transacao(self, transacao_id: int, usuario_id: int, tipo: str, valor: float):
        transacao = self.get_transacao_by_id(transacao_id)
        if transacao:
            transacao.usuario_id = usuario_id
            transacao.tipo = tipo
            transacao.valor = valor
            self.db.commit()
        return transacao

    def delete_transacao(self, transacao_id: int):
        transacao = self.get_transacao_by_id(transacao_id)
        if transacao:
            self.db.delete(transacao)
            self.db.commit()
        return transacao
