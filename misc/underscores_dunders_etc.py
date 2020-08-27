"""
 underscores or douple underscores meaning

 Types:
 single leading _var
 single trailing var_
 double leading __var
 dbl trailing and leading __var__
 single underscores: _
"""


def single_leading():
    # has no real meaning to the compliler for variables
    # more as a convention

    # defined by PEP 8
    # means this variable is for internal use
    _num = 5

    # But does change for importing
    # lets say you have this module
    def _my_function():
        return 5

    # if you import your module using * i.e import * from module, it will ignore
    # _my_function
    # above behaviour can be overidden if you define an __all__ in the module

def single_trailing():
    # just for using names taken by a keyword in python
    # i.e

    def foo(class): # fails
        pass
    def foo(class_): # okay
        pass

def double_leading():
    # used for name mangling
    # to avoid naming conflicts in subclasses
    class Test:
        def __init__(self):
            self.foo = 1
            self._bar = 2
            self.__baz = 3

        def get_mangled(self):
            return self.__baz

        # also becomes _Test_mangled_function
        def __mangled_function(self):
            pass

    t = Test()
    dir(t)
    """
    __baz becomes _Test__baz , everything else stays the same
    """
    t.__baz # fails: 'Test' object has no attribute '__baz'

    t.get_mangled() # okay

    # interesting hack
    _MangledGlobal__mangled = 23
    class MangledGlobal:
        def test(self):
            return __mangled

    MangledGlobal().test() # returns 23 because mangling appends the name of the class _MangledGlobal to __mangled

def dunders():
    # dunder just means double underscores
    # __baz = dunder baz
    pass

def double_leading_trailing():
    # name mangling not applied for __var__
    # reserved for special use in language
    # TODO get more info
    pass

def single_underscore():
    # name like _

    # _ just means not needed 
    for i, _ in enumerate([1,2,35]):
        print("hi",  i)
