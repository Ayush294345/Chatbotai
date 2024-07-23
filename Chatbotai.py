def simple_chatbot(user_input):
    # Predefined rules and responses
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm good, thank you!",
        "what's your name?": "I'm a chatbot. You can call me ChatGPT.",
        "bye": "Goodbye! Have a great day!"
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if user input matches any predefined rule
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand that."

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = simple_chatbot(user_input)
        print("Chatbot:", response)
