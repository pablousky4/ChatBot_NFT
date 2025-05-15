from src.repositories.usuario_repo import UsuarioRepository

def test_user_persistence():
    repo = UsuarioRepository()
    repo.save("usuario", "hashed_pass")
    data = repo.load("usuario")
    assert data["username"] == "usuario"
