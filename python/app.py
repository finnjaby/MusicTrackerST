from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

CSV_FILENAME = "songs.csv"

def load_songs():
    songs = []
    try:
        with open(CSV_FILENAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                songs.append(row)
    except FileNotFoundError:
        pass
    return songs


def save_song_to_csv(title, artist, album, genre):
    file_exists = False
    try:
        open(CSV_FILENAME, "r")
        file_exists = True
    except:
        pass

    with open(CSV_FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # write header if file is new
        if not file_exists:
            writer.writerow(["title", "artist", "album", "genre"])

        writer.writerow([title, artist, album, genre])


@app.route("/")
def home():
    songs = load_songs()
    return render_template("web.html", songs=songs)


@app.route("/add", methods=["GET", "POST"])
def add_song():
    if request.method == "POST":
        title = request.form["title"]
        artist = request.form["artist"]
        album = request.form["album"]
        genre = request.form["genre"]

        save_song_to_csv(title, artist, album, genre)

        return redirect("/")

    return render_template("add_song.html")


if __name__ == "__main__":
    app.run(debug=True)
