#!/usr/bin/python3


# 用chrome打开bd
from time import sleep


def open_bdsite_with_chrome_browser():
     from selenium import webdriver
     browser = webdriver.Chrome('/home/chin/company/program/chromedriver')
     browser.get('https://www.baidu.com/')

# 打开python主页, 输入pycon回车, 获得搜索结果页面, 来模拟搜索
def search_by_keyword():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome('/home/chin/company/program/chromedriver')
    driver.get('http://www.python.org')
    assert 'Python' in driver.title
    elem = driver.find_element_by_name('q')
    elem.send_keys('pycon')
    elem.send_keys(Keys.RETURN)
    print(driver.page_source)


# 模拟tb登录 -- failed
# 难度高, 放弃....
def mock_login():
    username = ''
    passwd = ''

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome('/home/chin/company/program/chromedriver')
    driver.get('https://h5.m.taobao.com/fav/index.htm?spm=a2141.7756461.1.2#!shop/queryColShop-1')
    # 页面元素嵌套在iframe, 首先需要选中iframe, 如果不切换到iframe会导致用户名密码输入框搜索不到
    driver.switch_to.frame(0)
    user = driver.find_element_by_xpath('//input[@name="TPL_username"]')
    passwd = driver.find_element_by_xpath('//input[@name="TPL_password"]')
    user.send_keys(username)
    passwd.send_keys(passwd)
    sleep(2)
    driver.find_element_by_id('btn-submit').send_keys(Keys.RETURN)
    sleep(2)
    # 关闭弹出提示框
    driver.find_element_by_class_name('km-dialog-btn').click()
    # 重新填写密码
    passwd.send_keys(passwd)
    sleep(3)
    # 找到验证圆圈
    circle = driver.find_element_by_xpath('//*[@id="nc_1-stage-1"]/div/div[1]/div')
    circle.click()
    sleep(3)
    # 再次点击登录按钮
    driver.find_element_by_id('btn-submit').send_keys(Keys.RETURN)
    sleep(11115)
    print(driver.page_source)


if __name__ == '__main__':
    # search_by_keyword()
    # open_bdsite_with_chrome_browser()
    mock_login()
