from urllib import request, parse
import json


if __name__ == '__main__':
    url = "http://fanyi.baidu.com/sug"
    kw = input("input a keyword:")
    data = {
        "kw": kw
    }
    data = parse.urlencode(data).encode()
    headers = {
        'Content-Length': len(data)
    }
    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    json_data = rsp.read().decode()
    json_data = json.loads(json_data)
    for i in json_data['data']:
        for k, v in i.items():
            print("{0}".format(v))



