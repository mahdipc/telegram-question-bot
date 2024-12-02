from bot import end, handle_guess, help_command, start
from config import Config
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(Config.TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("end", end))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
