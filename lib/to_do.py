#File : to_do.py
to_do_list = []
def to_do(string):
    if string[0:5].upper() == "#TODO":
        to_do_list.append(string[6:])
        return f"{string[6:]} is on your to do list!"
    else:
        return "This isn't an actionable task!"
    
#print(to_do("#TODO take the dog for a walk"))
# print(to_do_list)