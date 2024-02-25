import random
patterns_responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "name": ["My name is ChatBot.", "You can call me ChatBot.", "I'm ChatBot."],
    "age": ["I'm just a computer program, so I don't have an age.", "Age is just a number for me."],
    "weather": ["The weather is sunny today.", "It's raining outside.", "I'm not sure, you should check a weather website."],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."]
}
def generate_response(user_input):
    for pattern, responses in patterns_responses.items():
        if pattern in user_input.lower():
            return random.choice(responses)
    return random.choice(patterns_responses["default"])
def main():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Big Chatbot: Goodbye! Thanks for chatting.")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
