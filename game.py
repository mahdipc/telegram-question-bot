
import random
from dataclasses import dataclass
from typing import Optional

@dataclass
class GameState:
    target_number: int
    attempts: int = 0

class NumberGame:
    def __init__(self, min_number: int, max_number: int):
        self.min_number = min_number
        self.max_number = max_number
        self.games = {}  # chat_id -> GameState

    def start_new_game(self, chat_id: int) -> int:
        """Start a new game for the given chat and return the target number."""
        target = random.randint(self.min_number, self.max_number)
        self.games[chat_id] = GameState(target_number=target)
        return target

    def guess(self, chat_id: int, number: int) -> tuple[bool, str]:
        """Process a guess and return (is_correct, message)."""
        if chat_id not in self.games:
            return False, "No active game! Start a new game first with /start"

        game_state = self.games[chat_id]
        game_state.attempts += 1

        if number == game_state.target_number:
            message = f"🎉 Correct! You got it in {game_state.attempts} attempts!"
            del self.games[chat_id]  # End the game
            return True, message
        elif number < game_state.target_number:
            return False, "Higher! Try again 👆"
        else:
            return False, "Lower! Try again 👇"

    def end_game(self, chat_id: int) -> Optional[int]:
        """End the current game and return the target number if there was one."""
        if chat_id in self.games:
            target = self.games[chat_id].target_number
            del self.games[chat_id]
            return target
        return None