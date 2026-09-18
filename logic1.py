"""
Logic-1: Basic boolean logic puzzles -- if/elif/else, and/or/not.
"""

def date_fashion(you, date):
    # Instructions: You and your date are trying to get into a
    # restaurant, where each of you has a fashion rating. If either
    # rating is 8 or more, you get in regardless of the other rating,
    # so return 2. Otherwise, if either rating is 2 or less, you do not
    # get in, so return 0. In all other cases, return 1.
    pass  # TODO: implement


def test_date_fashion():
    assert date_fashion(5, 10) == 2
    assert date_fashion(5, 2) == 0
    assert date_fashion(5, 5) == 1
    assert date_fashion(2, 2) == 0
    assert date_fashion(9, 1) == 2
    assert date_fashion(8, 8) == 2
    assert date_fashion(3, 3) == 1
    assert date_fashion(2, 9) == 2
    print("all date_fashion tests passed!")

# don't forget to CALL the test functions :--)

def squirrel_play(temp, is_summer):
    # Instructions: Squirrels play outside when the temperature is
    # between 60 and 90 degrees, inclusive. Unless it is summer, in
    # which case the upper limit is 100 instead of 90. Given an int
    # temp and a boolean is_summer, return True if the squirrels play.
    pass  # TODO: implement


def test_squirrel_play():
    assert squirrel_play(70, False) == True
    assert squirrel_play(95, False) == False
    assert squirrel_play(95, True) == True
    assert squirrel_play(59, False) == False
    assert squirrel_play(100, True) == True
    assert squirrel_play(101, True) == False
    assert squirrel_play(90, False) == True
    assert squirrel_play(91, False) == False
    assert squirrel_play(60, True) == True
    print("all squirrel_play tests passed!")


def caught_speeding(speed, is_birthday):
    # Instructions: A police officer catches you speeding. Return an
    # int result encoding the outcome: 0 for no ticket, 1 for a small
    # ticket, and 2 for a big ticket. If speed is 60 or below, return 0.
    # If speed is between 61 and 80 inclusive, return 1. If speed is 81
    # or above, return 2. Unless it is your birthday, in which case your
    # speed is treated as 5 mph lower for all of the above checks.
    pass  # TODO: implement


def test_caught_speeding():
    assert caught_speeding(60, False) == 0
    assert caught_speeding(65, False) == 1
    assert caught_speeding(80, False) == 1
    assert caught_speeding(85, False) == 2
    assert caught_speeding(90, True) == 2
    assert caught_speeding(65, True) == 0
    assert caught_speeding(81, True) == 1
    assert caught_speeding(86, True) == 2
    print("all caught_speeding tests passed!")


def sorta_sum(a, b):
    # Instructions: Given two int values, return their sum. However,
    # sums in the range 10 to 19 inclusive are forbidden, so in that
    # case return 20 instead.
    pass  # TODO: implement


def test_sorta_sum():
    assert sorta_sum(3, 4) == 7
    assert sorta_sum(9, 4) == 20
    assert sorta_sum(10, 11) == 21
    assert sorta_sum(1, 8) == 9
    assert sorta_sum(1, 9) == 20
    assert sorta_sum(9, 10) == 20
    assert sorta_sum(9, 9) == 20
    assert sorta_sum(0, 0) == 0
    print("all sorta_sum tests passed!")


def alarm_clock(day, vacation):
    # Instructions: Given a day of the week encoded as an int (0=Sunday,
    # 1=Monday, ..., 6=Saturday) and a boolean vacation flag, return a
    # string giving the time the alarm clock should be set to. On
    # weekdays the alarm is "7:00", and on weekends it is "10:00" --
    # unless it is vacation, in which case weekdays become "10:00" and
    # weekends become "off".
    pass  # TODO: implement


def test_alarm_clock():
    assert alarm_clock(1, False) == "7:00"
    assert alarm_clock(5, False) == "7:00"
    assert alarm_clock(0, False) == "10:00"
    assert alarm_clock(6, False) == "10:00"
    assert alarm_clock(3, True) == "10:00"
    assert alarm_clock(0, True) == "off"
    assert alarm_clock(6, True) == "off"
    assert alarm_clock(1, True) == "10:00"
    print("all alarm_clock tests passed!")


def love6(a, b):
    # Instructions: The number 6 is a great number. Given two int
    # values, a and b, return True if either one of them is 6, or if
    # their sum or their difference is 6.
    pass  # TODO: implement


def test_love6():
    assert love6(6, 4) == True
    assert love6(4, 5) == False
    assert love6(1, 5) == True
    assert love6(-2, 8) == True
    assert love6(6, 6) == True
    assert love6(10, 4) == True
    assert love6(3, 3) == True
    assert love6(2, 2) == False
    print("all love6 tests passed!")


def in1to10(n, outside_mode):
    # Instructions: Given an int n, return True if n is in the range 1
    # to 10, inclusive. Unless outside_mode is True, in which case
    # return True if n is less than or equal to 1, or greater than or
    # equal to 10.
    pass  # TODO: implement


def test_in1to10():
    assert in1to10(5, False) == True
    assert in1to10(11, False) == False
    assert in1to10(11, True) == True
    assert in1to10(0, True) == True
    assert in1to10(1, False) == True
    assert in1to10(10, False) == True
    assert in1to10(1, True) == True
    assert in1to10(10, True) == True
    assert in1to10(5, True) == False
    print("all in1to10 tests passed!")


def near_ten(num):
    # Instructions: Given a non-negative int num, return True if num is
    # within 2 of a multiple of 10.
    pass  # TODO: implement


def test_near_ten():
    assert near_ten(12) == True
    assert near_ten(17) == False
    assert near_ten(19) == True
    assert near_ten(9) == True
    assert near_ten(4) == False
    assert near_ten(0) == True
    assert near_ten(2) == True
    assert near_ten(3) == False
    assert near_ten(20) == True
    assert near_ten(28) == True
    print("all near_ten tests passed!")
