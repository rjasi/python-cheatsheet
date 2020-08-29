"""
create lists, dicts, sets easily
"""


def example():
    nums = [x for x in range(5)] # [0,1,2,3,4]

def conditionals():
    nums = [x for x in range(10) if x % 3 == 0] # [0,3,6,9]

def multidimensional():
    matrix = [[0,1,2,3], [0,1,2,3], [0,1,2,3]]
    nums = [y for x in matrix for y in x ]

    """
    translates to:
    nums = []
    for x in matrix:
        for y in x:
            nums.append(y)
    """

def multidimensional_conditionals():
    matrix = [[1,2,3,4], [0,1,3], [6,8,9,14]]
    nums = [y for x in matrix if len(x) == 4 for y in x if y % 2 == 0]

    """
    translates to:
    nums = []
    for x in matrix:
        if len(x) != 4:
            continue
        for y in x:
            if y % 2 == 0:
                nums.append(y)
    """

def set_comprehension():
    nums = [abs(x) for x in range(-10, 5)] # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    nums = {abs(x) for x in range(-10, 5)} #  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def dict_comprehension():
    # note x:x *x 
    nums = { x: x * x for x in range(5) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
