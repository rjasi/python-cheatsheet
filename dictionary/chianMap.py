"""
 combines multiple dicts into 1 , but still keeps dicts seperate

 sounds pointless because you can just merge 2 dicts together but
 the advantage is that ChainMap is much more efficient at merging

 querying is O(n) time so it sucks for that

 https://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap
"""

from collections import ChainMap


def example():
    d1 = {'one':1, 'two':2}
    d2 = {'three':3, 'four':4}
    chain = ChainMap(d1, d2)
    chain # ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
    # query only finds first occurrence

    # i.e
    d1 = {'one':1, 'two':2}
    d2 = {'one':3, 'four':4}
    chain = ChainMap(d1, d2)
    chain['one'] # returns 1 not 3
