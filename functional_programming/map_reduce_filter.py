"""
map, reduce and filter are staples in all
functional programming languages
"""


def map_function():
    # use to apply a function to all items in an iterable

    # list example
    words = ["Hello", "Python", "Red"]
    words = list(map(str.upper, words)) # returns map object, conver to list
    # results is words = ['HELLO', 'PYTHON', 'RED']

    # pass args to map

    def add_x(x, add_val):
        return x + add_val
    nums = [1,2,3]

    # note must supply a val for each item in nums
    nums = list(map(add_x, nums, [5]*len(nums)))
    # nums [6,7,8]

    # forget to supply a val, just ignores rest
    nums = list(map(add_x, nums, [5,5]))
    # nums = [6,7]

def filter_function():
    # self explanatory
    nums = [1,2,3,4,5,6]

    # function must return true or false
    def is_even(x):
        return x%2 == 0
    nums = list(filter(is_even, nums))
    # nums = [2, 4, 6]

def reduce_function():
    # applies functions between 2 elements in a list cumulatively
    from functools import reduce

    def concat(x, y):
        return x + y

    words = ["Hello", "Python", "Red"]
    word = (reduce(concat, words, ""))
    word
    # word = "HelloPythonRed"

    # what happened was concat(concat("Hello", "Python"), "Red")
