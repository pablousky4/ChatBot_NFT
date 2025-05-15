import gradio as gr
from src.services.poll_service import PollService
from src.services.chatbot_service import ChatbotService
from src.services.nft_service import NFTService
from src.services.user_service import UserService

class UIController:
    def __init__(self, poll_service: PollService, chatbot_service: ChatbotService,
                 nft_service: NFTService, user_service: UserService):
        self.poll_service = poll_service
        self.chatbot_service = chatbot_service
        self.nft_service = nft_service
        self.user_service = user_service

    def launch(self):
        with gr.Blocks() as demo:
            gr.Markdown("# 📊 Votaciones Interactivas para Streamers")

            with gr.Tab("Encuestas"):
                poll_dropdown = gr.Dropdown(label="Encuestas activas")
                option_radio = gr.Radio(label="Opciones", choices=[])
                user_input = gr.Textbox(label="Tu nombre de usuario")
                vote_btn = gr.Button("Votar")
                vote_output = gr.Textbox(label="Resultado")

                def update_options(poll_id):
                    poll = self.poll_service.get_poll_by_id(poll_id)
                    return gr.update(choices=poll.opciones)

                def votar(poll_id, opcion, username):
                    self.poll_service.vote(poll_id, username, opcion)
                    return f"¡Voto registrado para {opcion}!"

                poll_dropdown.change(update_options, poll_dropdown, option_radio)
                vote_btn.click(votar, [poll_dropdown, option_radio, user_input], vote_output)

            with gr.Tab("Chatbot"):
                chatbot = gr.ChatInterface(fn=self.chatbot_service.get_response)

            with gr.Tab("Mis Tokens"):
                username_input = gr.Textbox(label="Nombre de usuario")
                get_btn = gr.Button("Ver tokens")
                tokens_output = gr.Dataframe(headers=["token_id", "poll_id", "option", "issued_at"])

                def get_tokens(username):
                    tokens = self.nft_service.get_tokens(username)
                    return [list(t.values()) for t in tokens]

                get_btn.click(get_tokens, username_input, tokens_output)

        demo.launch()
