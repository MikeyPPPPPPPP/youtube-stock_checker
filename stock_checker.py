#size 10
import urllib.request
from bs4 import BeautifulSoup
html = ("https://www.google.com/search?q=uuraf&oq=uuraf&aqs=chrome..69i57j0l7.1412j0j7&sourceid=chrome&ie=UTF-8")

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(html, headers = headers)
resp = urllib.request.urlopen(req)

r = resp.read()
soup = BeautifulSoup(r, 'lxml')

'''

string we find to parse

<span class="IsqQVc NprOob iVHhrQyJ7MqQ-zJFzKq8ukm8">0.16</span> 0.16
'''

price = ''

for data in soup.find_all('span'):
    if data.has_attr('class') and data['class'][0].startswith('IsqQVc'):
        if '()' not in str(data.text):
            price = str(data.text)
            #print(data.text)     #this is for debugging, it prints the price
        else:
            pass


print(price)
