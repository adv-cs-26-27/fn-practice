"""
Warmup-1: Simple warmup problems, no loops necessary!
"""

def sleep_in(weekday, vacation):
    # Instructions: You are on vacation from school, and you get to sleep
    # in if it is not a weekday, or if it is a weekday but you are also
    # on vacation. Given two boolean values, weekday and vacation, return
    # True if you get to sleep in.
    pass  # TODO: implement


def test_sleep_in():
    assert sleep_in(False, False) == True
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True
    assert sleep_in(True, True) == True
    print("all sleep_in tests passed!")

# don't forget to CALL the test functions :--)

def monkey_trouble(a_smile, b_smile):
    # Instructions: Two monkeys, a and b, are always in trouble together,
    # or always out of trouble together -- there is trouble exactly when
    # both are smiling or both are not smiling. Given two boolean values,
    # a_smile and b_smile, return True if there is trouble.
    pass  # TODO: implement


def test_monkey_trouble():
    assert monkey_trouble(True, True) == True
    assert monkey_trouble(False, False) == True
    assert monkey_trouble(True, False) == False
    assert monkey_trouble(False, True) == False
    print("all monkey_trouble tests passed!")


def sum_double(a, b):
    # Instructions: Given two int values, return their sum. Unless the
    # two values are the same, in which case return double their sum.
    pass  # TODO: implement


def test_sum_double():
    assert sum_double(1, 2) == 3
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8
    assert sum_double(-1, -1) == -4
    assert sum_double(0, 0) == 0
    assert sum_double(5, -5) == 0
    assert sum_double(10, 10) == 40
    print("all sum_double tests passed!")


def diff21(n):
    # Instructions: Given an int n, return the absolute difference
    # between n and 21, except return double that difference if n is
    # over 21.
    pass  # TODO: implement


def test_diff21():
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0
    assert diff21(22) == 2
    assert diff21(25) == 8
    assert diff21(0) == 21
    assert diff21(50) == 58
    assert diff21(20) == 1
    print("all diff21 tests passed!")


def parrot_trouble(talking, hour):
    # Instructions: We have a loud talking parrot. The "hour" parameter
    # is the current hour time in the range 0..23. We are in trouble if
    # the parrot is talking and the hour is before 7 or after 20. Given
    # a boolean talking and an int hour, return True if there is trouble.
    pass  # TODO: implement


def test_parrot_trouble():
    assert parrot_trouble(True, 6) == True
    assert parrot_trouble(True, 7) == False
    assert parrot_trouble(False, 6) == False
    assert parrot_trouble(True, 21) == True
    assert parrot_trouble(True, 20) == False
    assert parrot_trouble(True, 0) == True
    assert parrot_trouble(False, 22) == False
    assert parrot_trouble(True, 12) == False
    print("all parrot_trouble tests passed!")


def makes10(a, b):
    # Instructions: Given two int values, return True if either one is
    # 10, or if their sum is 10.
    pass  # TODO: implement


def test_makes10():
    assert makes10(9, 10) == True
    assert makes10(9, 9) == False
    assert makes10(1, 9) == True
    assert makes10(10, 0) == True
    assert makes10(5, 5) == True
    assert makes10(0, 0) == False
    assert makes10(3, 7) == True
    assert makes10(10, 10) == True
    print("all makes10 tests passed!")


def near_hundred(n):
    # Instructions: Given an int n, return True if it is within 10 of
    # 100 or 200. (Note: abs(num) computes the absolute value of a
    # number.)
    pass  # TODO: implement


def test_near_hundred():
    assert near_hundred(93) == True
    assert near_hundred(90) == True
    assert near_hundred(89) == False
    assert near_hundred(205) == True
    assert near_hundred(211) == False
    assert near_hundred(100) == True
    assert near_hundred(110) == True
    assert near_hundred(0) == False
    assert near_hundred(200) == True
    assert near_hundred(190) == True
    print("all near_hundred tests passed!")


def pos_neg(a, b, negative):
    # Instructions: Given two int values, return True if one is negative
    # and the other is positive. Except if the parameter "negative" is
    # True, in which case return True only if both values are negative.
    pass  # TODO: implement


def test_pos_neg():
    assert pos_neg(1, -1, False) == True
    assert pos_neg(-1, 1, False) == True
    assert pos_neg(-4, -5, True) == True
    assert pos_neg(-4, -5, False) == False
    assert pos_neg(4, 5, False) == False
    assert pos_neg(4, -5, True) == False
    assert pos_neg(0, -1, False) == False
    assert pos_neg(-1, 0, False) == False
    print("all pos_neg tests passed!")


def not_string(s):
    # Instructions: Given a string, return a new string where "not " has
    # been added to the front. However, if the string already begins
    # with "not", return the string unchanged.
    pass  # TODO: implement


def test_not_string():
    assert not_string("candy") == "not candy"
    assert not_string("x") == "not x"
    assert not_string("not bad") == "not bad"
    assert not_string("") == "not "
    assert not_string("not") == "not not"
    assert not_string("NOT bad") == "not NOT bad"
    print("all not_string tests passed!")


def missing_char(s, n):
    # Instructions: Given a string and an index n, return a new string
    # with the character at index n removed. The value of n will be a
    # valid index of a character in the string (i.e. n will be in the
    # range 0..len(str)-1 inclusive).
    pass  # TODO: implement


def test_missing_char():
    assert missing_char("kitten", 1) == "ktten"
    assert missing_char("kitten", 0) == "itten"
    assert missing_char("kitten", 4) == "kittn"
    assert missing_char("kitten", 5) == "kitte"
    assert missing_char("a", 0) == ""
    print("all missing_char tests passed!")


def front_back(s):
    # Instructions: Given a string, return a new string where the first
    # and last characters have swapped places.
    pass  # TODO: implement


def test_front_back():
    assert front_back("code") == "eodc"
    assert front_back("a") == "a"
    assert front_back("ab") == "ba"
    assert front_back("") == ""
    assert front_back("abc") == "cba"
    print("all front_back tests passed!")


def front3(s):
    # Instructions: Given a string, return a new string made of its
    # first 3 characters repeated three times. If the string is shorter
    # than 3 characters, use whatever characters are available.
    pass  # TODO: implement


def test_front3():
    assert front3("Java") == "JavJavJav"
    assert front3("Chocolate") == "ChoChoCho"
    assert front3("abc") == "abcabcabc"
    assert front3("ab") == "ababab"
    assert front3("") == ""
    assert front3("a") == "aaa"
    print("all front3 tests passed!")
