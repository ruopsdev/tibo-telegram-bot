# Complete Command Reference

This document lists all available bot commands with detailed explanations.

## Table of Contents
- [Basic Commands](#basic-commands)
- [Weather Commands](#weather-commands)
- [Entertainment Commands](#entertainment-commands)
- [Math & Random](#math--random)
- [Social Features](#social-features)
- [Sentiment Analysis](#sentiment-analysis)
- [Other Commands](#other-commands)

---

## Basic Commands

### `/start`
**Description:** Initialize the bot and register as a user
**What it does:**
- Registers your user ID
- Sends welcome message: "Hello, stranger, let me scan you..."
- Shows help with all available commands

**Example:**
```
You: /start
Bot: Hello, stranger, let me scan you...
Bot: Scanning complete, I know you now
Bot: The following commands are available: ...
```

### `/check`
**Description:** Same as `/start` - check bot status and register
**What it does:** Identical to `/start` command

### `/help`
**Description:** Display all available commands
**What it does:** Shows a list of commands defined in the bot

**Example:**
```
You: /help
Bot: The following commands are available:
     /start - Get used to the bot
     /help - Gives you information about the available commands
     ...
```

---

## Weather Commands

### `/weather [city]`
**Description:** Get current weather information
**Default city:** Perm (if no city specified)
**API:** OpenWeatherMap

**What you get:**
- Current temperature
- Weather conditions
- Max temperature
- Min temperature (at night)

**Examples:**
```
/weather
/weather Moscow
/weather London
/weather "New York"
```

**Response format:**
```
24.5 clear sky, up to 26.0, at night 18.0
```

### `/погода [город]`
**Description:** Russian version of weather command
**Same functionality as `/weather`**

**Examples:**
```
/погода
/погода Москва
/погода Санкт-Петербург
```

---

## Entertainment Commands

### `/mem`
**Description:** Get a random meme
**Source:** imgflip.com API
**Returns:** Random meme image

### `/meme`
**Description:** Get a random meme
**Same as `/mem`**

### `/getimage` or `/image`
**Description:** Get a random image
**Source:** imgflip.com API
**Returns:** Random image from meme database

**Example:**
```
You: /meme
Bot: [Sends random meme image]
```

---

## Math & Random

### `/8`, `/eight`, `/восемь`, `/рандом`
**Description:** Generate a random number
**Range:** 1 to 100
**All variants work the same:**
- `/8` (English)
- `/eight` (English word)
- `/восемь` (Russian)
- `/рандом` (Russian - random)

**Example:**
```
You: /8
Bot: 42
Bot: 42
```
*Note: Bot sends the number twice*

### `/3.14`, `/3`, `/three`, `/три`, `/pi`, `/пи`
**Description:** Display the value of Pi
**Value:** 3.141592653589793 (Python's math.pi)

**All variants:**
- `/3.14` (numeric)
- `/3` (short)
- `/three` (English)
- `/три` (Russian - three)
- `/pi` (English)
- `/пі` (Russian)

**Example:**
```
You: /pi
Bot: 3.141592653589793
Bot: 3.141592653589793
```
*Note: Bot sends Pi value twice*

---

## Social Features

### `/bar`
**Description:** Notify bar members and create a poll
**Requires:** Pre-configured bar_members in code

**What it does:**
1. Mentions all configured bar members
2. Sends message: "@user1 @user2 GO BAR"
3. Creates a poll: "DRINK BEER SAVE WATER"
   - Options: "Drink beer", "Discord", "Play computer"
4. Sends random beer photo

**Example:**
```
You: /bar
Bot: @ChudakovSergey @elijah_here GO BAR
Bot: [Poll] DRINK BEER SAVE WATER
Bot: [Random beer photo]
```

**Pre-configured members:**
- ChudakovSergey
- elijah_here (Илья Полосков)
- James Touchet
- Pavel S
- Nikita

*Note: To add your own members, edit the `bar_members` dictionary in telegram.py*

---

## Sentiment Analysis

All these commands trigger the **same sentiment analysis feature**. The bot will:
1. Ask you to send text
2. Analyze the emotional sentiment using NLTK VADER
3. Respond with emoji and sentiment scores

### Main Command
- `/emotion`

### All Alternative Commands (37 total)
`/themes`, `/idea`, `/more`, `/mind`, `/context`, `/echo`, `/bet`, `/produce`, `/think`, `/note`, `/tibo`, `/agenda`, `/graph`, `/map`, `/push`, `/fact`, `/top`, `/stat`, `/game`, `/quiz`, `/test`, `/chat`, `/bio`, `/date`, `/rpg`, `/lol`, `/notify`, `/quote`, `/advice`, `/contact`, `/donate`, `/share`, `/random`, `/schedule`, `/settings`, `/new`

### How It Works

**Step 1 - Send command:**
```
You: /emotion
Bot: Send your text
```

**Step 2 - Send text to analyze:**
```
You: I absolutely love this amazing bot!
Bot: 😁 {'neg': 0.0, 'neu': 0.254, 'pos': 0.746, 'compound': 0.8658}
```

### Sentiment Response Table

| Emoji | Sentiment | Compound Score |
|-------|-----------|----------------|
| 😁 | Very positive | > 0.75 |
| 😀 | Positive | > 0.5 |
| 😊 | Slightly positive | > 0.25 |
| 🤨 | Neutral positive | > 0 |
| 😥 | Neutral negative | > -0.25 |
| 😈 | Negative | > -0.5 |
| 👹 | Very negative | > -0.75 |
| 🤬 | Extremely negative | > -1 |
| 🙄 | Other | ≤ -1 |

### Sentiment Scores Explained

The response includes 4 scores:
- **neg:** Negative score (0.0 to 1.0)
- **neu:** Neutral score (0.0 to 1.0)
- **pos:** Positive score (0.0 to 1.0)
- **compound:** Overall sentiment (-1.0 to 1.0)
  - -1.0 = most negative
  - 0.0 = neutral
  - +1.0 = most positive

**Examples:**

```
Text: "This is terrible and awful"
Response: 👹 {'neg': 0.629, 'neu': 0.371, 'pos': 0.0, 'compound': -0.7351}

Text: "This is okay"
Response: 🤨 {'neg': 0.0, 'neu': 0.536, 'pos': 0.464, 'compound': 0.2023}

Text: "I'm so happy and excited!"
Response: 😁 {'neg': 0.0, 'neu': 0.334, 'pos': 0.666, 'compound': 0.7184}
```

---

## Other Commands

### `/promo`
**Description:** Display advertisement
**Requires:** TeleAds package and configuration
**Status:** May not work if TeleAds is not installed

**What it does:**
- Attempts to call TeleAds advertisement API
- Sends promotional content (if configured)
- Responds: "Promo processed (ad request sent)"

**Note:** This feature requires:
- TeleAds package installed
- `TELEADS_API_KEY` environment variable set

### `/help_auth`
**Description:** Show inline bot help
**What it does:**
- Displays message: "The bot supports inline. Type @<botusername> in any chat"
- Shows button: "Message the developer" (links to @ChudakovSergey)

**Use case:** Contact bot developer for support

---

## Command Categories Summary

| Category | Command Count | Examples |
|----------|---------------|----------|
| Basic | 3 | /start, /check, /help |
| Weather | 2 | /weather, /погода |
| Entertainment | 3 | /mem, /meme, /getimage |
| Math/Random | 8 | /8, /pi, /рандом, /три |
| Social | 1 | /bar |
| Sentiment | 38 | /emotion, /themes, /idea... |
| Other | 2 | /promo, /help_auth |
| **Total** | **57** | |

---

## Tips

1. **Weather:** Works best with single-word city names. For multi-word cities, the command might not parse correctly without quotes.

2. **Sentiment Analysis:** Works with any language but optimized for English (uses VADER lexicon).

3. **Russian Commands:** Several commands have Russian variants (погода, восемь, рандом, три, пі).

4. **Memes:** Powered by imgflip.com public API - no authentication needed.

5. **Bar Command:** To customize members, edit the `bar_members` dictionary in telegram.py:133-154.

---

## Not Implemented Yet

The `commands` dictionary in telegram.py (line 97) only lists 7 commands, but 57 total commands are implemented. The help text doesn't show all commands automatically.

**Commands shown in /help:**
- start
- help
- getimage
- weather
- погода
- bar
- mem
- meme
- emotion

**Commands NOT shown in /help (but still work):**
- check
- promo
- help_auth
- All the math/random commands (/8, /pi, etc.)
- All the sentiment analysis aliases (37 commands)

To see all commands, refer to this document or check the source code in `telegram.py`.
