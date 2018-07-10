# 参考资料
- python网络数据采集 图灵工业出版
- 精通python爬虫框架Scrapy 人民邮电出版
- [python3网络爬虫](https://blog.csdn.net/c406495762/article/details/72858983)
- [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
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
