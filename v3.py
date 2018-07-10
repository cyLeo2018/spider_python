from urllib import request

if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifu"
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)
    print(rsp.geturl())
    print(rsp.info())
    print(rsp.getcode())
    html = rsp.read()
    print(html)