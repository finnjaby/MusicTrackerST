from Song import Song

song1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera")
print(song1)

# list to store songs in memory
songs = []

# loop to add songs
while True:
    title = input("title (or 'q' to quit): ")
    if title.lower() == "q":
        break

artist = input("artist: ")
album = input("album: ")

songs.append(Song(title, artist, album))
print("song added.\n")
  