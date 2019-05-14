import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pykeyboard import PyKeyboard
import  xml.dom.minidom
dom = xml.dom.minidom.parse('database.xml')
root = dom.documentElement
itemlist = root.getElementsByTagName('login')
item = itemlist[0]
User=item.getAttribute("username")
Pwd=item.getAttribute("passwd")

li=list((input("input Report Name:").split(" ")))
cwd=os.getcwd()
path=cwd+"\\IEDriverServer.exe"
iedriver=(path)	
os.environ["webdriver.ie.driver"] = iedriver 
browser = webdriver.Ie(iedriver)
browser.get("https://agile.us.dell.com/Agile/default/login-cms.jsp")
browser.find_element_by_name('j_username').clear()
browser.find_element_by_name('j_username').send_keys(User)
browser.find_element_by_name('j_password').clear()
browser.find_element_by_name('j_password').send_keys(Pwd)
browser.find_element_by_name('j_password').send_keys(Keys.ENTER)
for SWB in li:
	print(SWB)
	for x in range(2,99999):
		if(len(browser.window_handles)>=2):
			browser.switch_to_window(browser.window_handles[1])
			browser.implicitly_wait(10)
			break
	time.sleep(1)
	WebDriverWait(browser,10,0.1).until(lambda browser:browser.find_element_by_id('selector_elm'))
	ele=browser.find_element_by_id('selector_elm')
	browser.execute_script('arguments[0].click()',ele)
	ele=browser.find_element_by_xpath('//*[@id="cls_3091"]/a')
	browser.execute_script('arguments[0].click()',ele)
	WebDriverWait(browser,20,0.5).until(lambda browser:browser.find_element_by_name('QUICKSEARCH_STRING'))
	browser.find_element_by_name('QUICKSEARCH_STRING').send_keys(Keys.CONTROL + 'a')
	browser.find_element_by_name('QUICKSEARCH_STRING').send_keys(str(SWB))
	browser.find_element_by_name('QUICKSEARCH_STRING').send_keys(Keys.ENTER)
	time.sleep(1)
	ele=browser.find_element_by_xpath("//a[text()='"+str(SWB)+"']")
	browser.execute_script('arguments[0].click()',ele)
	browser.implicitly_wait(10)
	ele=browser.find_element_by_id('MSG_RptObjectExecutespan')
	browser.execute_script('arguments[0].click()',ele)
	for x in range(2,99999):
		if(len(browser.window_handles)>=3):
			browser.switch_to_window(browser.window_handles[-1])
			browser.implicitly_wait(10)
			break
	time.sleep(2)
	WebDriverWait(browser,30,0.1).until(lambda browser:browser.find_element_by_id('cmdFinishspan'))
	ele=browser.find_element_by_id('cmdFinishspan')
	browser.execute_script('arguments[0].click()',ele)
	time.sleep(70)
	print(browser.window_handles)
	for x in range(2,99999):
		if(len(browser.window_handles)>=3):
			browser.switch_to_window(browser.window_handles[-1])
			browser.implicitly_wait(10)
			break
	browser.implicitly_wait(10)
	browser.switch_to.frame(0)	
	# WebDriverWait(browser,20,0.1).until(lambda browser:browser.find_element_by_xpath('//*[@id="exportRpt"]/span'))
	ele=browser.find_element_by_xpath('//*[@id="exportRpt"]/span')
	browser.execute_script('arguments[0].click()',ele)
	time.sleep(1)
	browser.switch_to_window(browser.window_handles[-1])
	browser.switch_to.frame(1)	
	time.sleep(1)
	ele=browser.find_element_by_id('prompt_ok')
	browser.execute_script('arguments[0].click()',ele)
	time.sleep(8)
	k = PyKeyboard()
	# k.press_key(k.tab_key)

	k.tap_key(k.tab_key,2)
	k.tap_key(k.enter_key)
	