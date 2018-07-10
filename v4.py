from urllib import request, parse


if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    wd = input("input keyword:")
    qs = {
        "wd": wd
    }
    qs = parse.urlencode(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read().decode()
    print(html)
