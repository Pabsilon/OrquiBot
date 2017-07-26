
def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))