from urllib import request
from lxml import etree
from bs4 import BeautifulSoup

url = "https://sci-hub.st/10.1017/S1053837200005290"

headers = ('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Referer', 'https://googleads.g.doubleclick.net/')
 

opener = request.build_opener()
opener.addheaders(headers)
response = opener.urlopen(url)

print('\n响应结果是：', response)
print('访问的地址是：', response.url)

try:
    soup = BeautifulSoup(response.text, features='lxml')
    pdf_URL = soup.button['onclick']
except:
    print("解析失败！")

request.urlretrieve(pdf_URL)
