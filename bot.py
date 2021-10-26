from dis_snek.client import Snake
from dis_snek.models.enums import Intents
from dis_snek.models.listener import listen
from os import getenv
from dotenv import load_dotenv

load_dotenv()

bot = Snake(intents=Intents.DEFAULT)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine


@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@listen()
async def on_message_create(event):
    # This event is called when a message is sent in a channel the bot can see
    print(f"message received: {event.message.content}")


bot.start(getenv("TOKEN"))
