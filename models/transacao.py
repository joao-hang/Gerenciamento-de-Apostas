from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from config import Base

class Transacao(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    tipo = Column(String, nullable=False)  # 'deposito' ou 'retirada'
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    usuario = relationship('Usuario', back_populates='transacoes')
