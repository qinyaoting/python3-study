#!/usr/bin/python3


# 用chrome打开bd
import collections
import re
import math
import threading
from time import sleep, time
from urllib import request

import datetime


def fecth_region():

    city_or_province = []
    company_urls = []
    from selenium import webdriver
    brower = webdriver.Chrome('/home/chin/company/program/chromedriver')
    brower.get('http://m.familydoctor.com.cn/ypk/arealist.html')
    # print(brower.page_source)
    province_nodes = brower.find_elements_by_xpath('/html/body/section[1]/div[3]/div[1]/a')

    for i in range(len(province_nodes[:2])):
        sleep(2)
        province_nodes[i].click()
        company_url = brower.find_element_by_xpath('html/body/section[1]/div[3]/div[2]/div[' + str(i+1) + ']/div/a[1]')
        # print('%s - %s - %s' % (province_nodes[i].text, company_url.text, company_url.get_attribute('href')))
        city_or_province.append(province_nodes[i].text)
        company_urls.append(company_url.get_attribute('href'))
    return collections.OrderedDict(zip(city_or_province, company_urls))

def fectch_drug_company_by_region(region_url):

    drug_companies = []
    comp_product_urls = []
    for region,url in region_url.items():
        # print(k, v)
        from selenium import webdriver
        brower = webdriver.Chrome('/home/chin/company/program/chromedriver')
        brower.get(url)

        drug_comp_nodes = brower.find_elements_by_xpath('/html/body/section[1]/div[3]/div[2]/ul/li/a')
        for dr in drug_comp_nodes:
            # print('%s - %s' % (dr.text, dr.get_attribute('href')))
            drug_companies.append(dr.text)  # 药厂名称  北京中新制药厂（155）
            comp_product_urls.append(dr.get_attribute('href'))  # 对应药厂产品列表
    return collections.OrderedDict(zip(drug_companies, comp_product_urls))


def fecth_drug_by_company(product_urls):

    product_urls_per_province = []
    for company, product_url in product_urls.items():
        # line = '北京中新制药厂（155） '
        rerule = re.compile(r'\d+')
        total = int(rerule.findall(company)[0])
        maxpage = int(math.ceil(total / 20))
        print('%s url:%s total:%s maxpage:%s' % (company, product_url, total, maxpage))
        n = 1
        while n <= maxpage:
            product_url = re.sub(r'_\d+\.', '_'+str(n)+'.', product_url)
            n = n + 1
            product_urls_per_province.append(product_url)
        return product_urls_per_province


def crawl_drug_list_by_company(url):

    # url = 'http://m.familydoctor.com.cn/ypk/factorymedicine_12947_0_0_0_0_27.html'
    from selenium import webdriver
    brower = webdriver.Chrome('/home/chin/company/program/chromedriver')
    brower.get(url)
    drug_item_nodes = brower.find_elements_by_xpath('/html/body/section[1]/div[4]/div[2]/div[1]/div/div[1]/dl/dd/h2/a')
    company_item_nodes = brower.find_elements_by_xpath('/html/body/section[1]/div[4]/div[2]/div[1]/div/div[1]/dl/dd/b/a')
    indication_item_nodes = brower.find_elements_by_xpath('/html/body/section[1]/div[4]/div[2]/div[1]/div/div[1]/dl/dd/p/a')

    for i in range(len(drug_item_nodes)):
        print('--%s \n ----%s \n ------%s' % (drug_item_nodes[i].text, company_item_nodes[i].text, indication_item_nodes[i].text))
    sleep(0.5)



from selenium import webdriver
driver = webdriver.Chrome('/home/chin/company/program/chromedriver')

def fetch_html_with_retry(id, url, retries=3, timeout=10):

    times = 1
    while times <= retries:
        try:
            print('id:%s - try %d times - url:%s' % (i, times, url))
            response = get_resonpse(url)
            if response:
                print('get html: %s' % response.strip('\<head\>')[0])
                break

        except ZeroDivisionError as e:
            times = times + 1

        finally:

            if times > 3:
               print('try third times, give up..')


# 如果超过10s, 还没有打开, 那就取消掉任务
def get_resonpse(url):
    timer = threading.Timer(10.0, raise_ex)
    timer.start()
    starttime = datetime.datetime.now()
    driver.get(url)
    resp = driver.page_source
    # sleep(11)
    endtime = datetime.datetime.now()
    if (endtime - starttime).seconds <= 10:
        timer.cancel()
    return resp

def raise_ex():
    raise ZeroDivisionError("xxxxxx")



if __name__ == '__main__':

    url = 'http://m.familydoctor.com.cn/ypk/arealist.html'
    for i in range(0, 5):
        fetch_html_with_retry(i, url)



# urls = fecth_drug_by_company(
    #     fectch_drug_company_by_region(
    #         fecth_region()))
    #
    # for url in urls:
    #     crawl_drug_list_by_company(url)
    # 超时的问题
    # 带有层级关系的爬取
    # scrapy 滚动到元素位置,

