"""

Dictionary stuff

"""

demo_dict = {1:"a", 2:"b", 3:"c"}

# dict.keys() method
def keys():

    # returns dict_keys([1, 2, 3])
    # keys is not an array you can't index it but you can loop through it
    # NOT OK keys[0]
    keys = demo_dict.keys()

    # OK
    for k in keys:
        print(k)

    # use list instead
    keys = list(keys)
    print(keys[0])

# dict.values() method
def values():
    # returns dict_values(['a', 'b', 'c'])
    # not array, can loop but no indexing
    # NOT OK values[0]
    values = demo_dict.values()

    # ok
    for v in values:
        print(v)

    values = list(values)
    print(values[0])

def items():
    # returns dict_items([(1, 'a'), (2, 'b'), (3, 'c')]) <- tuples
    # not array
    # NOT OK items[0]
    items = demo_dict.items()

    # preferable way to loop through dict items
    for key, value in demo_dict.items():
        # prints tuple
        print(key, ":", value)

def copy():
    # make a copy of a dict
    copied = demo_dict.copy()

    # or
    copied = dict(demo_dict)

    # DOES NOT WORK, this just copies the pointer
    bad_copy = copied
    # copied is now  {1: 'a', 2: 'b', 3: 'c'}
    bad_copy[1] = 'z'
    # copied is now {1: 'z', 2: 'b', 3: 'c'},
    # but we didn't touch copied

    # NOTE the copy is shallow i.e if you had
    # dict = {1:[1,2,3,4]}
    # the list's pointer would be copied not the list itself


def clear():
    # removes everything in the dict
    temp = dict(demo_dict)
    temp.clear()

    # prints {}
    print(temp)

def get():
    # dict.get is a safe way to get something from a dictionary

    # remember demo_dict = {1: 'a', 2: 'b', 3: 'c'}

    demo_dict[5] # will throw an exception

    result = demo_dict.get(5)
    # result is None

def fromkeys():
    # creates a new dictionary from the given sequence
    # of elements with a value provided
    keys = [1,2,3,4]
    new_dict = dict.fromkeys(keys)
    # new_dict is {1: None, 2: None, 3: None, 4: None}

    # can also supply values
    value = "a"
    new_dict = dict.fromkeys(keys, value)
    # new_dict = {1: 'a', 2: 'a', 3: 'a', 4: 'a'}

def pop():
    # removes and returns an
    # element from a dictionary having the given key
    demo_dict = {1: 'a', 2: 'b', 3: 'c'}
    result = demo_dict.pop(1)
    # result = 'a'

    # doesn't work for nonexistent keys
    # demo_dict.pop(6) throws exception

    # BUT you can supply a default value
    # Safe delete
    demo_dict.pop(100, None)
    # returns the default value too, in this case it would None

def popitem():
    #  removes and returns the (key, value) pair from the dictionary
    # in the Last In, First Out (LIFO) order
    # takes no arguments

    demo_dict = {1: 'a', 2: 'b', 3: 'c'}
    result = demo_dict.popitem()
    # result will be (3, 'c')

def setdefault():
    # returns the value of a key (if the key is in dictionary).
    # If not, it inserts key with a value to the dictionary.
    demo_dict = {1: 'a', 2: 'b', 3: 'c'}
    result = demo_dict.setdefault(1)
    # result = 'a'

    # if not exisst
    demo_dict.setdefault(4)
    # demo_dict = {1: 'a', 2: 'b', 3: 'c', 4: None}

    # can supply value
    demo_dict.setdefault(5, "z")
    # demo_dict = = {1: 'a', 2: 'b', 3: 'c', 4: None, 5:"z"}

def update():
    # insert another dict's k,v into another one
    demo_dict = {1: 'a', 2: 'b', 3: 'c'}
    temp = {4:'d', 5:'e'}

    demo_dict.update(temp)
    # demo_dict = {1: 'a', 2: 'b', 3: 'c', 4:'d', 5:'e'}

    # also overwrites the keys of the dictionary you are upating # TODO:
    temp = {1:'z'}
    demo_dict.update(temp)
    # demo_dict = {1: 'z', 2: 'b', 3: 'c', 4:'d', 5:'e'}

def dict_comprehension():
    nums = [1,2,3,4,5]
    demo_dict = {k:k*2 for k in nums }
    # demo_dict = demo_dict = {k:k*2 for k in nums }

def delete_an_item():
    # see dict.pop()
    demo_dict = {1: 'a', 2: 'b', 3: 'c'}
    # also
    del demo_dict[1]
    # demo_dict ={ 2: 'b', 3: 'c'}

    # del non existant key will throw error
    # del demo_dict[6] not ok

def hashable_keys():
    # keys of a dict must be hashable
    # hashable object means its hash value never changes
    # __hash__ <- hash code of something
    # __eq__ <- how to compare 2 different objects
    return 
