from urllib import request


if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifu"
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)
    html = rsp.read().decode()
    print(html)




