class Music():

    def __init__(self, performer, song, album, year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year

    def __str__(self):
#        return "Performer:  " + self.performer + "\nSong:   " + self.song
        return f"Performer: {self.performer}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"


music = Music("Ed Sheeran","I  see fire","Divide","2017")
print(music)