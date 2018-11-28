from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import json
import requests

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.`0.3440.106 Safari/537.36"}

def getDownload(url, params = None, num_retries = 2):
    resp = requests.get(url, params = params, headers = headers)

    if 500 <= resp.status_code < 600 and num_retries > 0:
        print("error : ", resp.status_code, resp.reason)
        return getDownload(url, params, num_retries - 1)

    return resp

driver = webdriver.Chrome()
query = '°í¶ó´Ï'
url = "https://www.google.com/search?biw=150&bih=700&tbm=isch&sa=1&ei=UWWsW7HeJcSD8gXOr5uADQ&q="+query+"&oq=%EC%9D%B4%EC%9C%A0%EB%B9%84&gs_l=img.3...0.0.0.136023.0.0.0.0.0.0.0.0..0.0....0...1c..64.img..0.0.0....0.ZW3HT5lvWr0"
driver.get(url)

ext = {'jpeg':'jpg', 'jpg':'jpg', 'png':'png', 'bmp':'bmp', 'gif':'gif', 'pjpeg':'png'}

img_wrap = driver.find_element_by_tag_name('body')
dom = BeautifulSoup(driver.page_source, 'lxml')
img_google = dom.select(".rg_meta.notranslate")

n=5
while n is not 0:
    img_wrap.send_keys(Keys.END)
    n -= 1
    time.sleep(1)

for i, img_list in enumerate(img_google):
    name = json.loads(img_list.text)['rid']
    result = json.loads(img_list.text)['ou']
    html = getDownload(result)
    content_type = html.headers.get('content-type').split('/')
    if(content_type[0] == 'image'):
        with open('C:/Users/dwlee/Python_Jupyter/DataScrape_Ryu/Crawling_Image/Google/Gorani/'+name+'.'+ext[content_type[1]], 'wb') as fp:
            fp.write(html.content)
    time.sleep(1)
