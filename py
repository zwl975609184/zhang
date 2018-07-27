from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random    #随机数
from time import sleep
def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)
dr=webdriver.Chrome()
dr.get("https://qzone.qq.com")
sleep(2)
dr.switch_to_frame(0)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()#点击
sleep(2)
dr.find_element_by_id('u').send_keys('2724896125')
dr.find_element_by_id('p').send_keys('zwl15091776390')
sleep(2)
dr.find_element_by_id('login_button').click()
sleep(2)
d=dr.find_element_by_link_text('好友')
ActionChains(dr).move_to_element(d).perform()#悬停
sleep(2)
dr.find_element_by_xpath('//*[@id="friend_search_input"]').send_keys('975609184')
sleep(2)
dr.find_element_by_xpath('//*[@id="friend_search_input"]').send_keys(Keys.ENTER)
b=dr.current_window_handle  #获取当前句柄
temp=dr.window_handles
for x in temp:
    if x!=b:
        dr.switch_to.window(x)    #到新的打开页
sleep(2)
dr.find_element_by_link_text('留言板').click()
while True:
    s=''
    while True:
        g=Unicode()
        s=s+g
        if len(s)==8:
            break
    sleep(2)
    dr.switch_to.frame('tgb')
    sleep(2)
    dr.switch_to.frame('veditor1_Iframe')
    sleep(2)
    dr.find_element_by_xpath('/html/body').send_keys(s)
    dr.switch_to.default_content()
    sleep(2);
    dr.switch_to.frame('tgb')
    dr.find_element_by_xpath('//*[@id="btnPostMsg"]').click()
    dr.switch_to.default_content()
    sleep(2)
