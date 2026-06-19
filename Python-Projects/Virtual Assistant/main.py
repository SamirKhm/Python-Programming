from openai import OpenAI

key = "YOUR_API_KEY"

client = OpenAI(api_key=key)

messages = []

def completion(message):
    global messages

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    user_question = input("Hi, I am Jarvis. How can I help you? ")
    completion(user_question)