"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""


def char_check(s: str):
    letters = space = digit = others = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    return letters, space, digit, others


s = "hello world @@#$1"
print('char = {},space = {},digit = {},others = {}'.format(*char_check(s)))
