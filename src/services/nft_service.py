from src.models.token_nft import TokenNFT
from src.repositories.nft_repo import NFTRepository


class NFTService:
    def __init__(self, nft_repo: NFTRepository):
        self.nft_repo = nft_repo

    def mint_token(self, owner, poll_id, option):
        token = TokenNFT.crear(owner, poll_id, option)
        self.nft_repo.guardar_token(token)

    def transfer_token(self, token_id, nuevo_owner, usuario_actual):
        token = self.nft_repo.buscar_token(token_id)
        if token and token.owner == usuario_actual:
            token.owner = nuevo_owner
            self.nft_repo.guardar_token(token)
        else:
            raise Exception("Transferencia inválida o no autorizada")

    def listar_tokens_usuario(self, username):
        return self.nft_repo.tokens_por_owner(username)
