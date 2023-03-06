
## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

Function name = time_to_read()

Parameters = takes one argument (number of words)

Returns number of words divided by 200 to give a time to read in minutes.

May cause issues with decimal places. avoid by returning less than a minute for args less than 200 and then round to 1 dp for everything else or force int instead float

```python
# EXAMPLE

def time_to_read(numwords):
    """calculates estimated time to read based on 200wpm

    Parameters: (list all parameters and their types)
        a number of words (eg "3000")

    Returns: (state the return value and its type)
        a string plus numerical value for time to read (eg ["Estimated time to read: 10.5 minutes)

    Side effects: (state any side effects)
        with a given wpm count of 200 there shouldnt be any awkward rounding numbers but limiting the result either to an int or forcing 1dp would increase readability
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

time_to_read(2000)
returns "Estimated time to read 2000 words is 10 minutes."

time_to_read(150)
returns "estimated time to read 150 words is less than a minute."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!