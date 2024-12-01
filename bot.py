
from config import Config
from game_manager import GameManager
import telebot
from telebot.storage import StateMemoryStorage

from message_handler import MessageHandler
from number_validator import NumberValidator
from states import GameStates

class NumberGuessingBot:
    def __init__(self):
        self.state_storage = StateMemoryStorage()
        self.bot = telebot.TeleBot(Config.TOKEN, state_storage=self.state_storage)
        self.game_manager = GameManager()
        self.message_handler = MessageHandler()
        self.number_validator = NumberValidator()
        self.setup_handlers()
    
    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            self.bot.reply_to(message, self.message_handler.get_welcome_message())
        
        @self.bot.message_handler(commands=['help'])
        def send_help(message):
            self.bot.reply_to(message, self.message_handler.get_help_message())
        
        @self.bot.message_handler(commands=['play'])
        def start_game(message):
            user_id = message.from_user.id
            self.game_manager.start_new_game(user_id)
            self.bot.set_state(user_id, GameStates.waiting_for_number, message.chat.id)
            self.bot.reply_to(message, self.message_handler.get_new_game_message())
        
        @self.bot.message_handler(state=GameStates.waiting_for_number)
        def handle_number_input(message):
            user_id = message.from_user.id
            
            # Validate input
            is_valid, number = self.number_validator.validate_number(message.text)
            if not is_valid:
                self.bot.reply_to(message, self.message_handler.get_not_number_message())
                return
            
            # Check guess
            result = self.game_manager.check_guess(user_id, number)
            response = self.message_handler.get_guess_response(result)
            self.bot.reply_to(message, response)
            
            # If correct, end game
            if result == "correct":
                self.bot.delete_state(user_id, message.chat.id)
                self.game_manager.end_game(user_id)
    
    def run(self):
        print("Bot is running...")
        self.bot.infinity_polling()