from lib.count_words import *

def test_count_words():
    result = count_words("there are seven words in this string")
    assert result == 7
    result2 = count_words(" ")
    assert result2 == 0
    result3 = count_words("Hello")
    assert result3 == 1