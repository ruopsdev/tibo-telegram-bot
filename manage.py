import os
from flask_script import Manager
from telegram import app, bot

manager = Manager(app)


@manager.command
def runserver():
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
    bot.send_message(41365750, 'Bot started in Heroku cloud')

if __name__ == "__main__":
    manager.run()