def count_words(str):
    count = 0
    for i in str:
        if i == " ":
            count += 1
    if count == 1 and str == " ":
        return 0
    else:
        return count + 1
    
