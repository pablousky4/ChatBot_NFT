import json
import os
from datetime import datetime
from src.models.encuesta import Encuesta


class EncuestaRepository:
    FILE = "data/encuestas.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def guardar(self, encuesta: Encuesta):
        encuestas = self.listar_todas()
        encuestas = [e for e in encuestas if e.id != encuesta.id]
        encuestas.append(encuesta)
        with open(self.FILE, "w") as f:
            json.dump([{
                **e.__dict__,
                "timestamp_inicio": e.timestamp_inicio.isoformat()
            } for e in encuestas], f)

    def listar_todas(self):
        with open(self.FILE, "r") as f:
            data = json.load(f)
        encuestas = []
        for e in data:
            e["timestamp_inicio"] = datetime.fromisoformat(e["timestamp_inicio"])
            encuestas.append(Encuesta(**e))
        return encuestas

    def buscar_por_id(self, poll_id):
        for e in self.listar_todas():
            if e.id == poll_id:
                return e
        return None
