Tibo.app - Theory of inventive based offers [@meteoritt](https://github.com/meteoritt)

# tibo-telegram-bot

![visitors](https://visitor-badge.laobi.icu/badge?page_id=ruopsdev.tibo-telegram-bot)

Telegram bot @albert_ai_bot (https://t.me/albert_ai_bot)

Open Source Code (СПО): [https://github.com/ruopsdev/tibo-telegram-bot](https://github.com/ruopsdev/tibo-telegram-bot)

## Quick Start

**New to this project?** Check out the [Quick Start Guide (QUICKSTART.md)](QUICKSTART.md) to get running in 5 minutes!

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Available Commands](#available-commands)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)

## Features

- Weather information via OpenWeatherMap API
- Random meme generation
- Sentiment analysis with NLTK
- Bar notification system
- Random number generator
- Webhook and polling modes
- Flask web server with health check endpoints

## Prerequisites

- Python 3.13 or higher (3.13-3.14)
- Telegram Bot Token (get from [@BotFather](https://t.me/BotFather))
- pip or Poetry for dependency management
- (Optional) Render.com account for deployment

## Installation

### Option 1: Using pip

```bash
# Clone the repository
git clone https://github.com/ruopsdev/tibo-telegram-bot.git
cd tibo-telegram-bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using Poetry

```bash
# Clone the repository
git clone https://github.com/ruopsdev/tibo-telegram-bot.git
cd tibo-telegram-bot

# Install dependencies with Poetry
poetry install
poetry shell
```

## Configuration

### Required Environment Variables

Create a `.env` file in the project root or set these environment variables:

```bash
# Required - Get this from @BotFather on Telegram
export TIBO_TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"

# Optional - For Render.com deployment only
export RENDER_SERVICE_ID="your_render_service_id"
export RENDER_API_KEY="your_render_api_key"

# Optional - For TeleAds middleware (if using)
export TELEADS_API_KEY="your_teleads_api_key"

# Optional - Server port (default: 8443)
export PORT=8443
```

### Getting a Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the token provided by BotFather
5. Set it as `TIBO_TELEGRAM_BOT_TOKEN` environment variable

## Running the Bot

### Local Development (Polling Mode)

Polling mode is recommended for local development and testing:

```bash
# Set the IDE environment variable to enable polling mode
export IDE=1
export TIBO_TELEGRAM_BOT_TOKEN="your_token_here"

# Run the bot
python telegram.py
```

The bot will start in polling mode and listen for messages directly from Telegram.

### Production (Webhook Mode)

Webhook mode is used for production deployment on platforms like Render.com:

```bash
# Set environment variables
export TIBO_TELEGRAM_BOT_TOKEN="your_token_here"
export PORT=8443

# Run with Flask development server
python telegram.py

# OR run with Gunicorn (recommended for production)
gunicorn telegram:app --bind 0.0.0.0:8443
```

### Using Flask-Script (Alternative)

```bash
python manage.py runserver
```

## Available Commands

**📖 For complete command reference with examples, see [COMMANDS.md](COMMANDS.md)**

Once the bot is running, you can use these commands in Telegram:

### Basic Commands
- `/start` - Initialize the bot, register user, and show help
- `/check` - Same as `/start` - register and show welcome
- `/help` - Display list of available commands

### Weather Information
- `/weather [city]` - Get current weather (default city: Perm)
  - Example: `/weather Moscow`
- `/погода [город]` - Weather command in Russian

### Entertainment & Fun
- `/mem` - Get a random meme from imgflip
- `/meme` - Get a random meme (same as `/mem`)
- `/getimage` or `/image` - Get a random image from imgflip
- `/8`, `/eight`, `/восемь`, `/рандом` - Generate random number between 1-100
- `/3.14`, `/3`, `/three`, `/три`, `/pi`, `/пи` - Display the value of Pi (3.141592...)

### Social Features
- `/bar` - Notify bar members with:
  - Mention all configured bar members
  - Create a poll "DRINK BEER SAVE WATER"
  - Send random beer photo

### Sentiment Analysis (AI-powered)
All these commands trigger sentiment analysis - the bot will ask you to send text, then analyze its emotional tone and respond with an emoji and sentiment scores:

**Main command:**
- `/emotion` - Analyze sentiment of your text

**Alternative commands (all do the same):**
`/themes`, `/idea`, `/more`, `/mind`, `/context`, `/echo`, `/bet`, `/produce`, `/think`, `/note`, `/tibo`, `/agenda`, `/graph`, `/map`, `/push`, `/fact`, `/top`, `/stat`, `/game`, `/quiz`, `/test`, `/chat`, `/bio`, `/date`, `/rpg`, `/lol`, `/notify`, `/quote`, `/advice`, `/contact`, `/donate`, `/share`, `/random`, `/schedule`, `/settings`, `/new`

**Sentiment responses:**
- 😁 Very positive (>0.75)
- 😀 Positive (>0.5)
- 😊 Slightly positive (>0.25)
- 🤨 Neutral positive (>0)
- 😥 Neutral negative (>-0.25)
- 😈 Negative (>-0.5)
- 👹 Very negative (>-0.75)
- 🤬 Extremely negative (>-1)

### Other Commands
- `/promo` - Display advertisement (requires TeleAds configuration)
- `/help_auth` - Show inline bot capabilities with contact button

## Deployment

### Deploy to Render.com

1. Create account on [Render.com](https://render.com)

2. Create a new Web Service

3. Connect your GitHub repository

4. Configure the service:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn telegram:app`
   - **Environment:** Python 3.13

5. Add Environment Variables:
   - `TIBO_TELEGRAM_BOT_TOKEN`
   - `RENDER_SERVICE_ID` (found in Render dashboard)
   - `RENDER_API_KEY` (create in Render account settings)

6. Deploy the service

7. After deployment, visit `https://your-service-url.onrender.com/` to set the webhook

### Webhook Endpoints

Once deployed, these endpoints are available:

- `GET /` - Set webhook to current URL
- `POST /<TIBO_TELEGRAM_BOT_TOKEN>` - Telegram webhook endpoint
- `GET /health` - Health check (returns "OK")
- `GET /debug` - Debug information
- `GET|POST /restart` - Restart Render service
- `GET /status` - Check Render service status

## Troubleshooting

### Bot doesn't respond

1. Check if `TIBO_TELEGRAM_BOT_TOKEN` is set correctly
2. Verify webhook is set (visit `/debug` endpoint)
3. Check logs for error messages
4. Ensure all required dependencies are installed

### ImportError or ModuleNotFoundError

```bash
# Reinstall all dependencies
pip install -r requirements.txt --upgrade
```

### NLTK Data Missing

The bot will automatically download NLTK data on first run. If you encounter errors:

```python
python -c "import nltk; nltk.download('vader_lexicon')"
```

### Webhook Issues

If webhook isn't working:

```bash
# Remove existing webhook
curl https://api.telegram.org/bot<YOUR_TOKEN>/deleteWebhook

# Set new webhook
curl https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://your-domain.com/<YOUR_TOKEN>
```

### Port Already in Use

```bash
# Change the port
export PORT=8000
python telegram.py
```

## Project Structure

```
tibo-telegram-bot/
├── telegram.py          # Main bot application
├── manage.py            # Flask-Script management
├── tiz.py              # NLTK sentiment analysis examples
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Poetry configuration
├── Procfile            # Render/Heroku deployment config
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Security Notes

- Never commit your `.env` file or expose `TIBO_TELEGRAM_BOT_TOKEN`
- Keep your dependencies up to date
- Review the security audit in project issues before deploying

---

# Git-Flow методология метрологии запуска фичеветок в кластере Kubernetes: [https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------](https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------)

* [https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------](https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------) - Презентация методологии git-flow - [Презентация методологии git-flow]([https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------](https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------))
* [https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------](https://medium.com/ruopsdev/git-flow-presentation-b80643390888?source=collection_home_page----925f883655a3-----0-----------------------------------) - перевод через сайт [https://translate.google.com](https://translate.google.com)

* Автор (Author): [Sergei Chudakov](https://sergos.medium.com/) - Автор книги [Dive into Penguin](https://github.com/meteoritt/gentleman) [Сергей Чудаков](https://sergos.medium.com/) - [Погружение в Пингвина](https://github.com/meteoritt/gentleman) - Книга про работу в консоли Linux для начинающих изучать WSL, Zsh и Bash на русском: [https://github.com/meteoritt/gentleman/blob/master/README.ru-RU.md](https://github.com/meteoritt/gentleman/blob/master/README.ru-RU.md) - Для навигации в консоли оставьте пальчиками Ctrl + <- (Arrow Left), Ctrl + -> (Arrow Right), Shift + Arrow - Marker, Copy, Paste. Right Click Mouse, Middle Button Click. Double Click Left Button Mouse. USB-D.

* Tables 1 (Таблица One):

# Для Windows (win):

* Ctrl+C – копирование (copy)

* Win+V – менеджер буфера обмена

* Win+L – блокировка экрана (lock)

* Ctrl+Shift+Esc – диспетчер задач (process explorer)

* PrtScr – снимок экрана в буфер обмена (Print Screen)

* Alt+Shift+S – снимок экрана ножницами (save screen)

* Alt+PrtScr – снимок экрана или окна в OneDrive

* Alt+Tab – переключение окон (Tabula)

* Win+Tab – переключение рабочих столов

* Win+Arrow (стрелка) – тайловый менеджер окон, прилепляет окно в границам экрана

* Win+R – окно выполнить (Run)

## ScrLk клавиша рядом с PrtScr включает и отключает навигацию в Microsoft Excel по ячейкам в таблице стрелками, можно листать документ или переходить по ячейкам, в зависимости от того был включен ScrLk или нет. Scroll Lock.

# Для Linux:

## В Linux полезна утилита screen, tmux или byobu для выполнения долгих запросов, команд или бэкапов. Установка sudo apt install screen -y # (C) CSRedRat © 2026 — символ копирайта, знак авторского права, представляет собой латинскую букву C (первая буква слова «copyright») в окружности. Site: [https://yandex.ru/search/?text=copyright+symbol&lr=2&clid=1836588](https://yandex.ru/search/?text=copyright+symbol&lr=2&clid=1836588), may be later && may be before: [https://web.archive.org/web/20200105175935/http://metin2wiki.ru/wiki/FAQ_Linux#expand](https://web.archive.org/web/20200105175935/http://metin2wiki.ru/wiki/FAQ_Linux#expand)

* Ctrl+C – остановить выполнение команды

* Ctrl+X – остановить выполнение программы

* Ctrl+Z – убрать программу в фоновый режм

* Ctrl+R – рекурсивный поиск по истории команд

* Ctrl+F – forward, обратный поиск по командам

## Команда htop показывает нагрузку по компьютеру, установка sudo apt install htop -y

## Команда sudo locate <текст> ищет по всему серверу, перед этим надо выполнить команду sudo apt install mlocate -y && sudo updatedb

 

# Мой телеграм: https://t.me/ChudakovSergey или @ChudakovSergey или можно найти по номеру телефона +79638610401

# Личная почта: csredrat@gmail.com

Sign (Подпись): стерхов 你會說中文嗎？- ни хуу шуа шонгвин ма [https://burui.t.me](https://burui.t.me) (sj588 布瑞)

**ALERT**: Ищу коллег для стартапа по написанию кода платформы Joker (codename RED.L), основанной на Topalias: [https://github.com/ruopsdev/topalias](https://github.com/ruopsdev/topalias)

Я автор книги про Linux: https://github.com/meteoritt/gentleman (если надо настроить домашний компьютер на Windows с WSL – Windows Subsystem Linux под выполнение пет-проджектов, хобби, проектов)

# License

[NoBSD](https://github.com/ruopsdev/tibo-telegram-bot/wiki/NoBSD-License): [https://github.com/ruopsdev/tibo-telegram-bot/wiki/NoBSD-License](https://github.com/ruopsdev/tibo-telegram-bot/wiki/NoBSD-License)

[NoBSD License](https://github.com/ruopsdev/tibo-telegram-bot/wiki/NoBSD-License): [https://github.com/ruopsdev/tibo-telegram-bot/wiki/NoBSD-License](https://github.com/ruopsdev/tibo-telegram-bot/wiki/NoBSD-License)
