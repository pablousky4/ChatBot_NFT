import argparse
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService
from src.controllers.cli_controller import CLIController
from src.controllers.ui_controller import UIController
from src.config import load_config
from src.ui.gradio_app import lanzar_ui
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main():
    config = load_config()

    # Inicializar repositorios
    encuesta_repo = EncuestaRepository(config)
    usuario_repo = UsuarioRepository(config)
    nft_repo = NFTRepository(config)

    # Inicializar servicios
    nft_service = NFTService(nft_repo)
    poll_service = PollService(encuesta_repo, nft_service)
    user_service = UserService(usuario_repo)
    chatbot_service = ChatbotService(poll_service)

    if "--ui" in sys.argv:
        ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)
        ui_controller.launch()
    else:
        cli_controller = CLIController(poll_service, user_service, nft_service)
        cli_controller.run()

if __name__ == "__main__":
    main()
