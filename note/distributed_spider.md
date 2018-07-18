# 分布式爬虫
- 单机爬虫的问题：
    - 单机效率问题
    - IO吞吐问题
- 多爬虫问题
    - 数据共享
    - 在空间上不同的多台机器，可以成为分布式爬虫
- 需要做：
    - 共享队列
    - 去重
- Redis
    - 内存数据库
    - 数据持久化保存到文件系统
    - 去重
    - 理解成dict、set、list的集合体
    - 对保存的内容进行生命周期的控制

- 内容保存数据库
    - MongoDB
    - MySQL

- 安装scrapy_redis
    - pip install scrapy_redis
    - github.com/rolando/scrapy-redis
    - scrapy-redis.readthedocs.org


