from urllib import request, parse


def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1531292839921",
        "sign": "673d32b326bbbd9fee475cce31047e59",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "203",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=995273788@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=793578770.1458806; JSESSIONID=aaasoMg9oPXbLhaetkisw; fanyi-ad-id=46607; fanyi-ad-closed=1; ___rl__test__cookies=1531292839917",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "X-Requested-With": 'XMLHttpRequest"
    }
    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    key = input("Input a keyword:")
    youdao(key)