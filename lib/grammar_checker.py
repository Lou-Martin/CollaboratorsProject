def grammar_checker(string):
    capital = False
    punctuation = True
    
    # error_list = [] < - For future refactoring, an error list using the .join() method
    #  to add the list to one sole error message would make the program 
    # infinitely scalable and remove the dependancy on if/elif/else statements
    
    positive_message = "Your grammar looks good!"
    negative_message = "Your grammar could use some work: no capitalization, missing punctuation."
    negative_punctuation = "Your grammar could use some work: missing punctuation."
    negative_capitalization = "Your grammar could use some work: missing capitalization."
    
    if type(string) != str:
        raise Exception("That's not a string!")
    
    if string[0] != string[0].capitalize():
        capital = True
    
    for mark in ['.', '!', '?']:
        if string.endswith(mark):
            punctuation = False
            break

    if capital == True and punctuation == True:
        return negative_message

    elif capital == True and punctuation == False:
        return negative_capitalization
    
    elif capital == False and punctuation == True:
        return negative_punctuation
    
    elif capital == False and punctuation == False:
        return positive_message
    else:
        return "Something's weird - how did you get here?"
