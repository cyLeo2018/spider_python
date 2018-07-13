from urllib import request
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
    rsp = request.urlopen(url)
    data = rsp.read().decode()
    data = json.loads(data)
    print(data)
    for i in data:
        print(i)

