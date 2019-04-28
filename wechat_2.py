from wxpy import *
bot = Bot()
tuling = Tuling(api_key='a05e064837ec40df929370b69c8397ac') 
company_group = ensure_one(bot.groups().search('跟着老板老板娘闯天下'))
y=0
for x in company_group:
	y+=1
	print(str(y)+". "+x)

# @bot.register(my_friend)
# def reply_my_friend(msg):
    # tuling.do_reply(msg)
    # print(msg.text, msg.sender)
    # print(tuling.reply_text(msg))

# bot.join()