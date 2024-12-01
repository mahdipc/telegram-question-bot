# Telegram Number Guessing Bot

A Python-based Telegram bot that implements a number guessing game with a clean, object-oriented architecture.

## Features

- 🎮 Number guessing game with customizable range
- 🔢 Input validation for user guesses
- 👥 Multi-user support
- 🏗️ Clean, modular architecture
- 💬 Helpful feedback messages
- 🎯 State management for game progress

## Project Structure

```
telegram-question-bot/
├── config.py           # Configuration settings
├── states.py          # Game state definitions
├── game_manager.py    # Game logic implementation
├── message_handler.py # Message text management
├── number_validator.py# Input validation
├── bot.py            # Main bot class
├── main.py           # Entry point
└── README.md         # Documentation
```

## Prerequisites

- Python 3.7 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mahdipc/telegram-question-bot.git
cd telegram-question-bot
```

2. Install required packages:
```bash
pip install pyTelegramBotAPI
```

3. Configure the bot:
   - Get a bot token from [@BotFather](https://t.me/botfather)
   - Open `config.py` and replace `'YOUR_BOT_TOKEN'` with your actual token

## Usage

1. Start the bot:
```bash
python main.py
```

2. In Telegram, interact with the bot using these commands:
   - `/start` - Initialize the bot
   - `/play` - Start a new game
   - `/help` - Show available commands and instructions

## Game Rules

1. The bot generates a random number between 1 and 100
2. Players try to guess the number
3. After each guess, the bot provides feedback:
   - "Too high!" if the guess is above the target
   - "Too low!" if the guess is below the target
   - "Congratulations!" when the correct number is guessed

## Class Structure

- **Config**: Configuration settings and constants
- **GameStates**: Game state management using telebot states
- **GameManager**: Core game logic and user session management
- **MessageHandler**: Centralized message text management
- **NumberValidator**: Input validation and processing
- **NumberGuessingBot**: Main bot class coordinating all components

## Future Development Plans

This project is evolving from a number guessing game into a comprehensive quiz and ranking system. Here's our roadmap:

### Phase 1: Quiz System Implementation
- Replace number guessing with multiple-choice questions
- Create a question bank system
- Add different categories for questions
- Implement difficulty levels
- Add time limits for answers

### Phase 2: User Progress & Ranking
- User profile system
- Points system based on:
  - Correct answers
  - Answer speed
  - Question difficulty
- Leaderboards:
  - Global rankings
  - Category-specific rankings
  - Weekly/Monthly challenges

### Phase 3: Advanced Features
- Custom quiz creation
- Group quiz competitions
- Achievement system
- Progressive difficulty
- Performance analytics
- Learning path recommendations

### Phase 4: Social Features
- Challenge other users
- Share results
- Form study groups
- Discussion forums
- Expert verification system

### Technical Improvements
- Database integration (PostgreSQL/MongoDB)
- Caching system
- API endpoints for external integrations
- Advanced analytics
- Performance optimization

### Administrative Features
- Question management dashboard
- User management system
- Content moderation tools
- Performance monitoring
- Analytics dashboard


## Customization

### Modifying Number Range
To change the valid number range, update `MIN_NUMBER` and `MAX_NUMBER` in `config.py`:

```python
class Config:
    TOKEN = 'YOUR_BOT_TOKEN'
    MIN_NUMBER = 1    # Change this value
    MAX_NUMBER = 100  # Change this value
```

### Adding New Commands
1. Add new handler in `NumberGuessingBot` class:
```python
@self.bot.message_handler(commands=['newcommand'])
def handle_new_command(message):
    # Command implementation
```

2. Add corresponding message in `MessageHandler`

## Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes:
```bash
git commit -m 'Add some AmazingFeature'
```
4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

We welcome contributions in the following areas:
- Question bank development
- Algorithm improvements
- UI/UX enhancements
- Documentation
- Testing
- Localization

## Contact

Your Name - [@mahdipc](https://github.com/mahdipc)

Project Link: [https://github.com/mahdipc/telegram-question-bot](https://github.com/mahdipc/telegram-question-bot)

## Acknowledgments

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for the Telegram bot framework
- [Telegram Bot API](https://core.telegram.org/bots/api) documentation