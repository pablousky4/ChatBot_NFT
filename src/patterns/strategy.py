import random

class DesempateStrategy:
    def resolver(self, opciones):
        raise NotImplementedError


class DesempateAlfabetico(DesempateStrategy):
    def resolver(self, opciones):
        return sorted(opciones)[0]


class DesempateAleatorio(DesempateStrategy):
    def resolver(self, opciones):
        return random.choice(opciones)


class DesempateProrroga(DesempateStrategy):
    def resolver(self, opciones):
        # Simula una "prórroga" — simplemente devuelve None para marcar como no resuelto
        return None


class ResultadoFormatter:
    def formatear(self, resultados):
        raise NotImplementedError


class ResultadoTexto(ResultadoFormatter):
    def formatear(self, resultados):
        return "\n".join([f"{k}: {v['votos']} votos ({v['porcentaje']:.2f}%)" for k, v in resultados.items()])


class ResultadoJSON(ResultadoFormatter):
    def formatear(self, resultados):
        import json
        return json.dumps(resultados, indent=2)


class ResultadoASCII(ResultadoFormatter):
    def formatear(self, resultados):
        lines = []
        for k, v in resultados.items():
            bar = "#" * int(v["porcentaje"] // 2)
            lines.append(f"{k}: {bar} ({v['porcentaje']:.1f}%)")
        return "\n".join(lines)
