import pip
# -*- coding: utf-8 -*-
from chatterbot import ChatBot

#creates database for chatterbot
bot = ChatBot(
    "Chris",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    #reads the input

    logic_adapters=[
        #solves math problems for basic operations
        #Example::  User: What is three plus five?  Bot: three plus five = 8
        "chatterbot.logic.MathematicalEvaluation",
        #returns the current time when requested
            #Example:: User: What time is it?   Bot: The current time is --:-- AM/PM
        "chatterbot.logic.TimeLogicAdapter"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    #reads the output
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./database.sqlite3"
)



print("Type something to begin...")
#while loop that can be exited using ctrl+C
while True:
    try:
        bot_input = bot.get_response(None)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break
