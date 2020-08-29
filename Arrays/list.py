"""
    list stuff
    list is implemented as a dynamic array
"""

def append():
    # simple.. add to end of list
    demo_list = [1,2,3,4,5]
    demo_list.append(6)
    # demo_list = [1, 2, 3, 4, 5, 6]

    # also
    demo_list += [7,8,9]
    # [1, 2, 3, 4, 5, 6, 7,8,9]

    # also
    demo_list[len(demo_list):] = [10,11,12]

def clear():
    # empty the list
    demo_list = [1,2,3,4,5]
    demo_list.clear()
    # demo_list = []

def copy():
    # make a copy
    demo_list = [1,2,3,4,5]
    copy_list = demo_list.copy()
    # copy_list is its own instance, not a copy of the pointer

    # alternatively
    copy_list = demo_list[:]

    # DOES NOT WORK
    copy_list = demo_list
    # copy list has the same pointer to demo_list
    # if you make a change in copy_list, demo_list will also get that change

def count():
    #  returns the number of times the specified element appears in the list
    # O(n) time complexity
    demo_list = [2,2,2,4,5]
    demo_list.count(2) # returns 3

def extend():
    # takes in an iterable
    # SIMILAR as append but not quite
    demo_list = [2,2,2,4,5]
    demo_list.extend([6,7,8])
    # demo_list = [2, 2, 2, 4, 5, 6, 7, 8]

    # extend unravles the iterable and adds vs append adds as is
    add_item = [9,0]
    demo_list.append(add_item)
    # demo_list = [2,2,2,4,5,6,7,8, [9,0]]

    # vs
    demo_list.extend(add_item)
    # demo_list = [2,2,2,4,5,6,7,8, [9,0], 9, 0]

def index():
    # returns index of an element
    # list.index(element, start, end)
    # only returns the first occurrence of the matching element
    demo_list = [1,2,3,4,5]
    demo_list.index(3) # will return 2
    demo_list.index(1,2,5) # will throw exception (1 is not in list)

def insert():
    # insert element at specific index
    #ist.insert(i, elem)
    demo_list = [1,2,3,4,5]
    demo_list.insert(2,10)
    # demo_list = [1, 2, 10, 3, 4, 5]

    # insert past the end?
    demo_list.insert(20,30)
    # demo_list = [1, 2, 10, 3, 4, 5, 30]
    # will just append to end

def pop():
    # removes the item at the given index and returns the removed item
    # list.pop(index), index is optional, if i not present, pops from end
    demo_list = [1,2,3,4,5]
    x = demo_list.pop()
    # x = 5, demo_list = [1,2,3,4]

    x = demo_list.pop(1)
    # x = 2, demo_list = [1,3,4]

    # trows exception if out of range

def remove():
    # removes first matching element
    # list.remove(elem)
    demo_list = [1,2,3,4,5]
    demo_list.remove(3)
    # demo_list = [1, 2, 4, 5]

    # raises exception if you tryto remove non existent value
    # demo_list.remove(10)

def reverse():
    # simple, reverse the list
    demo_list = [1,2,3,4,5]
    demo_list.reverse()
    # demo_list = [5, 4, 3, 2, 1]

    # alternatively

    demo_list = [1,2,3,4,5]
    demo_list = demo_list[::-1]

    # also
    demo_list = [1,2,3,4,5]
    demo_list = list(reversed(demo_list))

def sort():
    # self explanatory
    # list.sort(key=..., reverse=...) reseverse is just decending order
    # list.sort(key=len) key is a custom comparator
    demo_list = [52,3,456,44,5]
    demo_list.sort()
    # demo_list = [3, 5, 44, 52, 456]

    demo_list = ["aaa", "a", "aaaaaaa", "aa"]
    demo_list.sort(key=len)
    # demo_list = ['a', 'aa', 'aaa', 'aaaaaaa']

    # alternatively
    new_list = sorted(demo_list) # returns new list
    # sorted(list, key=..., reverse=...)

def indexing():
    demo_list = [1,2,3,4,5]

    # indexing/splicing goes as follows [start:stop:step]
    demo_list[::2]
    # returns [1, 3, 5], visited 0, 2, 4

    # easy reverse
    demo_list[::-1]

def splicing():
    demo_list = [1,2,3,4,5]
    list2 = [8,9,10,11,12]
    demo_list[0:2] + list2[1:3]
    # returns [1,2,9,10]
