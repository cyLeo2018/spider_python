# scrapy
# 爬虫框架
- 框架
- 爬虫框架
    - scrapy
    - pyspider
- scrapy框架介绍
    - 官方文档：https://doc.scrapy.org/en/latest/
    - 中文文档：http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
- 安装：
    - 利用pip
        - pip install scrapy
- scrapy概述
    - 模块
        - ScrapyEngine:核心引擎，
        - Scheduler:调度器,调度request请求
        - Downloader:下载器，处理request请求，得到response
        - Spider爬虫:负责把下载器得到的结果进行分析，生成数据和链接
        - ItemPipeline管道:详细处理Item
        - DownloaderMiddleware下载中间件：自定义下载的功能扩展组件
        - SpiderMiddleware爬虫中间件：对spider进行功能扩展

- 爬虫项目大概流程：
    - 新建项目：scrapy startproject xxx
    - 明确需要目标/产出：编写item.py
    - 制作爬虫:地址 spider/xxxspider.py
    - 存储内容：pipelines.py

- ItemPipeline
    - 对应的是pipelines文件
    - 爬虫提取出数据存入item后，item中保存的数据需要进一步处理，比如清洗、去重、存储等
    - process_item
        - spider提取出来的item作为参数传入，同时传入的还有spider
        - 此方法必须实现
        - 必须返回一个item对象，被丢弃的item不会被之后的pipeline处理
    - __init__:构造函数
        - 进行必要的参数初始化
    - open_spider(spider):
        - spider对象被开启的时候调用
    - close_spider(spider):
        - 当spider对象被关闭的时候调用
- Spider
    - 对应的是文件夹spider下的文件
    - __init__:初始化爬虫名称,start_urls列表
    - start_requests:生成requests对象交给Scrapy下载器，返回response
    - parse:根据返回的response解析相应的item,item自动进入pipeline,如果需要，解析出url,url交给requests模块，如此循环
    - start_request:此方法仅能被调用一次，读取start_urls内容并启动循环过程
    - name:设置爬虫名称
    - start_urls：设置开始第一批爬取的url
    - allow_domain:spider允许爬取的域名列表
    - start_request(self)：只被调用一次
    - parse
    - log:日志记录

- 中间件(DownloaderMiddlewares)
    - 中间件是处于引擎和下载器中间的一层组件
    - 可以有很多个，按顺序加载执行
    - 作用是对发出的请求和返回结果执行处理
    - 在middlewares文件夹中
    - 需要在settings中设置以便生效
    - 一般一个中间件完成一项功能
    - 必须实现以下一个或多个防范
        - process_request(self, request, spider)
            - 在request通过的时候被调用
            - 必须返回None或Response或Request或raise IgnoreRquest
                - None:scrapy继续处理该request
                - Request:scrapy停止调用process_request并重新调度返回的request
                - Response:scrapy不会调用其他prcess_request或process_exception,直接将该response作为结果
        - process_response(self, request, response, spider)
            - 与process_request类似
            - 每次返回结果的时候自动调用
            - 可以有多个，按顺序调用

- 去重
    - 防止死循环，需要去重
    - 在spider中的parse函数中，返回request时加上dont_filter=False参数

- 在scrapy中使用selenium
    - 放入中间件process_request函数中


