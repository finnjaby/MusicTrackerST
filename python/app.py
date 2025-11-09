from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the template (no songs yet)
    return render_template('web.html')

if __name__ == '__main__':
    app.run(debug=True)
