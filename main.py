from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# nltk.download()

import streamlit as st

chatbot = ChatBot("Panther")  # change the name of the chatbot by changing the parem
trainer = ListTrainer(chatbot)
trainer.train([
    "Hello", "hey", "whats up", "Hi, my name is " + chatbot.name,

])

response = ''
while response.lower().strip() != "exit":
    try:
        usr_input = input("Type your Message: ")
        response = str(chatbot.get_response(usr_input))
        print(str(chatbot.name) + ": " + str(response))
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
