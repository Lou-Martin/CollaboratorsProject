class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.unread_library = self.contents.split()

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        contents_as_list = self.contents.split()
        counter = 0
        for words in contents_as_list:
            counter += 1
        return counter
    
    def reading_time(self, wpm):
        time_taken_to_read_contents = self.count_words() / wpm
        return time_taken_to_read_contents

    def reading_chunk(self, wpm, minutes):
        amount_user_can_read = wpm * minutes #this is the calculation that determines the size of chunk
        if self.unread_library == []:
            self.unread_library = self.contents.split()
            #self.unread_library - this is a copy of the diary entry, in list format and should contain all unread text
        chunk = " ".join(str(word) for word in self.unread_library[0:amount_user_can_read]) #this is the text that the user will read in their alotted time
        del self.unread_library[0:amount_user_can_read] #deletes first word within self.unread library up to the index equal to amount_user_can_read
        return chunk