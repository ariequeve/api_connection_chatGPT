import openai
import os

# Define tu clave de API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define el modelo de OpenAI a utilizar (en este caso ChatGPT)
model_engine = "text-davinci-002"

# Definir la función de conversación
def talk_to_chatgpt(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text
    return message.strip()

# Comenzar la conversación
while True:
    user_input = input("Ariel: ")
    prompt = user_input
    message = talk_to_chatgpt(prompt)
    print("chatGPT: " + message)
