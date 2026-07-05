from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  # reads .env into os.environ

groq_api_key = os.environ.get("GROQ_API_KEY")
groq_base_url = os.environ.get("GROQ_BASE_URL")
groq_model = os.environ.get("GROQ_MODEL")

client = OpenAI(
    api_key=groq_api_key,
    base_url=groq_base_url
)

history = []

while True:
    input_data = input("Enter your prompt: ")

    history.append({
        "role": "user",
        "content": input_data
    })
    
    if input_data == "":
        print("\n===== END OF PROGRAM =====\n")
        break

    response = client.responses.create(
        model=groq_model,
        instructions="You are an helpful assistant.",
        input = history,
        # input=input_data
    )

    output_data = response.output_text

    history.append({
        "role": "assistant",
        "content": output_data
    })

    print("="*10)
    print(output_data)
    print("="*10)