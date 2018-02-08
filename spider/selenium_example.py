#!/usr/bin/python3


# 用chrome打开bd
from time import sleep
from urllib import request


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
    password = ''

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome('/home/chin/company/program/chromedriver')
    driver.get('https://h5.m.taobao.com/fav/index.htm?spm=a2141.7756461.1.2#!shop/queryColShop-1')
    # 页面元素嵌套在iframe, 首先需要选中iframe, 如果不切换到iframe会导致用户名密码输入框搜索不到
    driver.switch_to.frame(0)
    user = driver.find_element_by_xpath('//input[@name="TPL_username"]')
    passwd = driver.find_element_by_xpath('//input[@name="TPL_password"]')
    user.send_keys(username)
    passwd.send_keys(password)
    sleep(2)
    driver.find_element_by_id('btn-submit').send_keys(Keys.RETURN)
    sleep(2)
    # 关闭弹出提示框
    driver.find_element_by_class_name('km-dialog-btn').click()
    # 重新填写密码
    passwd = driver.find_element_by_xpath('//input[@name="TPL_password"]')
    passwd.send_keys(password)
    sleep(3)
    # 找到验证圆圈
    circle = driver.find_element_by_xpath('//*[@id="nc_1-stage-1"]/div/div[1]/div')
    circle.click()
    sleep(3)
    # 再次点击登录按钮
    driver.find_element_by_id('btn-submit').send_keys(Keys.RETURN)
    sleep(11115)
    print(driver.page_source)

# 读取ajax修改页面后的元素
def fetch_element_change_by_ajax():

    # from selenium import webdriver
    # import time
    # driver = webdriver.PhantomJS(executable_path=r'/home/chin/company/program/phantomjs/bin/phantomjs')
    # driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
    # # ajaxDemo.html延迟3秒会变为另一个内容
    # #  如果是1秒, 获得是第一个页面的内容, 如果改为3秒,将获得第二个页面,用来模拟获取ajax后, 页面的内容
    # time.sleep(3)
    # print(driver.find_element_by_id('content').text)
    # driver.close()

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.PhantomJS(executable_path='/home/chin/company/program/phantomjs/bin/phantomjs')
    driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))
    finally:
        print(driver.find_element_by_id('content').text)
        driver.close()

def fack_ua():
    # 如何伪装ua
    url = 'http://www.csdn.net/'
    # head = {}
    # head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    # req = request.Request(url,headers=head)
    # response = request.urlopen(req);
    # req = request.Request(url)
    # req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
    # response = request.urlopen(req)
    # html = response.read().decode('utf-8')
    # print(html)

    # 如何使用代理
    url = 'http://www.whatismyip.com.tw/'
    proxy = {'https': '110.73.10.187:8123'}
    proxy_support = request.ProxyHandler(proxy)

    opener = request.build_opener(proxy_support)

    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    request.install_opener(opener)

    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)

if __name__ == '__main__':
    # search_by_keyword()
    # open_bdsite_with_chrome_browser()
    # mock_login()
    fetch_element_change_by_ajax()
