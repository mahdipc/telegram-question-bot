
from telebot.handler_backends import State, StatesGroup

class GameStates(StatesGroup):
    waiting_for_number = State()
