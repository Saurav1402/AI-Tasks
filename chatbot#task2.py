def simple_chatbot(user_input):
    
    user_input = user_input.lower()

    
    rules = {
        "hi": "Hello!",
        "how are you": "I'm good, thank you!",
        "what is your name": "I'm a simple chatbot.",
        "bye": "Goodbye! Take care.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what's the weather like today": "I'm sorry, I cannot provide real-time weather information.",
        "who created you": "I was created by SAURAV.",
        "what can you do": "I can respond to certain predefined questions and engage in simple conversation.",
        "what's your favorite color": "I don't have a favorite color, I'm just a simple chatbot.",
        "how old are you": "I don't have an age, I'm just a computer program.",
        "do you dream": "No, I don't have the ability to dream. I'm just a chatbot.",
        "what is the meaning of life": "The meaning of life is a philosophical question that I'm not equipped to answer."

    }

    
    for rule, response in rules.items():
        if rule in user_input:
            return response
    
    
    return "I'm sorry, I don't understand that."


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Bot:", response)