from urllib import request


if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifu"
    rsp = request.urlopen(url) #http.client.HTTPResponse类
    print(type(rsp))
    print(rsp)
    html = rsp.read().decode() #read读取的是byte流，需要decode解码
    print(html)




