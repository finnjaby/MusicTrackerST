class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album
    
    def __str__(self):
        return f"'{self.title}' by {self.artist} from the album '{self.album}'"

# This returns a formatted string showing the song’s title, artist, and album in aligned columns for easy viewing.
    def display_info(self):
        """Return a formatted string for displaying song details"""
        return f"{self.title:<25} | {self.artist:<20} | {self.album}"