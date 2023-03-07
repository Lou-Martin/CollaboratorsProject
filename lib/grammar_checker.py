def grammar_checker(string):
    capital = False
    punctuation = True

    positive_message = "Your grammar looks good!"
    negative_message = "Your grammar could use some work."
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
        print(capital)
        print(punctuation)
        return negative_message

    elif capital == True and punctuation == False:
        print(capital)
        print(punctuation)
        return negative_capitalization
    
    elif capital == False and punctuation == True:
        print(string[-1:])
        print(capital)
        print(punctuation)
        return negative_punctuation
    
    elif capital == False and punctuation == False:
        print(capital)
        print(punctuation)
        return positive_message
    else:
        return "Something's weird - how did you get here?"
