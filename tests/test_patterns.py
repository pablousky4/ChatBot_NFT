from src.patterns.strategy import AlfabetoStrategy, AleatorioStrategy
from src.models.encuesta import Poll

def test_alfabeto_strategy():
    poll = Poll("¿Letra favorita?", ["A", "B", "C"], 60)
    poll.votos = {"A": 2, "B": 2}
    ganador = AlfabetoStrategy().resolver(poll)
    assert ganador == "A"  # Alfabéticamente

def test_aleatorio_strategy(monkeypatch):
    monkeypatch.setattr("random.choice", lambda x: "B")
    poll = Poll("¿Letra?", ["A", "B"], 60)
    poll.votos = {"A": 2, "B": 2}
    ganador = AleatorioStrategy().resolver(poll)
    assert ganador == "B"
