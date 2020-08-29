"""
 Returns a default value if a key does not exist
"""

from collections import defaultdict

def example():
    # takes the default value in the constructor
    # constructor must be callable
    dd = defaultdict(lambda : 0)
    # or
    def default():
        return 0
    dd = defaultdict(default)

    print(dd[4854]) # prints 0

    # default val can be anything
    dd = defaultdict(list)
    print(dd[1234]) # prints empty list []
