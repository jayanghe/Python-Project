# wechat autoreply
from wxpy import * 
import os
import random
# 扫码登陆
bot = Bot()
# 初始化图灵机器人 (API key 申请: http://tuling123.com)
my_friend= bot.chats()
a=0
for x in my_friend:
	a+=1
	print(a)
	print(x)
print("查找完成")
# tuling = Tuling(api_key='a05e064837ec40df929370b69c8397ac')
 
# 自动回复所有文字消息
# @bot.register(msg_types=TEXT)
# def auto_reply_all(msg):
    # tuling.do_reply(msg)
	# print(msg.text, msg.sender)
    # print(tuling.reply_text(msg))
# 开始运行


j=[]
j.append("我一直想跟别人分享他的故事，但始终未果，说不上为什么，也许是这个世界太像大人太成熟。 I've always wanted to share his story, but always failed, can't say why, may be the world too much like mature adults too.")
j.append("只恨我那是年纪太小，看不透他那小小花招背后的柔情。Only hate me that's age is too small, cannot see through his little tricks behind the tender feelings.")
j.append("小王子：我那时什么也不懂！我应该根据她的行为，而不是根据她的话来判断她。她香气四溢，让我的生活更加芬芳多彩，我真不该离开她的...我早该猜到，在她那可笑的伎俩后面是缱绻")
j.append("柔情啊。花朵是如此的天真无邪！可是，我毕竟是太年轻了，不知该如何去爱她。")
j.append("这是我的一个秘密，再简单不过的秘密：一个人只有用心去看，才能看到真实。事情的真相只用眼睛是看不见的。")
j.append("你知道的-当一个人情绪低落的时候，他会格外喜欢看日落……")
j.append("正是你为你玫瑰花所花费的时间，才让你的玫瑰花变得如此重要。Is your roses the time it takes for you, that makes your rose so important.")
j.append("村庄的温情不会外泄，想体会它的美丽，你不能匆匆走过。Village of warmth will not leak, wanted to experience its beauty, you can't hurried by.")

@bot.register(my_friend)
def reply(msg):
	jj=j
	print (msg.sender.name,':',msg.text,'Msg Type:',msg.type)
	msg.sender.mark_as_read()
	if ("Hello,jiayang" in msg.text):
		my_msg=random.choice(jj)
		msg.reply_msg(my_msg)
		print("我: ",my_msg)

		jj_p=jj.index(my_msg)
		jj.pop(jj_p)
		if(len(jj)==0):
			msg.reply_msg("如果再也见不到你,那祝你早安,午安,晚安.")
		# subprocess.call("pause",shell=True)
		# os.system("pause")
embed()		
# bot.join()

