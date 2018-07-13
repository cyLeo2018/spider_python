import re

str = "one12twothree3"
s = r"\d+"
pattern = re.compile(s)
print(type(pattern))
print(pattern)
m = pattern.match(str)
print(type(m))
print(m)

m = pattern.match(str, 3, 10)
print(type(m))
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
