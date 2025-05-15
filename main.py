import argparse
from src.ui.gradio_app import lanzar_ui
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService
from src.controllers.cli_controller import CLIController
from src.controllers.ui_controller import UIController
from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo import UsuarioRepository
from src.repositories.nft_repo import NFTRepository
from src.config import load_config
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main():
    config = load_config()

    # Inicializar repositorios
    encuesta_repo = EncuestaRepository()
    usuario_repo = UsuarioRepository()
    nft_repo = NFTRepository()

    # Inicializar servicios
    nft_service = NFTService(nft_repo)
    poll_service = PollService(encuesta_repo, nft_service)
    user_service = UserService(usuario_repo)
    chatbot_service = ChatbotService(poll_service)
    lanzar_ui(poll_service, chatbot_service, nft_service) ####COMENTAR ESTA LÍNEA PARA EJECUTAR EN CONSOLA Y NO EN GRADIO

    if "--ui" in sys.argv:
        ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)
        ui_controller.launch()
    else:
        cli_controller = CLIController(poll_service, user_service, nft_service, chatbot_service)
        cli_controller.cmdloop()

if __name__ == "__main__":
    main()
