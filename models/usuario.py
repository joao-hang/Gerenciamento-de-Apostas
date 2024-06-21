from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from config import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    saldo = Column(Float, default=0.0)

    apostas = relationship('Aposta', back_populates='usuario')
    notificacoes = relationship('Notificacao', back_populates='usuario')
    transacoes = relationship('Transacao', back_populates='usuario')
