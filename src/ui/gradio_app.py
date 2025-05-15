import gradio as gr

def lanzar_ui(poll_service, chatbot_service, nft_service):
    def votar(poll_id, opcion, username):
        try:
            poll_service.vote(poll_id, username, opcion)
            return "¡Voto registrado!"
        except Exception as e:
            return str(e)

    def responder(pregunta, username):
        return chatbot_service.responder(username, pregunta)

    def ver_tokens(username):
        tokens = nft_service.get_tokens_by_user(username)
        return [f"{t.option} (ID: {t.token_id})" for t in tokens]

    encuesta_inputs = [
        gr.Textbox(label="ID Encuesta"),
        gr.Textbox(label="Opción"),
        gr.Textbox(label="Usuario")
    ]

    chatbot_inputs = [
        gr.Textbox(label="Pregunta"),
        gr.Textbox(label="Usuario")
    ]

    demo = gr.TabbedInterface(
        interface_list=[
            gr.Interface(fn=votar, inputs=encuesta_inputs, outputs="text", title="Votar en Encuesta"),
            gr.Interface(fn=responder, inputs=chatbot_inputs, outputs="text", title="Chatbot"),
            gr.Interface(fn=ver_tokens, inputs=gr.Textbox(label="Usuario"), outputs="text", title="Mis Tokens")
        ],
        tab_names=["Encuestas", "Chatbot", "Tokens"]
    )

    demo.launch()
