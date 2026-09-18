"""
Logic-2: Medium boolean logic puzzles -- if/elif/else, and/or/not.
"""

def make_bricks(small, big, goal):
    # Instructions: We want to build a row of bricks that is exactly
    # goal inches long, using small bricks (1 inch each) and big
    # bricks (5 inches each). Given counts of small and big bricks and
    # a target length goal, return True if it is possible to reach
    # that exact length using some combination of the bricks on hand.
    pass  # TODO: implement


def test_make_bricks():
    assert make_bricks(3, 1, 8) == True
    assert make_bricks(3, 1, 9) == False
    assert make_bricks(3, 2, 10) == True
    assert make_bricks(0, 0, 0) == True
    assert make_bricks(0, 0, 1) == False
    assert make_bricks(9, 1, 7) == True
    assert make_bricks(0, 3, 7) == False
    assert make_bricks(2, 2, 16) == False
    print("all make_bricks tests passed!")

# don't forget to CALL the test functions :--)

def lone_sum(a, b, c):
    # Instructions: Given three int values, a, b, and c, return their
    # sum. However, if any one of the values equals another of the
    # values, that repeated value does not count toward the sum. If
    # all three are equal, the result is 0.
    pass  # TODO: implement


def test_lone_sum():
    assert lone_sum(1, 2, 3) == 6
    assert lone_sum(3, 2, 3) == 2
    assert lone_sum(3, 3, 3) == 0
    assert lone_sum(5, 5, 7) == 7
    assert lone_sum(1, 2, 1) == 2
    print("all lone_sum tests passed!")


def lucky_sum(a, b, c):
    # Instructions: Given three int values, a, b, and c, return their
    # sum. However, if one of the values is 13, it does not count
    # toward the sum, and neither do any of the values to its right
    # (b and c are considered to be to the right of a; c is to the
    # right of b).
    pass  # TODO: implement


def test_lucky_sum():
    assert lucky_sum(1, 2, 3) == 6
    assert lucky_sum(1, 2, 13) == 3
    assert lucky_sum(1, 13, 3) == 1
    assert lucky_sum(13, 1, 3) == 0
    assert lucky_sum(13, 13, 13) == 0
    print("all lucky_sum tests passed!")


def no_teen_sum(a, b, c):
    # Instructions: Given three int values, a, b, and c, return their
    # sum. However, any value that is a "teen" -- in the range 13 to
    # 19 inclusive -- counts as 0 toward the sum, except that 15 and
    # 16 are not affected by this rule and count normally. Implement a
    # separate helper function fix_teen(n) that applies this rule to a
    # single value, and call it once for each of a, b, and c.
    pass  # TODO: implement


def fix_teen(n):
    pass  # TODO: implement


def test_no_teen_sum():
    assert no_teen_sum(1, 2, 3) == 6
    assert no_teen_sum(2, 13, 1) == 3
    assert no_teen_sum(2, 1, 14) == 3
    assert no_teen_sum(2, 1, 15) == 18
    assert no_teen_sum(2, 1, 16) == 19
    assert no_teen_sum(19, 19, 19) == 0
    print("all no_teen_sum tests passed!")


def round_sum(a, b, c):
    # Instructions: Given three int values, a, b, and c, round each one
    # to the nearest multiple of 10 and return the sum of the rounded
    # values. A value rounds up if its rightmost digit is 5 or more,
    # and rounds down otherwise. Implement a separate helper function
    # round10(num) that rounds a single value, and call it once for
    # each of a, b, and c.
    pass  # TODO: implement


def round10(num):
    pass  # TODO: implement


def test_round_sum():
    assert round_sum(16, 17, 18) == 60
    assert round_sum(12, 13, 14) == 30
    assert round_sum(6, 4, 4) == 10
    assert round_sum(0, 0, 0) == 0
    assert round_sum(5, 5, 5) == 30
    print("all round_sum tests passed!")


def close_far(a, b, c):
    # Instructions: Given three int values, a, b, and c, return True if
    # one of b or c is "close" to a (differs from a by 1 or less),
    # while the other one is "far" from both a and the close value
    # (differs from each of them by 2 or more).
    pass  # TODO: implement


def test_close_far():
    assert close_far(1, 2, 10) == True
    assert close_far(1, 2, 3) == False
    assert close_far(4, 1, 3) == True
    assert close_far(1, 5, 5) == False
    assert close_far(0, 1, 10) == True
    print("all close_far tests passed!")


def make_chocolate(small, big, goal):
    # Instructions: We want to make a package of exactly goal kilos of
    # chocolate using small bars (1 kilo each) and big bars (5 kilos
    # each). Assuming we always use as many big bars as we can without
    # going over the goal, return the number of small bars needed to
    # make up the rest. Return -1 if it is not possible to reach the
    # goal exactly with the small bars available.
    pass  # TODO: implement


def test_make_chocolate():
    assert make_chocolate(4, 1, 9) == 4
    assert make_chocolate(4, 1, 10) == -1
    assert make_chocolate(4, 1, 7) == 2
    assert make_chocolate(0, 0, 0) == 0
    assert make_chocolate(0, 1, 4) == -1
    assert make_chocolate(5, 2, 9) == 4
    print("all make_chocolate tests passed!")
