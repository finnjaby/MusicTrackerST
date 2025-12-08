from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

CSV_FILE = "songs.csv"

def load_songs_from_csv():
    songs = []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                songs.append(row)
    except FileNotFoundError:
        pass
    return songs

def save_songs_to_csv(songs):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "artist", "album", "genre"])
        for s in songs:
            writer.writerow([s["title"], s["artist"], s["album"], s["genre"]])

@app.route('/')
def home():
    songs = load_songs_from_csv()
    return render_template('web.html', songs=songs)

# ⭐ NEW: Add a song (web form)
@app.route('/add', methods=["GET", "POST"])
def add_song():
    if request.method == "POST":
        title = request.form["title"]
        artist = request.form["artist"]
        album = request.form["album"]
        genre = request.form["genre"]

        songs = load_songs_from_csv()
        songs.append({
            "title": title,
            "artist": artist,
            "album": album,
            "genre": genre
        })
        save_songs_to_csv(songs)
        return redirect('/')
    
    return render_template('add_song.html')

@app.route('/remove/<title>', methods=['POST'])
def remove_song(title):
    songs = load_songs_from_csv()
    updated = [s for s in songs if s["title"].lower() != title.lower()]
    save_songs_to_csv(updated)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
