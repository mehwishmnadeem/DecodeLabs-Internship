from tkinter import *
def chatbot_response():
    user = entry.get().lower().strip()

    if user == "":
        return

    chat.insert(END, "You: " + user + "\n")

    if user in ["hi", "hello", "hey"]:
        bot = "Hello! Welcome. How can I help you today?"

    elif user == "what is your name":
        bot = "My name is SmartBot. I am a Rule-Based Chatbot."

    elif user == "how are you":
        bot = "I'm doing great! Thanks for asking."

    elif user == "what can you do":
        bot = ("I can answer simple predefined questions about AI, "
               "Python, Robotics, and programming.")

    elif user == "what is ai":
        bot = ("AI stands for Artificial Intelligence. "
               "It enables machines to perform tasks that "
               "normally require human intelligence.")

    elif user == "what is machine learning":
        bot = ("Machine Learning is a branch of AI where computers "
               "learn patterns from data.")

    elif user == "what is python":
        bot = ("Python is a popular programming language used in "
               "AI, Machine Learning, Web Development, and Automation.")

    elif user == "what is robotics":
        bot = ("Robotics is the field of designing, building, "
               "and programming intelligent robots.")

    elif user == "help":
        bot = ("You can ask me:\n"
               "- What is AI?\n"
               "- What is Python?\n"
               "- What is Robotics?\n"
               "- What is Machine Learning?\n"
               "- How are you?\n"
               "- What can you do?\n"
               "- What is your name?")

    elif user in ["thanks", "thank you"]:
        bot = "You're welcome! Happy to help."

    elif user in ["bye", "exit", "quit"]:
        bot = "Goodbye! Have a great day."
        chat.insert(END, "Bot: " + bot + "\n\n")
        root.after(1000, root.destroy)
        return

    else:
        bot = "Sorry, I don't understand that. Type 'help' to see available commands."

    chat.insert(END, "Bot: " + bot + "\n\n")
    chat.see(END)
    entry.delete(0, END)

root = Tk()
root.title("Rule-Based Chatbot")
root.geometry("700x550")
root.configure(bg="#E8F0FE")

title = Label(root,
              text="🤖 Rule-Based Chatbot",
              font=("Arial", 20, "bold"),
              bg="#1E3A8A",
              fg="white",
              pady=10)
title.pack(fill=X)

chat = Text(root,
            width=80,
            height=22,
            font=("Arial", 11),
            bg="white",
            fg="black")
chat.pack(padx=10, pady=10)

chat.insert(END,
            "Bot: Hello! Welcome to the Rule-Based Chatbot.\n"
            "Bot: Type 'help' to see available commands.\n\n")

frame = Frame(root, bg="#E8F0FE")
frame.pack(pady=10)

entry = Entry(frame,
              width=50,
              font=("Arial", 12))
entry.grid(row=0, column=0, padx=5)

send = Button(frame,
              text="Send",
              font=("Arial", 11, "bold"),
              bg="#2563EB",
              fg="white",
              width=12,
              command=chatbot_response)
send.grid(row=0, column=1, padx=5)

clear = Button(frame,
               text="Clear Chat",
               font=("Arial", 11, "bold"),
               bg="#DC2626",
               fg="white",
               width=12,
               command=lambda: chat.delete(1.0, END))
clear.grid(row=0, column=2, padx=5)

entry.bind("<Return>", lambda event: chatbot_response())

root.mainloop()
