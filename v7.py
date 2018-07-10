from urllib import request, error

if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifua"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except Exception as e:
        print(e)
