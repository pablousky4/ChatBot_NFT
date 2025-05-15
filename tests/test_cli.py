from src.controllers.cli_controller import CLIController
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

def test_register_login(monkeypatch):
    cli = CLIController(PollService(), UserService(), NFTService(), ChatbotService())
    monkeypatch.setattr("builtins.input", lambda _: "testuser")
    cli.onecmd("registrar testuser pass123")
    cli.onecmd("login testuser pass123")
    assert cli.current_user == "testuser"
