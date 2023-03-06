from lib.time_to_read import *

def test_time_to_read():
    result = time_to_read(2000)
    assert result == "This text will take approximately 10 minutes to read."
    result = time_to_read(1)
    assert result == "This text will take less than a minute to read!"