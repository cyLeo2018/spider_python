import re

str = "Hello world wide web"
s = r'([a-z]+)([a-z]+)'
pattern = re.compile(s, re.I)
m = pattern.match(str)
s = m.group(0)
print(s)
a = m.span(0)
print(a)
s = m.group(1)
print(s)
a = m.span(1)
print(a)
s = m.groups()
print(s)
