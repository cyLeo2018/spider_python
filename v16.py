from urllib import request, parse
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
cookie.load("renren_cookie.txt", ignore_expires=True, ignore_discard=True)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def getHomePage():
    url = "http://www.renren.com/965360364/profile"
    rsp = opener.open(url)
    html = rsp.read()
    with open("renren2.html", "wb") as f:
        f.write(html)


if __name__ == '__main__':
    getHomePage()
