## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

Function name = grammar_checker()

Parameters = takes one argument (a string)

Returns a positive statement if the grammar is correct or a negative with suggestions if not.

```python
# EXAMPLE

def grammar_checker(string):
    """returns a positive message if grammar is good and a negative with suggestions if conditions are met. Takes a mixed string and checks for a capital and punctuation.

    Parameters: (list all parameters and their types)
        a mixed string

    Returns: (state the return value and its type)
        a string (message) with suggested grammar fixes (if there are any)

    Side effects: (state any side effects)
       none
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

grammar_checker("Is this correct?")
returns "Your grammar looks good!"

grammar_checker("what about this")
returns "Your grammar could use some work: no capitalization, missing punctuation."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!