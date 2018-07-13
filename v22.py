import requests


if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    key = input("Input a keyword:")
    kw = {
        "wd": key
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    rsp = requests.get(url, params=kw, headers=headers)
    print(type(rsp))
    print(rsp)
    print(rsp.content)
    print(rsp.url)
    print(rsp.encoding)
    print(rsp.status_code)
    print(rsp.headers)
    print(rsp.cookies)
