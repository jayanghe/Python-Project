from wxpy import *
import winsound
import sys
import os

bot = Bot()
tuling = Tuling(api_key='f0b70cd7021b43efa33b3de2afa11747') 
my_friend = bot.mps().search("同程旅游网")[0]
print(my_friend)

@bot.register(my_friend)
def reply_my_friend(msg):
	tuling.do_reply(msg)
	f=open('C:/Users/JYH/Desktop/test.txt','a')
	print(msg.text, msg.sender,file = f, flush = True)
	print(tuling.reply_text(msg),file = f, flush = True)
	winsound.MessageBeep(winsound.MB_ICONHAND)
	
bot.join()