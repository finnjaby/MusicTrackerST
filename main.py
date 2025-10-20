from Song import Song

song1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera")
print(song1)

# This function views all the songs
def view_songs(song_list):
    print("\n=== My Music Collection ===")
    print(f"{'Title':<25} | {'Artist':<20} | {'Album'}")
    print("-" * 60)
    for song in song_list:
        print(song.display_info())

# Calls the function
view_songs(songs)