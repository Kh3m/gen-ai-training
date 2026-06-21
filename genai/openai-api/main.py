from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  # reads .env into os.environ

groq_api_key = os.environ.get("GROQ_API_KEY")

client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
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
        model="llama-3.3-70b-versatile",
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



# import os
# from openai import OpenAI

# client = OpenAI(
#     api_key=os.environ["GROQ_API_KEY"],
#     base_url="https://api.groq.com/openai/v1"
# )

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {"role": "user", "content": "Write a short bedtime story about a unicorn."}
#     ]
# )

# print(response.choices[0].message.content)