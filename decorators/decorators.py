"""
    Decorators define reusable building blocks you can apply to a
    callable to modify its behavior without permanently modifying
    the callable itself.
"""

def most_basic_decorator():


    def basic_decorator(func):
        return func

    def greet():
        return "hello"

    greet = basic_decorator(greet)
    greet() # returns hello

    # alternatively
    @basic_decorator
    def greet():
        return "hello"

def upper_case_decorator():
    def uppercase(func):
        def wrapper():
            original_res = func()
            modified_result = original_res.upper()
            return modified_result
        return wrapper

    @uppercase
    def greet():
        return "hello"

    greet() # outputs HELLO

    # why wrapper? why not just do this?
    def uppercase(func):
        original_res = func()
        modified_result = original_res.upper()
        return modified_result
    @uppercase
    def greet():
        return "hello"

    greet # greet is actually a string now. No longer a function.
    greet() # syntax error, greet is not callable since its a string now
    # you need to return the wrapper function

def multiple_decorators():
    # decorators are applied from botton to top
    # aka decorator stacking

    def strong(func):
        def wrapper():
            return '<strong>' + func() + '</strong>'
        return wrapper

    def emphasis(func):
        def wrapper():
            return '<em>' + func() + '</em>'
        return wrapper

    @strong # last executed
    @emphasis # first executed
    def greet():
        return "hello"

    greet() # returns '<strong><em>Hello!</em></strong>'

def arguments_to_decorators():
    # use *args and **kwargs
    def proxy(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

def debuggable_decorators():
    # meta data is lost when decorating

    def uppercase(func):
        @functools.wraps(func) # copies func meta_data like doc string to uppercase decorator 
        def wrapper():
            return func().upper()
    return wrapper
