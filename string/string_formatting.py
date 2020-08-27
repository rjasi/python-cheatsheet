"""
string formatting
"""

def old_formating():
    # the % way
    name = "bob"
    print("hi %s" % name) # okay

    # OR
    print("hi %(name)s" % {"name":name})

def new_formating():
    name = "bob"
    print("hello, {}".format(name))
    # or
    print("hello, {name}".format(name=name))

def f_strings():
    name = "bob"
    print(f"hello {name}")
    # internally becomes "hello" + name

def template_strings():
    from string import Template
    t = Template("Hey $name")
    t.substitute(name="jam")

    # a good use is for formatting user generated stuff
    SECRET = 'this-is-a-secret'
    class Error:

    def __init__(self):
        pass
    err = Error()
    user_input = '{error.__init__.__globals__[SECRET]}'
    user_input.format(error=err)  # will print the SECRET

    # safer way
    Template(user_input).substitute(error=err) # will throw error
