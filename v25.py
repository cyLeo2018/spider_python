import re


if __name__ == '__main__':
    str = "one12two34three56"
    s = r'\d+'
    pattern = re.compile(s)
    m = pattern.match(str)
    print(m.group())

    m = pattern.search(str, 10, 40)
    print(m.group())