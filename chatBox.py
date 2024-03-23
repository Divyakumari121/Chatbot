import nltk
import re
import random

# Download NLTK data if not already present
nltk.download('punkt')

# Predefined responses for different patterns
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "farewell": ["Goodbye!", "Bye!", "See you later!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm sorry, I don't understand.", "Can you please rephrase that?", "I'm not sure I follow."],
}

# Patterns to match user input
patterns = {
    "greeting": re.compile(r"hello|hi|hey|good morning|good afternoon|good evening", re.IGNORECASE),
    "farewell": re.compile(r"bye|goodbye|see you later|take care", re.IGNORECASE),
    "thanks": re.compile(r"thank you|thanks|thanks a lot", re.IGNORECASE),
}

def respond(message):
    """Generate a response to the user's message."""
    for intent, pattern in patterns.items():
        if re.search(pattern, message):
            return random.choice(responses.get(intent, responses["default"]))
    return random.choice(responses["default"])

def chat():
    """Run the chatbot."""
    print("Bot: Hi! How can I assist you today?")

    while True:
        user_input = input("You: ").strip()

        # Check for exit command
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break

        # Get response from the bot
        bot_response = respond(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    chat()
