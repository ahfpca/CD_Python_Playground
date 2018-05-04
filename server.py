from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", count = 3)

@app.route("/play/<count>")
def play(count):
    return render_template("index.html", count = int(count))

@app.route("/play/<count>/<color>")
def playWithColor(count, color):
    return render_template("index.html", count = int(count), color = color)
    

if __name__ == "__main__":
    app.run(debug = True)
