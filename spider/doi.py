import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = 'https://www.nature.com/search?q=Machine%20learning,%20molecular%20design,%20QSPR&date_range=2012-2023&order=relevance'

# 存储获取的内容的列表
data = []
# 获取当前年份
current_year = datetime.datetime.now().year
# 爬取300篇文献
for i in range(1, 2):
    # 构造链接
    search_url = url + str(i)
    print(search_url)
    # 获取网页的 HTML 代码
    r = requests.get(search_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    # 提取需要的信息
    for article in articles:
        doi = article.find('a', {'data-track-action': 'view article'}).get('href').split('/')[-1]
        data.append([doi,])
        if current_year <= 10:
            data.append([ doi,])

# 将数据打印出来
for d in data:
    print("DOI:", d[0])
    print()

# 将数据导入到 Excel 表格中
df = pd.DataFrame(data, columns=['DOI'])
df.to_excel('doi.xlsx', index=False)