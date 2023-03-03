# 網路爬蟲 BeautifulSoup 測試程式
import requests
from bs4 import BeautifulSoup
result =requests.get ('http://myweb.scu.edu.tw/~wencpai/')
x = BeautifulSoup(result.text,"html.parser")
print(x.select('span')[0].text )
print('\n程式測試完成 ......')
