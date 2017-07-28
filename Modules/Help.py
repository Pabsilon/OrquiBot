def help(bot, update):
    update.message.reply_text('For now, these are the available commands:\n'
        '/Hello: Says hello to you\n'
        '/Help: Displays this message\n'
        '/Start: Says hello world\n'
        '/Status: Pings the server\n'
        '/Server: does server stuff\n\n'
        'Some of them do more things and have their own help')