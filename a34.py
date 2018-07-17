from urllib import request
from bs4 import BeautifulSoup


url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')
content = soup.prettify()

print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)

print(soup.name)
print(soup.attrs)


for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node)