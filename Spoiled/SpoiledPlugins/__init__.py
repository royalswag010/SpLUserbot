import time
from config import STUFF
from Spoiled.Utils import *

hl = STUFF.COMMAND_HANDLER

startTime = time.time()

COMMANDS_HELP = {}

def add_command(command, help):
    global COMMANDS_HELP
    COMMANDS_HELP[command] = help
