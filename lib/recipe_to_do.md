## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

example text? what format is the text? is it a diary entry? post it note style? 

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

Function name = to_do()

Parameters = takes one argument(string)

append text following todo to list and then V

Returns the task and a message to display if task is actionable

Side effects:
possibility poor formatting/illegibility. Takes prior knowledge of "to do tasks" depending on how good the users input is

```python
# EXAMPLE

def to_do():
    """checks 

    Parameters: (string)
        an amount of text (eg "#TODO take the dog for a walk")

    Returns: (state the return value and its type)
        an updated list (eg ["1 take the dog for a walk. 2 take out the bins. 3 paint the house"])

    Side effects: (state any side effects)
        illegibility depending on complexity, unknown user input
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

to_do("Hi, it's me")
returns "This isn't an actionable task"

to_do("#TODO take the dog for a walk")
returns "take the dog for a walk is on your to do list!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!

