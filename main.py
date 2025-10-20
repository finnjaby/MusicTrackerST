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
  
  # print all songs before exiting
print("\nall songs added:")
for s in songs:
    print(f"{s.title} - {s.artist} ({s.album})")

print

# loop to remove songs

while True:
    remove = input("title to remove (or 'stop' to stop removing): ")
    if remove.lower() == "stop":
        break
    for i, s in enumerate(songs):
        if s.title.lower() == remove.lower():
            songs.pop(i)
            print("song removed.\n")
            break
    else:
        print("no song found with that title.\n")