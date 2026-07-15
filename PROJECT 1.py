print("=" * 50)
print("      Welcome to the Rule-Based Chatbot")
print("Type 'exit' or 'bye' anytime to end the chat.")
print("=" * 50)
while True:
    user = input("\nYou: ").lower()
    if user == "exit" or user == "bye" or user == "quit":
        print("ChatBot: Goodbye! Have a wonderful day.")
        break
    elif user == "hi" or user == "hello" or user == "hey":
        print("ChatBot: Hello! Nice to meet you.")
    elif user == "what is your name":
        print("ChatBot: My name is SmartBot. I am a simple rule-based chatbot.")
    elif user == "how are you":
        print("ChatBot: I'm doing great! Thanks for asking. How can I help you?")
    elif user == "what can you do":
        print("ChatBot: I can answer simple questions using predefined rules.")
    elif user == "which university are you from":
        print("ChatBot: I am not from a university. I am a Python chatbot.")
    elif user == "what is python":
        print("ChatBot: Python is a popular programming language used for AI, web development, automation, and data science.")
    elif user == "what is ai":
        print("ChatBot: AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.")
    elif user == "what is robotics":
        print("ChatBot: Robotics is the field of designing, building, and programming robots.")
    elif user == "thank you" or user == "thanks":
        print("ChatBot: You're welcome! Happy to help.")
    elif user == "help":
        print("ChatBot: You can ask me questions like:")
        print("- What is AI?")
        print("- What is Python?")
        print("- What is Robotics?")
        print("- How are you?")
        print("- What can you do?")
        print("- What is your name?")
    elif user == "what is your favorite color":
        print("ChatBot: I like blue because it reminds me of technology.")
    elif user == "who created you":
        print("ChatBot: I was created using Python programming with rule-based logic.")
    else:
        print("ChatBot: Sorry, I don't understand that. Type 'help' to see what you can ask.")
print("Chat ended successfully.")
