def chatbot_response(user_input):
    # Normalize input to lowercase
    user_input = user_input.lower()
    
    # Define rules for different types of inputs
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    elif "weather" in user_input:
        return "I cannot check real-time weather, but you can use your favorite weather app!"
    
    elif "time" in user_input or "what time" in user_input:
        return "I'm not able to check the current time, but you can check it on your device."
    
    elif "how are you" in user_input:
        return "I’m just a bot, but I’m here to help!"
    
    # Add more rules as needed
    else:
        return "I’m not sure how to respond to that. Can you try rephrasing?"

# Main chatbot loop
def start_chat():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
