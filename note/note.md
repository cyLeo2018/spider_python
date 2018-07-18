# 参考资料
- Python 3网络爬虫开发实战 催庆才
- [python3网络爬虫](https://blog.csdn.net/c406495762/article/details/72858983)
- [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)

- python网络数据采集 图灵工业出版
- Python爬虫开发与项目实战， 范传辉， 机械工业出版社
- 精通python爬虫框架Scrapy 人民邮电出版 李斌 翻译



# 前提知识
- url
- http
- html\css\js
- ajax
- re\xpath
- xml

# 爬虫简介
- 爬虫定义:按照一定规则，自动抓取网站信息的程序
- 爬虫特征:
    - 按要求下载数据或内容
    - 自动在网络上流窜？？
- 三大步骤：
    - 下载网页
    - 提取有用数据
    - 根据规则自动跳转其他URL执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫(聚焦爬虫)
- python爬虫包
    - python2.x: urllib urllib2 urllib3 httplib httplib2 requests
    - python3.x: urllib urllib3 httplib2 requests

# urllib
- 包含模块
    - urllib.request 打开和读取url
    - urllib.error 常见错误，使用try捕获
    - urllib.parse 处理url方法
    - urllib.robotparse 解析robots.txt文件
    - 案例v1

# 网页编码问题
    - 第三方chardet包 自动检测网页编码，但是不一定准确，案例v2

# urllib.request.urlopen()的返回对象
    - geturl() 返回请求对象的url
    - info() 返回请求对象的meta信息
    - getcode() 返回状态码
    - 案例v3

# urllib.request.date的使用
- 访问网页的两种方法
    - get
        - 利用参数给服务器传递信息
        - 参数为dict,然后使用parse编码
        - 案例v4
    - post
        - 一般向服务器传递参数使用post
        - post将信息自动加密处理
        - 使用post信息，使用urllib.request.urlopen(data=) 参数
        - 使用post,意味着http请求头信息需要更新
            - Content-Type application/x-www.form-urlencode
            - Content-Length 数据长度
            - 一旦更改请求方法，要注意请求头的相关信息
        - urllib.parse.urlencode(data=)可以将字符串自动转换成上面的
        - 案例v5
        - 为了更多的设置请求头信息，urllib.request.urlopen()不能满足要求
        - 使用urllib.request.Request
        - 案例v6

# urllib.error
- URLError产生的原因：
    - 网络不通
    - 服务器连接失败
    - 找不到指定服务器
    - URLError是OSError的一个子类
    - 案例v7
- HTTPError,是URLError的一个子类
- 案例v8
- OSError > URLError > HTTPError

# UserAgent
- UserAgent 用户代理，简称UA，属于请求头的一部分，服务器通过UA鉴别访问者身份
- 常见的UA
    ```
    1.Android
    Mozilla/5.0 (Linux Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
    Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

    2.Firefox
    Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
    Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0

    3.Google Chrome
    Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
    Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19

    4.iOS
    Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
    Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3
    ```
- 设置UA的方式
    - heads
    - add_header
    - 案例v9

# ProxyHandler代理(代理服务器)
- 使用代理IP，是爬虫的常用手段
- 获取代理服务器的地址：
    - www.xicidaili.com
    - www.goubanjia.com
- 代理使用步骤：
    - 设置代理地址
    - 创建ProxyHandler
    - 创建Opener
    - 安装Opener
    - 案例v10

# cookie & session
- 由于http的无状态，使用cookie和session记录连接状态
- cookie保存在客户浏览器端的一段信息，session是保存在服务器端的另一半信息
- cookie和session的区别
    - 存放位置不同
    - cookie放在客户端，并不安全，所以不存放敏感信息
    - session有过期时间
    - 单个cookie保存数据不超过4K，很多浏览器限制一个站点最多保存20个cookie
- session的存放位置
    - 存放在服务器端
    - 一般情况，session放在内存或者数据库中
    - 没有cookie登录 案例v11

- 使用cookie登录
    - 直接把cookie复制下来，然后放入请求头，案例v12
    - http模块包含一些关于cookie的模块，通过模块我们可以自动使用cookie
        - CookieJar
            - 管理、存储cookie,向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar(filename, delayload=None, policy=None)
            - 使用文件管理cookie
            - filename是存储的cookie文件
        - MozillaCookieJar
            - 创建与mozilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 关系：CookieJar-->FileCookieJar-->MozillaCookieJar & LwpCookieJar
    - 利用CookieJar访问 v13
        - 自动使用cookie登录，流程
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈的cookie
        - 利用提取的cookie登录隐私页面
    - handler是Handler的实例，常用的有
        - request.HTTPCookieProcessor(cookie)
        - request.HTTPHandler()
        - request.HTTPSHandler()
    - 创建handler后，使用opener打开，打开后相应的功能由相应的handler处理
    - 将cookie作为变量打印出来 案例v14
        - cookie属性
            - name 名称
            - value 值
            - domain 可以访问此cookie的域名
            - path 可以访问cookie的页面路径
            - exprise 过期时间
            - size 大小
            - http字段
    - cookie的保存-FileCookieJar 案例v15
    - cookie的读取，案例v16

# SSL
    - SSL证书就是指遵守SSL安全套接层协议的服务器数字证书(SecureSocketLayer)
    - 网景公司开发
    - CA（CertifacateAuthority）数字证书认证中心，发放、管理、废除证书的收信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理，案例v17

# js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理(迅雷是取md5值)
    - 经过加密传输的是密文，但是
    - 加密函数或者过程一定是在浏览器完成，也就是一定会把代码(js代码)暴露给使用者
    - 经过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 案例v18,v19
    
# ajax
- 异步请求
- 一定会有URL，请求方法，可能有数据
- 一般使用json格式 案例v20

# Requests模块
- HTTP for humans 更简洁更友好
- 继承urllib的所有特征
- 底层使用了urllib3
- 开源地址：https://github.com/requests/requests
- 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
- 安装:conda install requests
- get请求
    - requests.get(url)
    - requests.request("get", url)
    - 可以带有headers和parmas参数
    - 案例v21
- get返回内容
    - 案例v22
- post
    - rsp = requests.post(url, data=)
    - 案例v23
    - data, headers要求dict类型
- proxy
    - proxies = {
        "http":
        "https":
    }
    - rsp = requests.request("get", "http:xxx", proxies=proxies)
    - 代理有可能报错，如果使用人数过多，考虑安全问题，可能会被关闭
- 用户验证
    - 代理验证
        - proxy = {
            "http": "china:123456@192.168.1.1:4444"
        }
        - rsp = requests.get("http//www.baidu.com", proxies=proxy)
- web客户端验证
    - auth = ("test1", "123456")
    - rsp = requests.get("http://www.baidu.com", auth=auth)
- cookie
    - requests可以自动处理cookie信息
    - 案例
- session
    - 与服务器端session不是同一个
    - 模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开链接
    - 能让我们跨请求时保持某些参数，比如在同一个session实例发出的，所有请求之间保持cookie
        ss = requests.session()
        headers = {"User-Agent": "xxxxxx"}
        data = {"name": "xxxxxx"}
        ss.post("http://www.baidu.com", data=, headers=)
        rsp = ss.get("xxxxxx")
- https请求验证SSL证书
    - 参数verify负责表示是否需要验证ssl证书，默认是True
    - 如果不需要验证SSL证书，则设置成False表示关闭
        rsp = requests.get("https://www.baidu.com", verify=False)




