def chatbot():

    # Greet the user
    print("Hello! I am a simple chatbot. You can ask me a few things.")
    print("Try asking 'what is your name?', 'how are you?', or about the 'weather'.")
    print("Type 'bye' to exit the chat.")

    # Start an infinite loop to keep the conversation going
    while True:
        # Get user input and convert it to lowercase for easier matching
        user_input = input("You: ").lower().strip()

        # Check if the user wants to end the chat
        if user_input == "bye" or user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break  # Exit the loop and end the program

        # --- Rule-based responses using if-elif-else ---
        
        # Respond to greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")

        # Respond to "how are you?"
        elif "how are you" in user_input:
            print("Chatbot: I'm a program, so I'm always running perfectly! Thanks for asking.")

        # Respond to questions about its name
        elif "what is your name" in user_input or "who are you" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot created with Python.")

        # Respond to questions about the weather
        elif "weather" in user_input:
            print("Chatbot: I can't check the real weather, but I hope it's nice where you are!")
            
        # Respond to a thank you
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")

        # The 'else' block handles any input that isn't recognized
        else:
            print("Chatbot: I'm sorry, I don't understand that. Please try asking something else.")

# The following line ensures the chatbot() function is called only when the script is executed directly
if __name__ == "__main__":
    chatbot()
