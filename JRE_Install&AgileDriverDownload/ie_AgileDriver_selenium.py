import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import  xml.dom.minidom
from pykeyboard import PyKeyboard
dom = xml.dom.minidom.parse('database.xml')
root = dom.documentElement
itemlist = root.getElementsByTagName('login')
item = itemlist[0]
User=item.getAttribute("username")
Pwd=item.getAttribute("passwd")

li=list((input("input SWB:").split(" ")))
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
			browser.implicitly_wait(20)
			browser.switch_to_window(browser.window_handles[1])
			browser.implicitly_wait(20)
			break
	dir="C:\\AgileDownload\\"+str(SWB)
	os.system("md %s" %(dir))
	browser.implicitly_wait(20)
	browser.switch_to_window(browser.window_handles[1])
	WebDriverWait(browser,1000,0.2).until(lambda browser:browser.find_element_by_id('selector_elm'))
	ele=browser.find_element_by_id('selector_elm')
	browser.execute_script('arguments[0].click()',ele)
	ele=browser.find_element_by_xpath('//*[@id="cls_901"]/a')
	browser.execute_script('arguments[0].click()',ele)
	WebDriverWait(browser,1000,0.2).until(lambda browser:browser.find_element_by_name('QUICKSEARCH_STRING'))
	browser.find_element_by_name('QUICKSEARCH_STRING').send_keys(Keys.CONTROL + 'a')
	browser.find_element_by_name('QUICKSEARCH_STRING').send_keys(str(SWB))
	browser.find_element_by_name('QUICKSEARCH_STRING').send_keys(Keys.ENTER)
	# WebDriverWait(browser,300,0.5).until(lambda browser:browser.find_element_by_id('Actionsspan'))
	browser.implicitly_wait(200)
	WebDriverWait(browser,1000,0.2).until(lambda browser:browser.find_element_by_xpath('//*[@id="Actionsspan"]'))
	# ele=browser.find_element_by_id('Actionsspan')
	ele=browser.find_element_by_xpath('//*[@id="Actionsspan"]')
	browser.execute_script('arguments[0].click()',ele)
	WebDriverWait(browser,1000,0.2).until(lambda browser:browser.find_element_by_xpath("//a[text()='AIC_AgileAttachmentUtility']"))	
	ele=browser.find_element_by_xpath("//a[text()='AIC_AgileAttachmentUtility']")
	browser.execute_script('arguments[0].click()',ele)
	browser.implicitly_wait(20)
	for x in range(2,99999):
		if(len(browser.window_handles)>=3):
			browser.switch_to_window(browser.window_handles[-1])
			browser.implicitly_wait(20)
			break
	time.sleep(2)		
	WebDriverWait(browser,200,0.5).until(lambda browser:browser.find_element_by_link_text('File Download'))		
	ele=browser.find_element_by_link_text('File Download')
	browser.execute_script('arguments[0].click()',ele)
	time.sleep(10)
	WebDriverWait(browser,600,0.5).until(lambda browser:browser.find_elements_by_css_selector('input[type=checkbox]'))
	checkboxes = browser.find_elements_by_css_selector('input[type=checkbox]')
	for checkbox in checkboxes:
		browser.execute_script('arguments[0].click()',checkbox)
	download= browser.find_elements_by_css_selector('input[type=button]')
	browser.execute_script('arguments[0].click()',download[0])
	for x in range(2,100):
		if(len(browser.window_handles)>=3):
			time.sleep(3)
			browser.switch_to_window(browser.window_handles[-1])
			break
	time.sleep(60)
	k = PyKeyboard()
	# k.tap_key(k.right_key)
	k.type_string(dir)
	k.tap_key(k.enter_key)
	time.sleep(10)