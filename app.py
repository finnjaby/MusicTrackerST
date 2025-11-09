from flask import Flask, render_template
from Song import Song   # reuse your class

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
