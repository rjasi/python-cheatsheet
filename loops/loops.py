


def basic_loop():
    """
    bad version

    my_items = ['a', 'b', 'c']
    i = 0
    while i < len(my_items):
        print(my_items[i])
        i += 1

    C, C++, Java style loops
    """

    my_items = ['a', 'b', 'c']
    for item in my_items:
        print(item)

def range_function():
    # range returns sequence of numbers
    list(range(5)) # [0,1,2,3,4]
    # also up to but not to the end, range(5) only went up to 4

    # range(start, stop, step)
    list(range(0,10, 2)) # start at 0, take jumps of 2 and stop at 10
    # [0, 2, 4, 6, 8]


def enumerate_loop():
    # if you need the index and element at the same time
    my_items = ['a', 'b', 'c']
    for index, value in enumerate():
        print(index, value)
