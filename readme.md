# Telegram Number Guessing Bot

A Python-based Telegram bot that implements a number guessing game with a clean, object-oriented architecture.

## Features

- 🎮 Number guessing game with customizable range
- 📊 Attempt tracking for each game
- 👥 Multi-chat support (different games per chat)
- 🏗️ Clean, modular architecture
- 💬 Helpful feedback messages
- 🎯 Game state management

## Project Structure

```
telegram-guess-bot/
├── config.py      # Configuration settings
├── game.py        # Game logic and state management
├── bot.py         # Main bot implementation
└── README.md      # Documentation
```

## Prerequisites

- Python 3.7 or higher
- python-telegram-bot library (version 20.0 or higher)
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd telegram-guess-bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure the bot:
   - Get a bot token from [@BotFather](https://t.me/botfather)
   - Open `config.py` and replace the empty TOKEN with your actual token

## Usage

1. Start the bot:
```bash
python bot.py
```

2. In Telegram, interact with the bot using these commands:
   - `/start` - Start a new game
   - `/end` - End current game
   - `/help` - Show available commands and instructions

## Game Rules

1. The bot generates a random number between MIN_NUMBER and MAX_NUMBER (default: 1-100)
2. Players try to guess the number
3. After each guess, the bot provides feedback:
   - "Higher!" if the guess is below the target
   - "Lower!" if the guess is above the target
   - "Correct!" when the right number is guessed, along with the number of attempts

## Class Structure

- **Config**: Configuration settings (bot token, number range)
- **GameState**: Data class for tracking game state
- **NumberGame**: Core game logic and state management
- **Bot Handlers**: Command and message handlers for Telegram interaction

## Customization

### Modifying Number Range
To change the valid number range, update `MIN_NUMBER` and `MAX_NUMBER` in `config.py`:

```python
class Config:
    TOKEN = ''  # Your bot token here
    MIN_NUMBER = 1    # Change this value
    MAX_NUMBER = 100  # Change this value
```

### Adding New Commands
1. Create a new handler function in `bot.py`:
```python
async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Command implementation
    pass
```

2. Register the handler in the main() function:
```python
application.add_handler(CommandHandler("newcommand", new_command))
```

## Error Handling

The bot includes comprehensive error handling:
- Validates number input range
- Manages game state appropriately
- Handles invalid inputs gracefully
- Provides clear error messages

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Acknowledgments

MahDi Molavi  - [@mahdipc](https://github.com/mahdipc)

Project Link: [https://github.com/mahdipc/telegram-question-bot](https://github.com/mahdipc/telegram-question-bot)
