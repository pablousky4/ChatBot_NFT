import json
import os
from src.models.usuario import Usuario


class UsuarioRepository:
    FILE = "data/usuarios.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def guardar_usuario(self, usuario: Usuario):
        usuarios = self.listar_todos()
        usuarios = [u for u in usuarios if u.username != usuario.username]
        usuarios.append(usuario)
        with open(self.FILE, "w") as f:
            json.dump([u.__dict__ for u in usuarios], f)

    def buscar_por_username(self, username: str):
        usuarios = self.listar_todos()
        for u in usuarios:
            if u.username == username:
                return Usuario(**u)
        return None

    def listar_todos(self):
        with open(self.FILE, "r") as f:
            data = json.load(f)
        return [Usuario(**u) for u in data]
