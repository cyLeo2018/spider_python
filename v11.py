from urllib import request

if __name__ =='__main__':
    url = "http://cps.17byh.com/index.php?s=/admin/public/login.html"
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    with open("byh.html", "w") as f:
        f.write(html)