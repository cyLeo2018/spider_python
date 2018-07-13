import requests


if __name__ == '__main__':
    url = "http://fanyi.baidu.com/sug"
    kw = input("input a keyword:")
    data = {
        "kw": kw
    }
    rsp = requests.post(url, data=data)
    print(rsp.json())




