"""
Same as regular dict but order of keys are preserved in insertion order
"""

from collections import OrderedDict


def example():
    d = OrderedDict(b=3, a=5, z=6)
    d.keys() # odict_keys(['b', 'a', 'z'])
