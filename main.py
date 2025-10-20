import sys
from Song import Song

song1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera")
print(song1)


# list to store songs in memory
songs = []

# loop to add songs
while True:
    title = input("title (or 'q' to quit): ")
    if title.lower() == "q":
        sys.exit(f"quitting")
    else: break

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
# This function views all the songs
def view_songs(song_list):
    print("\n=== My Music Collection ===")
    print(f"{'Title':<25} | {'Artist':<20} | {'Album'}")
    print("-" * 60)
    for song in song_list:
        print(song.display_info())

# Calls the function
view_songs(songs)

# Edit songs

while (1):
    yn = input("Do you want to edit your playlist? \n (Y/N)")
    if yn.lower() == "y":
        edit = input("Enter the title of the song you want to Edit:")
        if edit.lower() == title.lower():
            title = input("Edit Title to:")
            """ save = input("Save changes? Y/N")
            if save.lower() == "y":
                print("New title is: " + title) """
        else: print("Title not Found.")
    elif yn.lower == "n":
        print("You have exited editing.")
        break
    else: print("Invalid Input.")

