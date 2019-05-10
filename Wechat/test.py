from wxpy import *

bot = Bot()

@bot.register()
def print_messages(msg):
    print(msg)

# 堵塞线程，并进入 Python 命令行
embed()