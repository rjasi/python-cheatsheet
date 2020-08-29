"""
Read only dicts
"""

from types import MappingProxyType

def example():
    regular_dict = {"one": 1, "two":2}
    read_only = MappingProxyType(regular_dict)
    read_only["one"] = 5 # throws error TypeError: 'mappingproxy' object does not support item assignment
