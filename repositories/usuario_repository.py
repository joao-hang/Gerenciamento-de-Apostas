from models.usuario import Usuario
from config import Session

class UsuarioRepository:
    
    def get_all():
        session = Session()
        usuarios = session.query(Usuario).all()
        session.close()
        return usuarios

    
    def get_by_id(usuario_id):
        session = Session()
        usuario = session.query(Usuario).get(usuario_id)
        session.close()
        return usuario

    
    def add(usuario):
        session = Session()
        session.add(usuario)
        session.commit()
        session.close()

    
    def update(usuario):
        session = Session()
        session.merge(usuario)
        session.commit()
        session.close()

    
    def delete(usuario):
        session = Session()
        session.delete(usuario)
        session.commit()
        session.close()
