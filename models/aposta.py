from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from config import Base

class Aposta(Base):
    __tablename__ = 'apostas'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    usuario = relationship('Usuario', back_populates='apostas')
    evento = relationship('Evento', back_populates='apostas')
