"""

information from dan bader
Summary:
1. assert is good for debugging
2. don't use to handle run time errors
3. can be globally disabled

"""


def example():
    one = 1
    two = 2
    assert one == two # raise error

def example2():
    # can pass a message
    one = 1
    two = 2
    assert one == two, "One is not equal to two"

def caveat1():
    """
    You can turn off assertions rendering all assets in your code useless

    quote: assertions can be globally disabled 3 with the -O and -OO command line switches, as
    well as the PYTHONOPTIMIZE environment variable in CPython

    So don't use it in production
    """

    return

def caveat2():
    """
    Assertions can never fail

    passing in tuples as first arg to assert always evals to true
    """

    assert(1 == 2, 'This should fail') # never fails, it is treating (1 == 2, 'This should fail') as a tuple
    # multiline
    assert(
        1 == 2,
        "This should fail"
    ) # will always eval to true
