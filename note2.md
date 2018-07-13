# 页面分析和数据提取
- 结构化数据
    - 先有结构，再谈数据
    - json数据
        - JSON Path
        - 转换成python类型进行操作(json类)
    - XML文件
        - 转换成python类型进行操作(xmltodict)
        - XPath
        - CSS选择器
        - 正则

- 非结构化数据
    - 现有数据，再谈结构
        - 文本
        - 电话号码
        - 邮箱地址
            - 通常处理此类数据，使用正则表达式
        - html文件
            - 正则
            - XPath
            - CSS选择器

# 正则表达式
- 一套规则，可以在字符串文本中进行搜索替换
- 案例v23,re的基本使用流程
    - re模块
    - compile函数将正则表达式的字符串编译为Pattern对象
    - 通过Pattern对象的方法对文本进行匹配，匹配结果为Match对象
    - 通过Match对象的方法，对结果进行操作

- 案例v24,match的基本使用
