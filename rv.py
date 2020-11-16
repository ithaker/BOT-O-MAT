from flask import Flask
from flask_ask import Ask, statement, question, session
import random

app = Flask(__name__)
ask = Ask(app, "/bot-o-mat")

def get_name(): #i don't know if i need this. Gets name from AMAZON.US_FIRST_NAME and saves it
    pass

def get_chores():
    chore_list = {
        "do the dishes": 1000,
        "sweep the house": 3000,
        "do the laundry": 10000,
        "take out the recycling": 4000,
        "make a sammich": 7000,
        "mow the lawn": 20000,
        "rake the leaves": 18000,
        "give the dog a bath": 14500,
        "bake some cookies": 8000,
        "wash the car": 20000
        }
    sampled_list = random.sample(chore_list.items(), 5)
    return sampled_list

@app.route('/bot-o-mat')
def homepage():
    return "Hi there, welcome to the Bot-o-Mat!"

@ask.launch
def start_skill():
    welcome_message = 'Hello there and welcome to Bot-o-Mat version alpha. Would you like to get started?'
    return question(welcome_message)

@ask.intent("YesIntent")
def get_started():
    start_message = 'Great! What would you like to name your robot?'
    return question(start_message)

@ask.intent("NameIntent")
def share_name():
    name = get_name()
    name_msg = 'Congratulations! Your robot is named {}'.format(name) + "What kind of robot is it?"
    return question(name_msg)

@ask.intent("YesIntent")
def share_chores():
    chores = get_chores()
    chores_msg = 'All set! The remaining chores are {}'.format(chores)
    return statement(chores_msg)
    
@ask.intent("NoIntent")
def no_intent():
    bye_text = 'This was an absolute waste of time. Please come back with a better mindset.'
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=False)
