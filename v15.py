from urllib import request, parse
from http import cookiejar

filename = "renren_cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
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
    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    login()
