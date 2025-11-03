import sys
import random
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

# Random song picker
def pick_random_song(song_list):
    if not song_list:
        print("no songs available to pick.\n")
        return
    choice = random.choice(song_list)
    print(f"random pick: {choice.title} - {choice.artist} ({choice.album})\n")


# Offer random song suggestion
pick = input("Pick a random song (Y/N): ")
if pick.lower() == "y":
    pick_random_song(songs)

# Edit songs
while True:
    yn = input("Do you want to edit your playlist? (Y/N): ").strip().lower()

    if yn == "n":
        break

    if yn == "y":
        print("\nYour current playlist:")
        for i, song in enumerate(songs, 1):
            print(f"{i}. {song}")

        edit = input("\nEnter the title of the song you want to edit: ").strip()

        for i in range(len(songs)):
            if edit.lower() in songs[i].title.lower():
                new_title = input("Edit title to: ").strip()
                songs[i] = new_title
                print("Song title updated!")
            else:
                print("Title not found.")

    else:
        print("Invalid input, please enter Y or N.")

# This function views all the songs
def view_songs(song_list):
    print("\n=== My Music Collection ===")
    print(f"{'Title':<25} | {'Artist':<20} | {'Album'}")
    print("-" * 60)
    for song in song_list:
        print(song.display_info())

# Calls the function
view_songs(songs)