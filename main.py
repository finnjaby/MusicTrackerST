import random
from Song import Song


def print_menu():
    print("\n=== Music Tracker Menu ===")
    print("1) Add song")
    print("2) Remove song")
    print("3) View songs")
    print("4) Pick random song")
    print("5) Edit a song")
    print("q) Quit")


def pick_random_song(song_list):
    if not song_list:
        print("no songs available to pick.\n")
        return
    choice = random.choice(song_list)
    print(f"random pick: {choice.title} - {choice.artist} ({choice.album})\n")


def view_songs(song_list):
    if not song_list:
        print("\nNo songs in your list yet.")
        return
    print("\n=== My Music Collection ===")
    print(f"{'Title':<25} | {'Artist':<20} | {'Album'}")
    print("-" * 60)
    for song in song_list:
        print(song.display_info())


def add_song(songs):
    title = input("title (blank to cancel): ").strip()
    if not title:
        print("canceled.")
        return
    artist = input("artist: ").strip()
    album = input("album: ").strip()
    songs.append(Song(title, artist, album))
    print("song added.\n")


def remove_song(songs):
    if not songs:
        print("no songs to remove.")
        return
    remove = input("title to remove: ").strip()
    for i, s in enumerate(songs):
        if s.title.lower() == remove.lower():
            songs.pop(i)
            print("song removed.\n")
            return
    print("no song found with that title.\n")


def edit_song(songs):
    if not songs:
        print("no songs to edit.")
        return
    print("\nYour current playlist:")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")
    target = input("\nEnter the exact title to edit: ").strip()
    for s in songs:
        if s.title.lower() == target.lower():
            new_title = input(f"New title (enter to keep '{s.title}'): ").strip()
            new_artist = input(f"New artist (enter to keep '{s.artist}'): ").strip()
            new_album = input(f"New album (enter to keep '{s.album}'): ").strip()
            if new_title:
                s.title = new_title
            if new_artist:
                s.artist = new_artist
            if new_album:
                s.album = new_album
            print("Song updated!\n")
            return
    print("Title not found.\n")


def main():
    songs = []
    print("Welcome to Music Tracker!")

    while True:
        print_menu()
        choice = input("Select an option: ").strip().lower()

        if choice == "1":
            add_song(songs)
        elif choice == "2":
            remove_song(songs)
        elif choice == "3":
            view_songs(songs)
        elif choice == "4":
            pick_random_song(songs)
        elif choice == "5":
            edit_song(songs)
        elif choice == "q":
            print("quitting")
            break
        else:
            print("invalid selection. please choose from the menu.")


if __name__ == "__main__":
    main()
