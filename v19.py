import time
import random
import hashlib
from urllib import request, parse


def getSalt():
    salt = int(time.time()*1000) + random.randint(0, 10)
    return salt


def getMD5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign


def getsign(key, salt):
    sign = "fanyideskweb" + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMD5(sign)
    return sign


def youdao(key):
    salt = getSalt()
    sign = getsign(key, salt)
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": str(sign),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=995273788@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=793578770.1458806; JSESSIONID=aaasoMg9oPXbLhaetkisw; fanyi-ad-id=46607; fanyi-ad-closed=1; ___rl__test__cookies=1531292839917",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }
    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    key = input("Input a keyword:")
    youdao(key)