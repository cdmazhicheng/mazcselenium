#已添加环境变量

from selenium import webdriver

#pcbrowser = webdriver.Chrome()
pcbrowser = webdriver.Firefox()
pcbrowser.get('')

'''
1. 输入账号；
2. 输入密码；
3. 提交；
'''
username = 'mazc'
password = '123456'
elem = pcbrowser.find_element_by_name('UserName')
elem.send_keys(username)
elem = pcbrowser.find_element_by_name('Password')
elem.send_keys(password)
elem = pcbrowser.find_element_by_id('btnLogin')
elem.click()

pcbrowser.find_element_by_link_text(u'订单批次').click()
#pcbrowser.switch_to_frame('BatchOrderList')