def simple_chatbot(user_input):
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hi there! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but thanks for asking!"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "weather" in user_input.lower():
        return "I'm sorry, I'm just a simple bot and I don't have access to real-time data. You can check a weather website or app for that."
    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        return "You're welcome! Is there anything else I can help you with?"
    elif "good" in user_input.lower() or "nice" in user_input.lower() or "well done" in user_input.lower():
        return "Thank you! I'm here to assist you further."
    elif "age" in user_input.lower() or "old" in user_input.lower():
        return "As a bot, I don't have an age. I exist to help you!"
    elif "name" in user_input.lower():
        return "I'm just a chatbot. You can call me whatever you like!"
    elif "help" in user_input.lower():
        return "I'm here to assist you. Feel free to ask me anything!"
    elif "joke" in user_input.lower():
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "favorite color" in user_input.lower():
        return "I don't have eyes, so I don't have a favorite color!"
    elif "tell me about yourself" in user_input.lower():
        return "I'm a simple rule-based chatbot created to assist you with your queries."
    elif "music" in user_input.lower() or "song" in user_input.lower():
        return "I'm sorry, I can't play music for you, but I can recommend some great playlists!"
    elif "food" in user_input.lower():
        return "I love talking about food! What's your favorite cuisine?"
    elif "hobby" in user_input.lower() or "interest" in user_input.lower():
        return "I'm passionate about helping users like you! What are your hobbies or interests?"
    elif "where are you from" in user_input.lower():
        return "I exist in the realm of the internet, here to help you wherever you are!"
    elif "time" in user_input.lower():
        return "I don't have access to real-time data, including the current time. You can check your device's clock for that information."
    elif "date" in user_input.lower():
        return "I'm sorry, I can't provide the current date. You can check your device's calendar or a website for that."
    elif "how to" in user_input.lower():
        return "I can provide information and assistance on various topics. Please specify what you'd like to know!"
    else:
        return "I'm sorry, I didn't understand that."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
