import cmd
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

class CLIController(cmd.Cmd):
    intro = "Bienvenido al sistema de votación. Escribe ayuda o ? para listar comandos.\n"
    prompt = "(streamer)> "

    def __init__(self, poll_service: PollService, user_service: UserService,
                 nft_service: NFTService, chatbot_service: ChatbotService):
        super().__init__()
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service
        self.chatbot_service = chatbot_service
        self.current_user = None

    def do_registrar(self, arg):
        "Registrar nuevo usuario: registrar <username> <password>"
        args = arg.split()
        if len(args) != 2:
            print("Uso: registrar <usuario> <contraseña>")
            return
        username, password = args
        try:
            self.user_service.register(username, password)
            print("Registro exitoso.")
        except Exception as e:
            print(f"Error: {e}")

    def do_login(self, arg):
        "Iniciar sesión: login <username> <password>"
        args = arg.split()
        if len(args) != 2:
            print("Uso: login <usuario> <contraseña>")
            return
        username, password = args
        if self.user_service.login(username, password):
            self.current_user = username
            print(f"Bienvenido, {username}!")
        else:
            print("Credenciales incorrectas.")

    def do_crear_encuesta(self, arg):
        "Crear encuesta: crear_encuesta <tipo> <duración> <pregunta> | opciones separadas por coma"
        try:
            tipo, duracion, pregunta_y_opciones = arg.split(" ", 2)
            duracion = int(duracion)
            pregunta, opciones_str = pregunta_y_opciones.split("|")
            opciones = [o.strip() for o in opciones_str.split(",")]
            encuesta = self.poll_service.create_poll(pregunta.strip(), opciones, duracion, tipo)
            print(f"Encuesta creada con ID: {encuesta.id}")
        except Exception as e:
            print(f"Error: {e}")

    def do_listar_encuestas(self, _):
        "Listar encuestas activas"
        encuestas = self.poll_service.list_active_polls()
        for e in encuestas:
            print(f"{e.id}: {e.pregunta} ({'Activa' if e.activa else 'Cerrada'})")

    def do_votar(self, arg):
        "Votar en encuesta: votar <poll_id> <opcion>"
        if not self.current_user:
            print("Debes iniciar sesión.")
            return
        args = arg.split()
        if len(args) != 2:
            print("Uso: votar <id_encuesta> <opcion>")
            return
        poll_id, opcion = args
        try:
            self.poll_service.vote(poll_id, self.current_user, opcion)
            print("Voto registrado. Token NFT generado.")
        except Exception as e:
            print(f"Error: {e}")

    def do_cerrar_encuesta(self, arg):
        "Cerrar encuesta manualmente: cerrar_encuesta <poll_id>"
        try:
            self.poll_service.close_poll(arg.strip())
            print("Encuesta cerrada.")
        except Exception as e:
            print(f"Error: {e}")

    def do_ver_resultados(self, arg):
        "Ver resultados finales: ver_resultados <poll_id>"
        try:
            res = self.poll_service.get_final_results(arg.strip())
            print(res)
        except Exception as e:
            print(f"Error: {e}")

    def do_mis_tokens(self, _):
        "Mostrar tokens NFT del usuario actual"
        if not self.current_user:
            print("Debes iniciar sesión.")
            return
        tokens = self.nft_service.get_tokens_by_user(self.current_user)
        for t in tokens:
            print(f"{t.token_id} → {t.option} (Encuesta {t.poll_id})")

    def do_transferir_token(self, arg):
        "Transferir token: transferir_token <token_id> <nuevo_usuario>"
        if not self.current_user:
            print("Debes iniciar sesión.")
            return
        try:
            token_id, nuevo_owner = arg.split()
            self.nft_service.transfer_token(token_id, self.current_user, nuevo_owner)
            print("Transferencia exitosa.")
        except Exception as e:
            print(f"Error: {e}")

    def do_salir(self, _):
        "Salir del programa"
        print("¡Hasta pronto!")
        return True
