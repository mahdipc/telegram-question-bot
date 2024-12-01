
import random

from config import Config

class GameManager:
    def __init__(self):
        self.user_numbers = {}
    
    def start_new_game(self, user_id):
        """Generate a new random number for a user"""
        self.user_numbers[user_id] = random.randint(Config.MIN_NUMBER, Config.MAX_NUMBER)
    
    def get_number(self, user_id):
        """Get the random number for a user"""
        return self.user_numbers.get(user_id)
    
    def end_game(self, user_id):
        """End the game for a user"""
        if user_id in self.user_numbers:
            del self.user_numbers[user_id]
    
    def check_guess(self, user_id, guess):
        """Check if the guess is correct and return appropriate message"""
        correct_number = self.get_number(user_id)
        
        if correct_number is None:
            return None
        
        if guess == correct_number:
            return "correct"
        elif guess < correct_number:
            return "low"
        else:
            return "high"