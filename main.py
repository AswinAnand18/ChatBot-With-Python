from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train("chatterbot.corpus.english")

# Chat with the bot
while True:
    user_input = input("You: ")

    # Get a response from the chatbot
    bot_response = chatbot.get_response(user_input)

    print("Bot: ", bot_response)
