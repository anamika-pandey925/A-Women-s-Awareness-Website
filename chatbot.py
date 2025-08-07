import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created to assist you. What's your name?", "I'm ChatBot! What's yours?"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I help you today?", "Hi %1! What can I do for you?"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm here to help! How are you?", "I'm good! How can I assist you?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you soon! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Can you elaborate?", "Interesting... Could you tell me more?"]
    ]
]

# Main function to initiate chatbot
def chatbot():
    print("Hi, I'm ChatBot! Type 'quit' to exit.")
    chatbot_instance = Chat(pairs, reflections)
    chatbot_instance.converse()

if __name__ == "__main__":
    chatbot()
