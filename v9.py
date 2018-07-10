from urllib import request, error


if __name__ == '__main__':
    url = "http://www.paopao7.com/kaifu"
    try:
        # headers = {}
        # headers['User-Agent'] = "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
        # req = request.Request(url, headers=headers)

        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3")

        rsp = request.urlopen(req)
        print(rsp.info())
        html = rsp.read().decode()
    except Exception as e:
        print(e)