import pytest
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService

def test_create_and_vote():
    poll_service = PollService()
    user_service = UserService()
    nft_service = NFTService()

    user_service.register("alice", "password")
    poll = poll_service.create_poll("¿Café o té?", ["Café", "Té"], 60)

    poll_service.vote(poll.id, "alice", "Café")
    results = poll_service.get_partial_results(poll.id)
    assert results["Café"] == 1

    with pytest.raises(Exception):
        poll_service.vote(poll.id, "alice", "Té")  # Repetido

def test_auto_close_poll():
    poll_service = PollService()
    poll = poll_service.create_poll("¿Amanecer o atardecer?", ["Amanecer", "Atardecer"], 0)
    import time; time.sleep(1)
    poll_service._check_auto_close()  # Método privado expuesto para test
    assert not poll.activa
