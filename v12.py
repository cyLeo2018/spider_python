from urllib import request

if __name__ == '__main__':
    url = "http://cps.17byh.com/index.php?s=/admin/public/login.html"
    headers = {
        "Cookie": "__jsluid=0dc621e0fb9ae2285e9debf75769930d; \
        Hm_lvt_35cbed5f3d75ce04b45c0bf79a7b0af7=1528251414,1528355438; \
        auth=47d9832a95daf417dc2863e219b2f3f2%3A880c97a3c3e99e5aed1178b9873b77f6; \
        username=qq3299861842; PHPSESSID=8ncojk8ikrjn3nc5s1r0rjus05"
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()
    with open("byh2.html", "wb") as f:
        f.write(html)