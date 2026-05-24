print("\n🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",
    "how are you": "I am doing great!",
    "what is your name": "I am DecodeBot 🤖",
    "who created you": "I was created using Python.",
    "good morning": "Good Morning! ☀️",
    "good evening": "Good Evening! 🌙",
    "thanks": "You're welcome! 😊",
    "bye": "Goodbye! Have a nice day 👋"
}

while True:

    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    reply = responses.get(
        user_input,
        "Bot: Sorry, I don't understand that."
    )

    print("Bot:", reply)