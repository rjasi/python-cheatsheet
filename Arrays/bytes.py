"""
immutable array of ints in the range 0 <= x <= 255
similar to strings but for ints
"""


def example():
    arr = bytes((0, 1, 2, 3)) # must wrap values in another array
    arr # b'\x00\x01\x02\x03'
    arr[0] = 2 # error, immutable
    
    arr = bytes([0, 1, 265, 3]) # error ValueError: bytes must be in range(0, 256)
