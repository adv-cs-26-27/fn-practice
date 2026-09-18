"""
List-1: Basic list problems, no loops necessary!
    > use a[0], a[1], ... to access elements in a list
    > len(a) is the length
"""


def first_last6(nums):
    # Instructions: Given a list of ints, return True if 6 appears as
    # either the first or last element in the list. The list will have
    # length 1 or more.
    pass  # TODO: implement


def test_first_last6():
    assert first_last6([1, 2, 6]) == True
    assert first_last6([6, 1, 2, 3]) == True
    assert first_last6([13, 6, 1, 2, 3]) == False
    assert first_last6([6]) == True
    assert first_last6([1, 2, 3]) == False
    print("all first_last6 tests passed!")


def same_first_last(nums):
    # Instructions: Given a list of ints, return True if the list has
    # length 1 or more and its first element is equal to its last
    # element.
    pass  # TODO: implement


def test_same_first_last():
    assert same_first_last([1, 2, 3]) == False
    assert same_first_last([1, 2, 3, 1]) == True
    assert same_first_last([1, 2, 1]) == True
    assert same_first_last([5]) == True
    assert same_first_last([1, 2]) == False
    print("all same_first_last tests passed!")


def common_end(a, b):
    # Instructions: Given two lists of ints, a and b, return True if
    # they have the same first element or the same last element. Both
    # lists will have length 1 or more.
    pass  # TODO: implement


def test_common_end():
    assert common_end([1, 2, 3], [7, 3]) == True
    assert common_end([1, 2, 3], [7, 3, 2]) == False
    assert common_end([1, 2, 3], [1, 3]) == True
    assert common_end([5], [5]) == True
    assert common_end([1, 2, 3], [4, 5, 6]) == False
    print("all common_end tests passed!")


def sum3(nums):
    # Instructions: Given a list of ints of length 3, return the sum of
    # all the elements.
    pass  # TODO: implement


def test_sum3():
    assert sum3([1, 2, 3]) == 6
    assert sum3([5, 11, 2]) == 18
    assert sum3([7, 0, 0]) == 7
    assert sum3([-1, -2, -3]) == -6
    print("all sum3 tests passed!")


def rotate_left3(nums):
    # Instructions: Given a list of ints of length 3, return a new list
    # with the elements "rotated left", so {1, 2, 3} yields {2, 3, 1}.
    pass  # TODO: implement


def test_rotate_left3():
    assert rotate_left3([1, 2, 3]) == [2, 3, 1]
    assert rotate_left3([5, 11, 9]) == [11, 9, 5]
    assert rotate_left3([7, 0, 0]) == [0, 0, 7]
    print("all rotate_left3 tests passed!")


def reverse3(nums):
    # Instructions: Given a list of ints of length 3, return a new list
    # with the elements in reverse order, so {1, 2, 3} becomes
    # {3, 2, 1}.
    pass  # TODO: implement


def test_reverse3():
    assert reverse3([1, 2, 3]) == [3, 2, 1]
    assert reverse3([5, 11, 9]) == [9, 11, 5]
    assert reverse3([7, 0, 0]) == [0, 0, 7]
    print("all reverse3 tests passed!")


def max_end3(nums):
    # Instructions: Given a list of ints of length 3, figure out which
    # is larger between the first and last elements, and return a new
    # list of length 3 where every element has been set to that larger
    # value.
    pass  # TODO: implement


def test_max_end3():
    assert max_end3([1, 2, 3]) == [3, 3, 3]
    assert max_end3([11, 5, 9]) == [11, 11, 11]
    assert max_end3([2, 11, 3]) == [3, 3, 3]
    assert max_end3([5, 5, 5]) == [5, 5, 5]
    print("all max_end3 tests passed!")


def sum2(nums):
    # Instructions: Given a list of ints, return the sum of the first 2
    # elements in the list. If the list has fewer than 2 elements, sum
    # whatever elements are present (an empty list sums to 0).
    pass  # TODO: implement


def test_sum2():
    assert sum2([1, 2, 3]) == 3
    assert sum2([1, 1]) == 2
    assert sum2([1, 1, 1, 1]) == 2
    assert sum2([5]) == 5
    assert sum2([]) == 0
    print("all sum2 tests passed!")


def middle_way(a, b):
    # Instructions: Given two int lists, a and b, each of length 3,
    # return a new list of length 2 containing their middle elements.
    pass  # TODO: implement


def test_middle_way():
    assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
    assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
    assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]
    print("all middle_way tests passed!")


def make_ends(nums):
    # Instructions: Given a list of ints, return a new list of length 2
    # containing the first and last elements from the original list.
    # The original list will have length 1 or more.
    pass  # TODO: implement


def test_make_ends():
    assert make_ends([1, 2, 3]) == [1, 3]
    assert make_ends([1, 2, 3, 4]) == [1, 4]
    assert make_ends([7, 4, 6, 2]) == [7, 2]
    assert make_ends([5]) == [5, 5]
    print("all make_ends tests passed!")


def has23(nums):
    # Instructions: Given an int list of length 2, return True if it
    # contains a 2 or a 3.
    pass  # TODO: implement


def test_has23():
    assert has23([2, 5]) == True
    assert has23([4, 3]) == True
    assert has23([4, 5]) == False
    assert has23([3, 2]) == True
    print("all has23 tests passed!")