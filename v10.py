from urllib import request, error


if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifu"
    proxy = {'http': '129.213.24.42:3128'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except Exception as e:
        print(e)