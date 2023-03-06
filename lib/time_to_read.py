def time_to_read(numberofwords):
    minutes = numberofwords / 200
    minutes_rounded = int(minutes)
    if minutes_rounded < 1:
        return "This text will take less than a minute to read!"
    else:
        return f"This text will take approximately {minutes_rounded} minutes to read."
    