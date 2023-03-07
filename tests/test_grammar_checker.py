from lib.grammar_checker import *

def test_grammar_checker():
    result = grammar_checker("Is this correct?")
    assert result == "Your grammar looks good!"
    result = grammar_checker("and now")
    assert result == "Your grammar could use some work."
    result = grammar_checker("And now")
    assert result == "Your grammar could use some work: missing punctuation."