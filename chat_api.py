import openai
import os

# Configura la clave API de OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define el modelo y el contexto
model_engine = "text-davinci-002"
# prompt_text = "Hola, ¿cómo estás?"

while True:

    # Lee la entrada del usuario
    prompt_text = input('Ariel: ')

    # Genera una respuesta de ChatGPT
    # response = generate_text(prompt_text)

    response = openai.Completion.create(
        model_engine,
        prompt_text,
        max_tokens=50
    )

    # Obtiene la respuesta del modelo
    output_text = response.choices[0].text

    # Imprime la respuesta del modelo
    print('ChatGPT: ' + output_text)




