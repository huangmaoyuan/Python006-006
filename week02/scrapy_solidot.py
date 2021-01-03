import requests
from lxml import etree
from queue import Queue
import threading
import json

url='https://www.solidot.org/'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent': ua}
response = requests.get(url, headers=header)
res= etree.HTML(response.text)
title = res.xpath('//div[@class="block_m"]/div[@class="ct_tittle"]/div[@class="bg_htit"]/h2/a/text()')
with open('./result.txt','a', encoding='utf-8') as f:
	for i in range(1,len(title)+1):
		f.write(str(i))
		f.write('\n')
		f.write(str(title[i-1]))
		f.write('\n')
