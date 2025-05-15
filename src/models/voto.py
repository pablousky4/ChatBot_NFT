from dataclasses import dataclass


@dataclass
class Voto:
    username: str
    poll_id: str
    opcion: str
