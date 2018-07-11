from urllib import request, parse
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email": "18022308503",
        "password": "123456Qw"
    }
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    rsp = opener.open(req)


if __name__ == '__main__':
    login()
    print(type(cookie))
    print(cookie)
    for item in cookie:
        print(item)
