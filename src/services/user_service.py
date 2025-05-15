import uuid
import bcrypt
from src.repositories.usuario_repo import UsuarioRepository
from src.models.usuario import Usuario


class UserService:
    def __init__(self, usuario_repo: UsuarioRepository):
        self.usuario_repo = usuario_repo
        self.sesiones = {}  # username -> session_token

    def register(self, username, password):
        if self.usuario_repo.buscar_por_username(username):
            raise ValueError("El usuario ya existe.")
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        usuario = Usuario(username=username, password_hash=password_hash.decode())
        self.usuario_repo.guardar_usuario(usuario)
        return True

    def login(self, username, password):
        usuario = self.usuario_repo.buscar_por_username(username)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        if bcrypt.checkpw(password.encode(), usuario.password_hash.encode()):
            token = str(uuid.uuid4())
            self.sesiones[username] = token
            return token
        else:
            raise ValueError("Contraseña incorrecta")

    def esta_logueado(self, username):
        return username in self.sesiones
