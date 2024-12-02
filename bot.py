
import logging
from telegram import Update
from telegram.ext import  ContextTypes
from config import Config
from game import NumberGame

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize the game
game = NumberGame(Config.MIN_NUMBER, Config.MAX_NUMBER)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a new game."""
    chat_id = update.effective_chat.id
    target = game.start_new_game(chat_id)
    logger.info(f"Started new game in chat {chat_id} with target {target}")
    
    await update.message.reply_text(
        f"🎮 Let's play! I'm thinking of a number between {Config.MIN_NUMBER} and {Config.MAX_NUMBER}.\n"
        "Can you guess what it is? Just send me a number!"
    )

async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle user's guess."""
    try:
        guess = int(update.message.text)
        if guess < Config.MIN_NUMBER or guess > Config.MAX_NUMBER:
            await update.message.reply_text(
                f"Please guess a number between {Config.MIN_NUMBER} and {Config.MAX_NUMBER}!"
            )
            return
    except ValueError:
        return  # Ignore non-number messages

    chat_id = update.effective_chat.id
    is_correct, message = game.guess(chat_id, guess)
    await update.message.reply_text(message)

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """End the current game."""
    chat_id = update.effective_chat.id
    target = game.end_game(chat_id)
    
    if target is not None:
        await update.message.reply_text(
            f"Game over! The number was {target}. Start a new game with /start"
        )
    else:
        await update.message.reply_text("No active game to end!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show help message."""
    help_text = (
        "🎮 Number Guessing Game Commands:\n"
        "/start - Start a new game\n"
        "/end - End the current game\n"
        "/help - Show this help message\n\n"
        f"Guess a number between {Config.MIN_NUMBER} and {Config.MAX_NUMBER} by simply sending it in the chat!"
    )
    await update.message.reply_text(help_text)
