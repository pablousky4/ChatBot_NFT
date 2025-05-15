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
    parser = argparse.ArgumentParser()
    parser.add_argument("--ui", action="store_true", help="Iniciar interfaz web")
    args = parser.parse_args()

    poll_service = PollService()
    user_service = UserService()
    nft_service = NFTService()
    chatbot_service = ChatbotService()

    if args.ui:
        lanzar_ui(poll_service, chatbot_service, nft_service)
    else:
        cli = CLIController(poll_service, user_service, nft_service, chatbot_service)
        cli.cmdloop()

if __name__ == "__main__":
    main()
