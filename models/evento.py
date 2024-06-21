from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from config import Base

class Evento(Base):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    odds = Column(Float, nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    ativo = Column(Boolean, default=True)

    apostas = relationship('Aposta', back_populates='evento')
