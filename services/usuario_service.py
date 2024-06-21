from repositories.usuario_repository import UsuarioRepository
from sqlalchemy.orm import Session
from models import Usuario

class UsuarioService:
    def __init__(self, db: Session):
        self.usuario_repository = UsuarioRepository(db)

    def get_usuario_by_id(self, usuario_id: int):
        return self.usuario_repository.get_usuario_by_id(usuario_id)

    def get_usuario_by_email(self, email: str):
        return self.usuario_repository.get_usuario_by_email(email)

    def get_all_usuarios(self):
        return self.usuario_repository.get_all_usuarios()

    def create_usuario(self, nome: str, email: str, senha: str, cpf: str):
        return self.usuario_repository.create_usuario(nome, email, senha, cpf)

    def update_usuario(self, usuario_id: int, nome: str, email: str, senha: str, cpf: str):
        return self.usuario_repository.update_usuario(usuario_id, nome, email, senha, cpf)

    def delete_usuario(self, usuario_id: int):
        return self.usuario_repository.delete_usuario(usuario_id)
