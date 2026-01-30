# Quick Start Guide

Get your Telegram bot running in 5 minutes!

## Step 1: Create Your Telegram Bot

1. Open Telegram and find [@BotFather](https://t.me/BotFather)
2. Send: `/newbot`
3. Choose a name (e.g., "My Albert Bot")
4. Choose a username (must end in 'bot', e.g., "my_albert_bot")
5. Copy the token that BotFather gives you (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 2: Install Python Dependencies

```bash
# Make sure you have Python 3.13+
python3 --version

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your bot token
nano .env  # or use any text editor
```

In the `.env` file, replace `your_telegram_bot_token_here` with your actual token from BotFather.

## Step 4: Run the Bot

```bash
# Set environment to use polling mode (for local testing)
export IDE=1

# Load environment variables
export $(cat .env | xargs)

# Run the bot
python telegram.py
```

You should see:
```
Bot initialized with token: 123456789:...
```

## Step 5: Test Your Bot

1. Open Telegram
2. Find your bot by the username you created
3. Send `/start` to your bot
4. Try other commands like `/help`, `/weather`, `/meme`

## Common Issues

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt --upgrade
```

### "Unauthorized" Error
- Check that your token in `.env` is correct
- Make sure there are no extra spaces

### Bot doesn't respond
- Verify `IDE=1` is set (for polling mode)
- Check that `TIBO_TELEGRAM_BOT_TOKEN` is loaded: `echo $TIBO_TELEGRAM_BOT_TOKEN`
- Look for error messages in the terminal

## Next Steps

- Read the full [README.md](README.md) for deployment options
- Customize the bot commands in `telegram.py`
- Deploy to Render.com for 24/7 operation

## Available Commands

Once running, try these in Telegram:

### Essential Commands
- `/start` - Initialize bot and get welcome
- `/help` - See all commands

### Try These Fun Commands
- `/weather Moscow` - Get weather for Moscow
- `/погода Москва` - Weather in Russian
- `/meme` - Get a random meme
- `/8` - Random number (1-100)
- `/pi` - Display value of Pi
- `/emotion` - Analyze sentiment (bot will ask for text)

### Social (if configured)
- `/bar` - Notify bar members with poll

### All Sentiment Commands
These all trigger sentiment analysis (same feature):
`/emotion`, `/themes`, `/idea`, `/mind`, `/tibo`, and 30+ more aliases

**Example:**
1. Send `/emotion`
2. Bot replies: "Send your text"
3. Send: "I love this bot!"
4. Bot analyzes and responds: "😁 {'neg': 0.0, 'neu': 0.192, 'pos': 0.808, 'compound': 0.6369}"

Happy botting! 🤖
