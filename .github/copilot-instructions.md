# GitHub Copilot / AI agent instructions for tibo-telegram-bot ✅

Purpose: short, actionable notes so an AI coding agent can be productive immediately with this repository.

## Quick architecture overview 🔧

- Single Python service: `telegram.py` — a Flask app that receives Telegram webhook updates and also contains legacy polling handlers. The file mixes two Telegram frameworks:
  - pyTelegramBotAPI (telebot) — most command handlers use `@bot.message_handler` and are synchronous
  - aiogram — used with an async `Dispatcher` (`dp`) for example handlers; middleware `BapMiddleware` is applied
- Deployment targets: Render / generic WSGI via `gunicorn telegram:app` (see `Procfile`) or run locally with Flask/Flask-Script (`manage.py`).
- Integrations:
  - TeleAds (`teleads`) — used for advertisement middleware and calls
  - Render API — used by `/restart` and `/status` endpoints (requires `RENDER_SERVICE_ID` / `RENDER_API_KEY`)
  - External APIs: OpenWeatherMap (token currently hard-coded in `telegram.py`), imgflip (memes), and others via `requests`

## Important files (source of truth) 📁

- `telegram.py` — main application, handlers, Flask endpoints, webhook logic
- `manage.py` — Flask-Script wrapper for `app` (local dev / Heroku use)
- `Procfile` — production command (`web: gunicorn telegram:app`)
- `requirements.txt` / `pyproject.toml` — dependencies and (odd) Python constraint: `>=3.13,<3.15`
- `README.md` — project overview and links

## Environment & runtime specifics (required to run) ⚠️

- Required environment variables (read at runtime):
  - `TIBO_TELEGRAM_BOT_TOKEN` (required) — used to run the webhook endpoint and encoded into route `/<TOKEN>`
  - `RENDER_SERVICE_ID` and `RENDER_API_KEY` — used by `/restart` and `/status` endpoints
  - `TELEADS_API_KEY` (optional, fallback to "meteoritt") — used by TeleAds middleware
  - `PORT` (optional) — server port (defaults to `8443` in the code)
- Local dev note: If the environment variable `IDE` is present, the app starts polling mode (`bot.polling`) instead of webhook Flask behavior. To run locally with polling: `IDE=1 python telegram.py`.

## Run & debug commands (examples) ▶️

- Install deps (pip): `pip install -r requirements.txt` (or use Poetry via `pyproject.toml`)
- Run locally (Flask server / webhook mode): `python telegram.py` or `python manage.py runserver`
- Run locally (polling for development/testing): `IDE=1 python telegram.py` (this sets polling instead of webhook)
- Run in production (WSGI): `gunicorn telegram:app` (Procfile uses this)
- Useful endpoints (when running):
  - `GET /` — sets webhook to `https://tibo-telegram-bot.onrender.com/<TIBO_TELEGRAM_BOT_TOKEN>` (helper during deploy)
  - `GET /health` — returns `OK`
  - `GET /debug` — returns basic bot state (webhook info, known users count)
  - `GET|POST /restart` — attempts to restart Render service using `RENDER_API_KEY`

## Patterns & conventions to follow when editing code ✅

- New bot commands (sync): use telebot decorators: `@bot.message_handler(commands=['mycmd'])` and accept a `telebot.types.Message` argument.
- New async handlers: use aiogram `@dp.message()` / filters and async functions. Both frameworks are present; pick the one that fits the handler semantics (use `telebot` for simpler sync handlers, `aiogram` for async workflows).
- Error handling: code typically wraps handlers in `try/except` and prints tracebacks. Follow existing style (print/traceback) for small fixes; for larger changes, prefer structured logging.
- Avoid sending test messages to the production user id hard-coded in the repo: `41365750` (used in `before_first_request` and other startup helpers).
- Webhook route: the incoming update POST path is `/<TIBO_TELEGRAM_BOT_TOKEN>` (defined in `telegram.py`). Ensure tests or local endpoints post to that route.

## Quick implementation examples ✍️

- Add a synchronous command:

```python
@bot.message_handler(commands=['echo'])
def cmd_echo(message):
    bot.send_message(message.chat.id, 'Echo: ' + message.text)
```

- Add an async aiogram handler:

```python
@dp.message()
async def handle_all(message: Message):
    await message.answer('Got it')
```

## Testing & automation notes 🧪

- There is currently no test suite in this repository. Good first targets for unit tests: small pure functions in `telegram.py` such as `weather_get` and `listToString`.
- When writing tests that exercise webhook handling, POST JSON must use the route `/<TIBO_TELEGRAM_BOT_TOKEN>` or call `bot.process_new_updates([update])` directly.

## Deployment & operational gotchas ⚠️

- `OPEN_WAETHER_MAP_TOKEN` is currently hard-coded inside `telegram.py`. Replace it with an env var if you add tests or change behavior.
- The code expects Render-style deployment. The `/restart` endpoint calls Render's REST API. Do not run restart in tests; stub HTTP calls.
- Python version pinning in `pyproject.toml` is unusual (>=3.13). Validate CI and runtime environments support the specified Python version before changing it.

## What an AI agent should do first (priority list) 📋

1. Read `telegram.py` fully — it's the main source of truth for behavior and endpoints. 🔎
2. Confirm required env vars and where they are used. 🔐
3. Run the app locally in `IDE=1` (polling mode) to verify basic command handlers without needing a public webhook. ✅
4. Create focused unit tests for small pure functions (e.g., `weather_get`) and for webhook processing by calling `bot.process_new_updates` directly (no real Telegram needed).

---

If any part is unclear or you want the instructions to include more detail (examples of tests, preferred linting rules, or a recommended Dockerfile), tell me which section to expand and I will update this file. 🔁
