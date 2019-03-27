# That's how you define a basic object class
class Song(object):

    # self variable is the empty object made by Python
    # It' s a special function which create not-empty object from the empty one (which is some sort of a skeleton...)
    # here is said that we take 1 more parameter - lyrics
    def __init__(self, lyrics):
        # this new created empty object it fulfilled - we create the variable self.lyrics = lyrics
        # self is given by defualt by Python
        self.lyrics = lyrics
    
    # create a function for this class objects
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        #self.number_words = len(" ".join(self.lyrics).split())
        #print("We have w lines in number: ", len(" ".join(self.lyrics).split()))
    
    def number_lines(self):
        self.lines = len(self.lyrics)
        print(len(self.lyrics))
    
    def number_words(self):
        self.number_of_words = len(" ".join(self.lyrics).split())
        print(len(" ".join(self.lyrics).split()))


song1 = ["Happy birthday to you",
        "I don't want to get sued",
        "So I'll stop right there"]

song2 = ["It's a song",
        "Such a nice song"]

# we give lyrics here while creating an object
happy_bday = Song(song1)
new_song = Song(song2)

happy_bday.sing_me_a_song()

new_song.sing_me_a_song()

print("")
#print(new_song)
print(">>>>>>")
print(new_song.number_words)
print(">>>>>>")
print(new_song.lyrics)
print(new_song.number_lines())
print("")
print()