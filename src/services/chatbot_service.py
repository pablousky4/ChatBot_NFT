from transformers import pipeline
from datetime import datetime
from src.services.poll_service import PollService


class ChatbotService:
    def __init__(self, poll_service: PollService):
        self.pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")
        self.poll_service = poll_service

    def responder(self, username, mensaje):
        mensaje_lc = mensaje.lower()

        if "quién va ganando" in mensaje_lc:
            # Asumimos última encuesta activa
            encuestas = self.poll_service.encuesta_repo.listar_todas()
            activas = [e for e in encuestas if e.estado == "activa"]
            if activas:
                resultados = self.poll_service.get_partial_results(activas[-1].id)
                return f"Resultados parciales: {resultados}"
            else:
                return "No hay encuestas activas ahora mismo."

        if "cuánto falta" in mensaje_lc:
            encuestas = self.poll_service.encuesta_repo.listar_todas()
            activas = [e for e in encuestas if e.estado == "activa"]
            if activas:
                e = activas[-1]
                restante = e.timestamp_inicio.timestamp() + e.duracion_segundos - datetime.now().timestamp()
                return f"Faltan {int(restante)} segundos para cerrar la encuesta."
            else:
                return "No hay encuestas activas ahora mismo."

        # En otros casos, responde con IA
        return self.pipeline(mensaje)[0]['generated_text']
