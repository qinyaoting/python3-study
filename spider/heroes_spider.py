'''
用selenium和phantomjs来模拟抓取包含ajax的页面
ajax执行完后会更改页面的某些元素,
如果获取这些元素, 直接获取是不行的,需要用下列方法----

'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 构造driver
driver = webdriver.PhantomJS(executable_path='/home/chin/company/program/phantomjs/bin/phantomjs')
driver.get('http://pvp.qq.com/web201605/herolist.shtml')
try:
    # 10是超时时间
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))
    heros_node = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/ul/li/a')


    hero_list = []
    url_list = []
    for node in heros_node:
        hero_list.append(node.text)
        url_list.append(node.get_attribute('href'))




    #17173 pvp
    data = pd.DataFrame({'hero':hero_list, 'url1':url_list})
    driver.get('http://news.17173.com/z/pvp/yxtj/index.shtml')
    nodes = driver.find_elements_by_xpath('//*[@id="jsheroshow"]/li/a')

    hero_list = []
    url_list = []
    for node in nodes:
        hero_list.append(node.text)
        url_list.append(node.get_attribute('href'))

    tmp = pd.DataFrame({'hero':hero_list, 'url2':url_list})
    data = pd.merge(data, tmp, on='hero')
    data.to_csv('/home/chin/pvp_hero.csv')

    # 4399 道具
    driver.get('http://news.4399.com/gonglue/wzlm/daoju/')
    action = ActionChains(driver)
    click_node = driver.find_element_by_xpath('//*[@id="hero_more"]/a')
    action.click(click_node)
    action.click(click_node)
    action.perform()
    heros_node = driver.find_elements_by_xpath('//*[@id="hreo_list"]/li/a')

    item_list = []
    url_list = []

    for hero in heros_node:
        item_list.append(hero.text)
        url_list.append(hero.get_attribute('href'))


    data = pd.DataFrame({'item':item_list, 'url1':url_list})
    data.to_csv('/home/chin/item_url.csv')


finally:
    print("finally")
    driver.close()