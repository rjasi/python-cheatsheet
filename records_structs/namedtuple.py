"""
similar to regular tubles
more memory efficent than classes

Good for giving your code more structure, rather than having
dynamic data structures like dicts that implicitly have structure to them

i.e if you have dict {"x1": 1, "x2":2} and the keys, vals never change its
much better to use a named tuple
"""

from collections import namedtuple

def example():
    p1 = namedtuple('Point', 'x y z')(1, 2, 3)
    p1 # Point(x=1, y=2, z=3)

def example2():
    Tup = namedtuple('example_tuple', 'field1 field2 field3') # space between fields
    t1 = Tup(1,2,3)
    t1  # example_tuple(field1=1, field2=2, field3=3)
