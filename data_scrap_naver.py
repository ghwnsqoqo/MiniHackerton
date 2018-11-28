from bs4 import BeautifulSoup
import requests
userAgent = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}

def getDownload(url,parmas=None ,num_rtries=2):
    
    resp = requests.request("get",url,params=params,headers=userAgent)
    if 500<= resp.status_code < 600 and NumRetries > 0:
        print("error",resp.status_code , resp.reason)
        return download(url,params,NumRetries-1) 
        
    return resp

def getUrls(url,params=None,num_depth=2):
    html = getDownload(url,params)
    dom = BeautifulSoup(html.text,'lxml')
    aList = dom.select('a')
    data = []
    
    for anchor in aList:
        if anchor.has_attr('href'):
            if anchor['href'].startswith('http') :
                data.append(anchor['href'])
    if num_depth >0 :
        for anchor in data:
            getUrls(anchor , num_depth=(num_depth-1))
    if num_depth >0 :
        for anchor in data:
            getUrls(anchor , num_depth=0)
            
    return data

url = "https://search.naver.com/search.naver"
params = {"where":"image","sm":"tab_jum","query":"°í¶ó´Ï"}
ext = {'jpeg':'jpg', 'jpg':'jpg', 'png':'png', 'bmp':'bmp', 'gif':'gif', 'pjpeg':'png'}

html = getDownload(url,params)
dom = BeautifulSoup(html.text,"html.parser")
imgList = dom.select("img._img")

for i,img in enumerate(imgList):
    html = getDownload(img["data-source"])
    content_type = html.headers.get('content-type').split('/')
    if(content_type[0] == 'image'):
        with open('C:/Users/dwlee/Python_Jupyter/DataScrape_Ryu/Crawling_Image/Google/Gorani/'+name+'.'+ext[content_type[1]], 'wb') as fp:
            fp.write(html.content)
