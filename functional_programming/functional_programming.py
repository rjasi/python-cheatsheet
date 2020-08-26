"""
functional programming stuff like lambdas

Note python lambda as just syntatic sugar
(they are eventually turned into regular functions by the compiler )
but a lazily evaled
src: https://realpython.com/python-lambda/

"""

def python_lambdas():
    # nothing special, want a function but too lazy or don't like the
    # extra bloat? Use lambdas aka anonymous functions

    # format is lambda paramters : function body

    # traditional function
    def add_one(x):
        # function takes an int and returns int + 1
        return x + 1

    # lambda versions
    add_one_lambda = lambda x : x + 1
    add_one_lambda(1) # returns 2

    # default args
    (lambda x, y, z=3: x + y + z)(1, 2)

    # expand list args
    (lambda *args: sum(args))(1,2,3)

def lambdas_in_list_comprehensions()
    # lets double all values in a list
    nums = [1,2,3,4,5]

    # wrap brackets around the lambda for closure
    new_nums = [(lambda x: x * 2)(x) for x in nums ]
    # new_nums = [2, 4, 6, 8, 10]

    # can do [x * 2 for x in nums ] as well ...

def curry_functions():
    # lambdas are lazily eval'd, meaning it is evaluated when you need it
    # currying just means you pass paramters to the final function in a chain

    """
    we want the follow code to raise 10 to the power of 0,1,2,3, and 4
    nums = [lambda x : x ** i for i in range(5)]
    [nums[j](10) for j in range(5)]

    """
    nums = [lambda x : x ** i for i in range(5)]

    # lambda x : x ** i is actually lambda x : x ** 4  for ALL
    [nums[j](10) for j in range(5)]

    # you get [10000,10000,10000,10000,10000]. WRONG!

    # better way using lambdas
    nums = [(lambda y : lambda x : x ** y)(i)  for i in range(5)]

    """
        # (lambda y : lambda x : x ** y)(i) translates to

        def outer(y):
            def inner(x):
                return x ** y
            return inner
    """

def lambda_donts():
    # No statements in lambdas
    # return, pass, assert, or raise will raise a SyntaxError exception.
    # (lambda x: assert x == 2)(2) BAD

    # no exceptions in lambdas too
    """
        >>> def throw(ex): raise ex
        >>> (lambda: throw(Exception('Something bad happened')))()
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            File "<stdin>", line 1, in <lambda>
            File "<stdin>", line 1, in throw
        Exception: Something bad happened
    """
    #
    return

def closures():
    #todo
    return 
