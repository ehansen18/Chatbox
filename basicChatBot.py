from chatterbot import ChatBot

chatbot = ChatBot(
    'Chris',
    trainer='chatterbot.trainers.ListTrainer'
)

chatbot.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

response = chatbot.get_response('I would like to book a flight.')
print(response)