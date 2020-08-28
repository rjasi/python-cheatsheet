"""
• *args and **kwargs let you write functions with a variable
number of arguments in Python.
• *args collects extra positional arguments as a tuple. **kwargs
collects the extra keyword arguments as a dictionary.
• The actual syntax is * and ** . Calling them args and kwargs is
just a convention (and one you should stick to)
"""


def example():
    # args are extra agruments
    # kwargs are extra arguments like extra_arg=5

    def foo(required, *args, **kwargs):
        print(required)
    if args: # is a tuple
        print(args)
    if kwargs: # is a dict
        print(kwargs)

    foo("required", "arg1", "arg2", kwarg_1="kwarg_1", kwarg_2="kwarg_2")
    """
    output :

    required
    ('arg1', 'arg2')
    {'kwarg_1': 'kwarg_1', 'kwarg_2': 'kwarg_2'}

    """

def subclassing():
    class Car:
        def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage
    class AlwaysBlueCar(Car):
        def __init__(self, *args, **kwargs):
            # no need to rewrite parent's __init__
            super().__init__(*args, **kwargs)
            self.color = 'blue'

    """
    Caveats
    The downside here is that the AlwaysBlueCar constructor now has a
    rather unhelpful signature—we don’t know what arguments it expects
    without looking up the parent class.

    Typically you wouldn’t use this technique with your own class hierar-
    chies. The more likely scenario would be that you’ll want to modify or
    override behavior in some external class which you don’t control
    """
