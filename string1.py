"""
String-1: Basic string problems -- no loops.
    > use + to combine strings
    > len(str) is the number of chars in a string
    > str[i:j] extracts the substring starting at 
      index i and running up to but not including index j
"""


def hello_name(name):
    # Instructions: Given a string name, return a greeting of the form
    # "Hello <name>!".
    pass  # TODO: implement


def test_hello_name():
    assert hello_name("Bob") == "Hello Bob!"
    assert hello_name("Alice") == "Hello Alice!"
    assert hello_name("") == "Hello !"
    assert hello_name("X") == "Hello X!"
    print("all hello_name tests passed!")


def make_abba(a, b):
    # Instructions: Given two strings, a and b, return a new string made
    # by concatenating them in the pattern a-b-b-a, so "Hi" and "Bye"
    # yields "HiByeByeHi".
    pass  # TODO: implement


def test_make_abba():
    assert make_abba("Hi", "Bye") == "HiByeByeHi"
    assert make_abba("Yo", "Alice") == "YoAliceAliceYo"
    assert make_abba("What", "Up") == "WhatUpUpWhat"
    assert make_abba("", "y") == "yy"
    assert make_abba("", "") == ""
    print("all make_abba tests passed!")


def make_tags(tag, word):
    # Instructions: Given strings tag and word, return a string where
    # word is wrapped in an HTML-style tag, so tag "i" and word "Yay"
    # yields "<i>Yay</i>".
    pass  # TODO: implement


def test_make_tags():
    assert make_tags("i", "Yay") == "<i>Yay</i>"
    assert make_tags("i", "Hello") == "<i>Hello</i>"
    assert make_tags("cite", "Yay") == "<cite>Yay</cite>"
    assert make_tags("b", "") == "<b></b>"
    print("all make_tags tests passed!")


def make_out_word(out, word):
    # Instructions: Given strings out and word, where out has length at
    # least 2, return a new string where word has been inserted in the
    # middle of out, splitting out between its first 2 characters and
    # the rest, so out "<<>>" and word "Yay" yields "<<Yay>>".
    pass  # TODO: implement


def test_make_out_word():
    assert make_out_word("<<>>", "Yay") == "<<Yay>>"
    assert make_out_word("<<>>", "WooWoo") == "<<WooWoo>>"
    assert make_out_word("[[]]", "word") == "[[word]]"
    assert make_out_word("{{}}", "test") == "{{test}}"
    assert make_out_word("Hoo", "Yay") == "HoYayo"
    print("all make_out_word tests passed!")


def extra_end(s):
    # Instructions: Given a string, return a new string made of 3 copies
    # of the last 2 characters of the original string. The string
    # length will be at least 2.
    pass  # TODO: implement


def test_extra_end():
    assert extra_end("Hello") == "lololo"
    assert extra_end("ab") == "ababab"
    assert extra_end("Hi") == "HiHiHi"
    assert extra_end("Hxyz") == "yzyzyz"
    print("all extra_end tests passed!")


def first_two(s):
    # Instructions: Given a string, return the first 2 characters. If
    # the string length is less than 2, return whatever there is.
    pass  # TODO: implement


def test_first_two():
    assert first_two("Hello") == "He"
    assert first_two("abcdefg") == "ab"
    assert first_two("ab") == "ab"
    assert first_two("a") == "a"
    assert first_two("") == ""
    print("all first_two tests passed!")


def first_half(s):
    # Instructions: Given a string of even length, return the first
    # half.
    pass  # TODO: implement


def test_first_half():
    assert first_half("WooHoo") == "Woo"
    assert first_half("HelloThere") == "Hello"
    assert first_half("abcdef") == "abc"
    assert first_half("") == ""
    assert first_half("ab") == "a"
    print("all first_half tests passed!")


def without_end(s):
    # Instructions: Given a string, return a version without the first
    # and last characters, so "Hello" yields "ell". The string length
    # will be at least 2.
    pass  # TODO: implement


def test_without_end():
    assert without_end("Hello") == "ell"
    assert without_end("java") == "av"
    assert without_end("coding") == "odin"
    assert without_end("ab") == ""
    assert without_end("abc") == "b"
    print("all without_end tests passed!")


def combo_string(a, b):
    # Instructions: Given two strings, a and b, return a string of the
    # form short+long+short, with the shorter string on the outside and
    # the longer string on the inside. The strings will not be the same
    # length, but either may be empty (length 0).
    pass  # TODO: implement


def test_combo_string():
    assert combo_string("Hello", "hi") == "hiHellohi"
    assert combo_string("hi", "Hello") == "hiHellohi"
    assert combo_string("aaa", "b") == "baaab"
    assert combo_string("", "abc") == "abc"
    assert combo_string("abc", "") == "abc"
    assert combo_string("ab", "ab") == "ababab"
    print("all combo_string tests passed!")
