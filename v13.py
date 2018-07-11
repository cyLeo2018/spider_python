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


def getHomePage():
    url = "http://www.renren.com/965360364/profile"
    rsp = opener.open(url)
    html = rsp.read()
    with open("renren.html", "wb") as f:
        f.write(html)


if __name__ == '__main__':
    login()
    getHomePage()