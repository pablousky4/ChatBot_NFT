https://github.com/pablousky4/ChatBot_NFT
# ChatBot_NFT

# ChatBot NFT - Sistema de Votación y Tokens

## Descripción

Este es un sistema de votación basado en encuestas con la integración de tokens NFT. Los usuarios pueden registrarse, votar en encuestas, y recibir tokens NFT como recompensa. Además, pueden transferir sus tokens a otros usuarios.

## Comandos Disponibles

### 1. `registrar`
Registra un nuevo usuario en el sistema.

**Uso**: 
registrar <username> <password>

**Ejemplo**:
(streamer)> registrar juan123 password321
Registro exitoso.

login <username> <password>
(streamer)> login juan123 password321
Bienvenido, juan123!

crear_encuesta <tipo> <duración> <pregunta> | <opciones separadas por coma>
(streamer)> crear_encuesta pública 10 "¿Cuál es tu comida favorita?" | Pizza, Hamburguesa, Pasta
Encuesta creada con ID: 1234

listar_encuestas
(streamer)> listar_encuestas
1234: ¿Cuál es tu comida favorita? (Activa)
5678: ¿Qué comida prefieres? (Cerrada)

votar <poll_id> <opcion>
(streamer)> votar 1234 Pizza
Voto registrado. Token NFT generado.
cerrar_encuesta <poll_id>
(streamer)> cerrar_encuesta 1234
Encuesta cerrada.

ver_resultados <poll_id>
(streamer)> ver_resultados 1234
Resultados: Pizza - 50%, Hamburguesa - 30%, Pasta - 20%

mis_tokens
(streamer)> mis_tokens
001 → Pizza (Encuesta 1234)
002 → Hamburguesa (Encuesta 5678)

transferir_token <token_id> <nuevo_usuario>
(streamer)> transferir_token 001 maria456
Transferencia exitosa.

salir
(streamer)> salir
¡Hasta pronto!

## Pruebas y Cobertura

Para ejecutar todas las pruebas:

pytest

git clone <url-del-repositorio>
