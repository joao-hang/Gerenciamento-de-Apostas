from sqlalchemy.orm import Session
from models import Aposta
from datetime import datetime

class ApostaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_aposta_by_id(self, aposta_id: int):
        return self.db.query(Aposta).filter(Aposta.id == aposta_id).first()

    def get_all_apostas(self):
        return self.db.query(Aposta).all()

    def create_aposta(self, usuario_id: int, evento_id: int, valor: float):
        nova_aposta = Aposta(usuario_id=usuario_id, evento_id=evento_id, valor=valor, data=datetime.utcnow())
        self.db.add(nova_aposta)
        self.db.commit()
        return nova_aposta

    def update_aposta(self, aposta_id: int, usuario_id: int, evento_id: int, valor: float):
        aposta = self.get_aposta_by_id(aposta_id)
        if aposta:
            aposta.usuario_id = usuario_id
            aposta.evento_id = evento_id
            aposta.valor = valor
            self.db.commit()
        return aposta

    def delete_aposta(self, aposta_id: int):
        aposta = self.get_aposta_by_id(aposta_id)
        if aposta:
            self.db.delete(aposta)
            self.db.commit()
        return aposta
