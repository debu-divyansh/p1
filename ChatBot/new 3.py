# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot
# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time

# Give a name to the chatbot "corona bot"
# and assign a trainer component.
chatbot=ChatBot('corona bot')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
"chatterbot.corpus.english.conversations" )

while True:
	request = input('You: ')
	if request == 'Ok':
	  print('Bot: Good Bye!!')
	  break
	else:
	  response = chatbot.get_response(request)
	  print("Bot: ", response)
