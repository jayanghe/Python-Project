# wechat autoreply
from wxpy import *
import os
import time
# 扫码登陆
bot = Bot()
# 初始化图灵机器人 (API key 申请: http://tuling123.com)
 
# tuling = Tuling(api_key='a05e064837ec40df929370b69c8397ac')
# 联系人
my_friend = bot.chats()
# for x in my_friend:
	# print(x)
# 自动回复所有文字消息
# @bot.register(msg_types=TEXT)
# def auto_reply_all(msg):
    # tuling.do_reply(msg)
 
@bot.register(my_friend)
def reply_my_friend(msg):
    # tuling.do_reply(msg)
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	print(msg)
    # print(tuling.reply_text(msg))

# 开始运行
embed()
# bot.join()
