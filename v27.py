import re


hello = u"你好，世界"
pattern = re.compile(r'[\u4e00-\u9fa5]+')
m = pattern.match(hello)
print(m)