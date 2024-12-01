
from config import Config


class NumberValidator:
    @staticmethod
    def validate_number(number_str):
        """Validate if the input is a valid number within range"""
        try:
            number = int(number_str)
            if Config.MIN_NUMBER <= number <= Config.MAX_NUMBER:
                return True, number
            return False, None
        except ValueError:
            return False, None
