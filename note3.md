# 动态HTML
## 爬虫与反爬虫
## 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从javascript代码入手采集
    - Python第三方库运行javascript，直接采集你在浏览器看到的页面
## Selenium + PhantomJS
- Selenium:web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装 pip install selenium
    - 官网 http://selenium-python.readthedocs.io/index.html
- PhantomJS
    - 官网 http://phantomjs.org/download.html
    - 浏览器
    - 基于Webkit的无界面浏览器
- Selenium库有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，进行数据爬取

## chrome + chromedriver
- 下载安装chrome
- 下载安装chromedriver
- Selenium操作主要分为两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例37
