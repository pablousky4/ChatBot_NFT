from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime, timedelta
from uuid import uuid4


@dataclass
class Encuesta:
    id: str
    pregunta: str
    opciones: List[str]
    votos: Dict[str, int]
    estado: str  # "activa" o "cerrada"
    timestamp_inicio: datetime
    duracion_segundos: int

    def __post_init__(self):
        self.votos = {op: 0 for op in self.opciones}

    def cerrar(self):
        self.estado = "cerrada"

    def ha_expirado(self):
        return datetime.now() > self.timestamp_inicio + timedelta(seconds=self.duracion_segundos)

    def votar(self, opcion):
        if self.estado != "activa":
            raise Exception("La encuesta no está activa.")
        if opcion not in self.opciones:
            raise ValueError("Opción inválida.")
        self.votos[opcion] += 1
