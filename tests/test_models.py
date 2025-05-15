from src.models.encuesta import Poll

def test_poll_creation():
    poll = Poll("¿Pizza o pasta?", ["Pizza", "Pasta"], 60)
    assert poll.pregunta == "¿Pizza o pasta?"
    assert len(poll.opciones) == 2
    assert poll.activa
