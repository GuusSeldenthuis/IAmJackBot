import time
from jackbot import bot, handle_message

response = bot.getUpdates()
print(response)
print('I am listening...')

while 1:
    time.sleep(10)
    response = bot.getUpdates()