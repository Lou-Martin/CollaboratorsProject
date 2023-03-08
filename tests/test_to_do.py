#File: test_to_do.py

from lib.to_do import *

def test_to_do():
    result = "This isn't an actionable task!"
    assert result == to_do("Hi, it's me")
    result2 = "take the dog for a walk is on your to do list!"
    assert result2 == to_do("#TODO take the dog for a walk")




