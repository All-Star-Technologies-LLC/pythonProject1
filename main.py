import openai

# Set up your OpenAI API credentials
openai.api_key = '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'


def ask_chatbot(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the GPT-3 model to use
        prompt=prompt,
        max_tokens=10000,  # Adjust the response length as needed
        temperature=0.7,  # Control the randomness of the response (0.0 to 1.0)
        n=1,  # Number of responses to generate
        stop=None,  # Stop generating tokens when reaching a certain string
        timeout=15,  # Timeout (in seconds) for the API request
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return None


# Example conversation loop
print("Chatbot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")
    prompt = f"User: {user_input}\nChatbot:"

    response = ask_chatbot(prompt)

    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: Apologies, I'm currently unable to generate a response.")

