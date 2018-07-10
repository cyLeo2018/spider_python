from urllib import request, parse
import json


if __name__ == '__main__':
    url = "http://fanyi.baidu.com/sug"
    kw = input("input a keyword:")
    data = {
        "kw": kw
    }
    data = parse.urlencode(data).encode()
    # print(data)
    rsp = request.urlopen(url, data=data)
    # print(type(rsp))
    # print(rsp)
    json_data = rsp.read().decode()
    # print(type(json_data))
    json_data = json.loads(json_data)
    # print(type(json_data))
    # print(json_data)
    # print(json_data['data'])
    for i in json_data['data']:
        for k, v in i.items():
            print("{0}".format(v))



