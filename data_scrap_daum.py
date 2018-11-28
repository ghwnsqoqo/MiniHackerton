from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import time

userAgent = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

def getdownload(url,params=None,numRetries=2):
    html = requests.get(url,params, headers=userAgent)
    
    if 500 <= html.status_code <= 600 and numRetries > 0:
        html = getdownload(url, numRetries-1)
    
    return html

driver = webdriver.Chrome()
query = "°í¶ó´Ï"

url = "https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=" + query
driver.get(url)

ext = {'jpeg':'jpg', 'jpg':'jpg', 'png':'png', 'bmp':'bmp', 'gif':'gif', 'pjpeg':'png'}

dom = BeautifulSoup(driver.page_source,"lxml")
img_list = dom.select(".wrap_thumb .thumb_img")

img_wrap = driver.find_element_by_tag_name("body")

n=5
while n is not 0:
    img_wrap.send_keys(Keys.END)
    n -= 1
    time.sleep(1)

for i,img in enumerate(img_list):
    print(img["data-src"])
    html = getdownload(img["data-src"])
    contentType = html.headers.get("content-type").split("/")
    if(content_type[0] == 'image'):
        with open('C:/Users/dwlee/Python_Jupyter/DataScrape_Ryu/Crawling_Image/Daum/Gorani/'+str(100 + i)+'.'+ext[content_type[1]], 'wb') as fp:
            fp.write(html.content)
