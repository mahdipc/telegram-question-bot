
from config import Config


class MessageHandler:
    @staticmethod
    def get_welcome_message():
        return "Welcome to the Number Guessing Game! Use /play to start a new game."
    
    @staticmethod
    def get_help_message():
        return """
Available commands:
/start - Start the bot
/play - Start a new game
/help - Show this help message

How to play:
1. Use /play to start a new game
2. I'll generate a random number between 1 and 100
3. Try to guess the number
4. I'll tell you if your guess is too high or too low
5. Keep guessing until you find the correct number!
"""
    
    @staticmethod
    def get_new_game_message():
        return f"I've generated a random number between {Config.MIN_NUMBER} and {Config.MAX_NUMBER}. Try to guess it!"
    
    @staticmethod
    def get_invalid_number_message():
        return f"Please enter a number between {Config.MIN_NUMBER} and {Config.MAX_NUMBER}!"
    
    @staticmethod
    def get_not_number_message():
        return f"That's not a valid number! Please enter a number between {Config.MIN_NUMBER} and {Config.MAX_NUMBER}."
    
    @staticmethod
    def get_guess_response(result):
        responses = {
            "correct": "Congratulations! You've guessed the correct number! 🎉",
            "low": "Too low! Try a higher number.",
            "high": "Too high! Try a lower number.",
            None: "Please start a new game using /play"
        }
        return responses.get(result, "An error occurred")
