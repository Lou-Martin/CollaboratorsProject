def make_snippet(str):

    list_ = str.split(" ")

    new_str = ""
    for i in range(5):
        new_str += (list_[i] + " ")

    new_str = new_str[:-1]

    if len(list_) <= 5:
        return str
    else:
        new_str += "..."

    return new_str
    


