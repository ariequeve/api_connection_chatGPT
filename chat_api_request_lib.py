import requests

# Reemplazar TU API KEY con tu clave de API
API_KEY = 'TU API KEY'
API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Función para enviar solicitudes a la API de ChatGPT y recibir respuestas
def generate_text(prompt):
    response = requests.post(
        API_URL,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'prompt': prompt,
            'max_tokens': 1024,
            'temperature': 0.5,
            'n': 1,
            'stop': '\n'
        }
    )

    if response.status_code == 200:
        # Devuelve la respuesta en formato JSON
        return response.json()['choices'][0]['text']
    else:
        # Si hubo un error, devuelve un mensaje de error
        return 'Error al generar el texto'

# Loop principal del programa
while True:
    # Lee la entrada del usuario
    prompt = input('Tu: ')

    # Genera una respuesta de ChatGPT
    response = generate_text(prompt)

    # Imprime la respuesta de ChatGPT
    print('ChatGPT: ' + response)
