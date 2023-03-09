from lib.diary_entry import *

'''

I really don't like using multi-line strings as comments. Oh well.

format should return title and string together with specific formatting 
("My title: My contents")

'''

def test_format_returns_title_and_contents():
    my_diary = DiaryEntry("A title", "These are the contents")
    result = my_diary.format()
    assert result == "A title: These are the contents"

def test_different_diary_entry_format():
    another_diary = DiaryEntry("Another Diary", "These are also the contents")
    result = another_diary.format()
    assert result == "Another Diary: These are also the contents"

'''

#count_words takes no arguments and returns the number of words in the #format diary entry (contents inclusive)

'''

def test_count_words_short_entry():
    my_diary = DiaryEntry("A title", "These are the contents")
    result = my_diary.count_words()
    assert result == 4

def test_count_words_longer_entry():
    another_diary = DiaryEntry("Another Diary", "These are also the contents")
    result = another_diary.count_words()
    assert result == 5

'''

#reading_time takes an argument (an number, words per minute) to calculate the time it will take the user to read the contents of a given diary entry.

returns an integer (an estimate of the reading time in minutes)

'''

def test_reading_time_slow():
    my_diary = DiaryEntry("A title", "These are the contents")
    result = my_diary.reading_time(2)
    assert result == 2

def test_reading_time_faster():
    another_diary = DiaryEntry("Another Diary", "These are also the contents")
    result = another_diary.reading_time(5)
    assert result == 1

'''

#reading_chunk is a function that will return the amount of words that a user can read in a specified time frame. Its passed the arguments wpm and minutes (the speed at which a user can read and the time the user has) and should return a "chunk" of text in string format.

'''

def test_reading_chunk_small():
    my_diary = DiaryEntry("A title", "These are the contents")
    result = my_diary.reading_chunk(4, 1)
    assert result == "These are the contents"

def test_reading_chunk_bigger():
    another_diary = DiaryEntry("Another Diary", "These are also the contents")
    result = another_diary.reading_chunk(5, 1)
    assert result == "These are also the contents"

def test_reading_chunk_sequentially():
    new_diary = DiaryEntry("Big book", "Ah, distinctly I remember it was in the bleak December; And each separate dying ember wrought its ghost upon the floor. Eagerly I wished the morrow; vainly I had sought to borrow From my books surcease of sorrow sorrow for the lost Lenore For the rare and radiant maiden whom the angels name Lenore Nameless here for evermore.")
    result = new_diary.reading_chunk(5, 1)
    assert result == "Ah, distinctly I remember it"
    result = new_diary.reading_chunk(5,1)
    assert result == "was in the bleak December;"
    
def test_reading_chunk_refresh():
    new_diary = DiaryEntry("Big book", "Ah, distinctly I remember it was in the bleak December; And each separate dying ember wrought its ghost upon the floor. Eagerly I wished the morrow; vainly I had sought to borrow From my books surcease of sorrow sorrow for the lost Lenore For the rare and radiant maiden whom the angels name Lenore Nameless here for evermore.")
    new_diary.reading_chunk(29,2)
    result = new_diary.reading_chunk(5,1)
    assert result == "Ah, distinctly I remember it"

def test_reading_chunk_repeat():
    newest_diary = DiaryEntry("Small book", "This is a small amount of text")
    result = newest_diary.reading_chunk(14,1)
    assert result == "This is a small amount of text"
    