"""
same as list but immutable
Whatever is in a tuple is defined during creating time
"""


def example():
    tup = 1, 2, 3
    tup # (1, 2, 30)

    # defined by circle braces
    tup = ('a', 1, 2)
    tup # ('a', 1, 2)

    # access like an array
    tup[0] # 'a'

    # cannot modify
    tup[0] = 5 # error "'tuple' object does not support item assignment"
