"""
with is useful for resource management
"""

def example():
    with open('text.txt', 'w') as f:
        f.write('hi')

    # no need to manage closing file
    """
    The code is internally translated to:

    f = open('test.txt', 'w')
    try:
        f.write('hid')
    finally:
        f.close()
    """

def example2():
    # locks
    some_lock = threading.Lock()
    some_lock.acquire()
    try:
        # do things
        print()
    finally:
        some_lock.release()

    # better way:
    with some_lock:
        # do things
        print()

def make_your_own_custom_context_manager():
    # example from Dan Bader - Python Tricks
    class ManagedFile:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            self.file = open(self.name, 'w')
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()

    # to use
    with ManagedFile('file.txt') as f:
        f.write("hg")

def use_contextlib_factory():
    # decorator
    from contextlib import contextmanager
    @contextmanager
    def managed_file(name):
        try:
            f = open(name, 'w')
            yield f
        finally:
            f.close()

    # to use :
    with managed_file("file.txt") as f:
        f.write("e")

def indenter_example():
    class Indenter():
        def __init__(self):
            self.indent = []
        def __enter__(self):
            self.indent.append("\t")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.indent:
                self.indent.pop()

        def print(self, word):
            print("".join(self.indent), word)

    with Indenter() as indent:
        indent.print('hi!')
        with indent:
            indent.print('hello')
            with indent:
                indent.print('bonjour')
        indent.print('hey')

def time_example():
    # TODO use with time to measure time it look to execute things
    return 
