"""
All functions in python are first class objects

"""


def object_as_function():
    # You can make an object work like a function
    class Adder:
        def __init__(self, n):
            self.n = n

        def __call__(self, x): # note __call__ dunder function
            return self.n + x

    add_3 = Adder(3)
    print(add_3(5)) # returns 8

    # check callable
    callable(add_3) # True
    callable(5) # False
