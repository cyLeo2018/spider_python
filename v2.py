import chardet
from urllib import request

if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifu"
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html) #返回字典
    print(type(cs))
    print(cs)
    html = html.decode(cs.get("encoding", "uft-8"))
    print(html)