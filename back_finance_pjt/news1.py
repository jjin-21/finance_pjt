# import requests
# from bs4 import BeautifulSoup as bs

# url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259'
# response = requests.get(url).text
# soup = bs(response, 'html.parser')
# a=soup.find('ul',{'class': 'type06_headline'}).find_all('li')
# print(a)

import os
import sys
import urllib.request
client_id = "CYv34EtcXhZ6vin_mvaa"
client_secret = "YHwJY0Xu1l"
encText = urllib.parse.quote("적금 상품")
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)