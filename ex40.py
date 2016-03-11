class Song :

    def __init__(self, lyrics) :
        self.lyrics = lyrics

    def sing_me_a_song(self) :
        for line in self.lyrics :
            print line

happy_birthday = Song(["Happy Birthday to you", "I don't want to get sued",
    "So I'll stop right there."])

bulls_on_a_parade = Song(["They rally round your family",
    "With a pocket full of shells."])

ring_around_the_rosey_lyrics = ["Ring around the rosey",
    "Pocket full of posey", "Ashes ashes, they all fall down"]

ring_around_the_rosey = Song(ring_around_the_rosey_lyrics)

print '-' * 10
happy_birthday.sing_me_a_song()
print '-' * 10
bulls_on_a_parade.sing_me_a_song()
print '-' * 10
ring_around_the_rosey.sing_me_a_song()

# add new lyric to ring around rosey song
ring_around_the_rosey.lyrics.append("new lyric")
print '-' * 10
ring_around_the_rosey.sing_me_a_song()