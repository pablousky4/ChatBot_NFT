from src.models.encuesta import EncuestaSimple, EncuestaMultiple

class EncuestaFactory:
    @staticmethod
    def crear_encuesta(tipo, pregunta, opciones, duracion_segundos):
        if tipo == "simple":
            return EncuestaSimple.crear(pregunta, opciones, duracion_segundos)
        elif tipo == "multiple":
            return EncuestaMultiple.crear(pregunta, opciones, duracion_segundos)
        else:
            raise ValueError("Tipo de encuesta no soportado.")
