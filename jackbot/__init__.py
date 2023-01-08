import random

import telepot

import jackbot.database as db

VERSION = '0.3.0    '
TOKEN = None

# Message creation
def make_start_response():
    return 'Run /help for commands and info.'


def make_help_response():
    return ('@IAmJackBot {} is created by @Panacea & @Infergo.'
            '\n/commands for all IAmJackBOT\'s commands'
            .format(VERSION))


def make_quote_response():
    r = random.randint(0, db.get_amount_of_quotes())
    return db.get_random_quote(r)


def make_jacks_response():
    return ('I am Jack\'s {} lines of bullshit.'
            .format(db.get_amount_of_quotes()))


def make_commands_response():
    return ('/help \t Displays info & version.\n'
            '/quote \t Spits out a random \'I am Jack\' quote.\n'
            '/jacks \t Shows the amount of available quotes.\n'
            '/commands \t You know what this does.'
            )


def make_unknown_response():
    return 'I am jack\'s unknown command.'


# Message handling
def handle_message(message):
    print(message['text'])
    chat_id = message['chat']['id']
    command = message['text']

    if command_is_start(command):
        response_message = make_start_response()

    elif command_is_help(command):
        response_message = make_help_response()

    elif command_is_quote(command):
        response_message = make_quote_response()

    elif command_is_jacks(command):
        response_message = make_jacks_response()

    elif command_is_commands(command):
        response_message = make_commands_response()

    try:
        bot.sendMessage(chat_id, response_message)
    except Exception as e:
        return


# Bot setup
try:  # pragma ignore
    with open('token', 'r') as token_file:
        TOKEN = token_file.read().splitlines()[0]
except FileNotFoundError:  # pragma ignore
    print('No token file found, exiting')
    exit(0)

bot = telepot.Bot(TOKEN)
