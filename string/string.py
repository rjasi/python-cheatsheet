"""
strings aka char arrays

Strings are recursive data structures
"""


def immutable():
    # strings are immutable in python
    s = "abcdef"
    s[0] = 'g' # raises error 'str' object does not support item assignment


    # to change it just make it into list then convert back to str
    l = list(s)
    l[0] = 'g'
    s = "".join(l)
    s # 'gbcdef'
