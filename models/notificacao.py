from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from config import Base

class Notificacao(Base):
    __tablename__ = 'notificacoes'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    mensagem = Column(String, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    usuario = relationship('Usuario', back_populates='notificacoes')
