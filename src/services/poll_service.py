from uuid import uuid4
from datetime import datetime
from src.repositories.encuesta_repo import EncuestaRepository
from src.services.nft_service import NFTService
from src.models.encuesta import Encuesta
from src.models.voto import Voto
from src.patterns.observer import Observable


class PollService(Observable):
    def __init__(self, encuesta_repo: EncuestaRepository, nft_service: NFTService):
        super().__init__()
        self.encuesta_repo = encuesta_repo
        self.nft_service = nft_service
        self.votos_registrados = {}  # poll_id -> set of usernames

    def create_poll(self, pregunta, opciones, duracion_segundos):
        encuesta = Encuesta(
            id=str(uuid4()),
            pregunta=pregunta,
            opciones=opciones,
            votos={},
            estado="activa",
            timestamp_inicio=datetime.now(),
            duracion_segundos=duracion_segundos
        )
        self.encuesta_repo.guardar(encuesta)
        return encuesta.id

    def vote(self, poll_id, username, opcion):
        encuesta = self.encuesta_repo.buscar_por_id(poll_id)
        if not encuesta or encuesta.estado != "activa":
            raise Exception("Encuesta inválida o cerrada.")
        if encuesta.ha_expirado():
            self.close_poll(poll_id)
            raise Exception("La encuesta ya expiró.")

        if poll_id not in self.votos_registrados:
            self.votos_registrados[poll_id] = set()

        if username in self.votos_registrados[poll_id]:
            raise Exception("Usuario ya ha votado.")

        encuesta.votar(opcion)
        self.votos_registrados[poll_id].add(username)
        self.encuesta_repo.guardar(encuesta)

        self.nft_service.mint_token(username, poll_id, opcion)

    def close_poll(self, poll_id):
        encuesta = self.encuesta_repo.buscar_por_id(poll_id)
        if encuesta and encuesta.estado == "activa":
            encuesta.cerrar()
            self.encuesta_repo.guardar(encuesta)
            self.notify_observers(encuesta)

    def get_partial_results(self, poll_id):
        encuesta = self.encuesta_repo.buscar_por_id(poll_id)
        total = sum(encuesta.votos.values())
        return {
            opcion: {
                "votos": count,
                "porcentaje": (count / total * 100) if total > 0 else 0
            } for opcion, count in encuesta.votos.items()
        }

    def get_final_results(self, poll_id):
        encuesta = self.encuesta_repo.buscar_por_id(poll_id)
        if encuesta.estado != "cerrada":
            raise Exception("La encuesta aún está activa.")
        return self.get_partial_results(poll_id)
