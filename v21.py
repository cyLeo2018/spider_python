import requests


if __name__ == '__main__':
    url = "http://www.baidu.com"
    rsp = requests.get(url)
    print(type(rsp))
    print(rsp)
    print(rsp.text)

    rsp = requests.request("get", url)
    print(type(rsp))
    print(rsp)
