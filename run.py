import os
from flask import Flask, render_template , request ,flash

app = Flask(__name__)
app.secret_key= "secret_word"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Thanks {} , next press play to begin".format
    (request.form["name"]))
    return render_template("index.html" , page_title="RiddleTwister")
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html" , page_title="leaderboard")
    
@app.route('/riddle_game')
def riddle_game():
    return render_template("riddle_game.html" , page_title="riddle_game")
 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)