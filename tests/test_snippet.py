from lib.snippet import *

def test_snippet():
    result = make_snippet("This is my dog called Juniper")
    assert result == "This is my dog called..."