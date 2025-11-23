from flask import Flask, render_template
import csv

app = Flask(__name__)

def load_songs_from_csv():
    songs = []
    try:
        with open("songs.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                songs.append(row)
    except FileNotFoundError:
        pass 
    return songs

@app.route('/')
def home():
    songs = load_songs_from_csv()
    return render_template('web.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
