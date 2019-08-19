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

f = open("questions.txt", "w+")
f.write("What gets wetter as it dries?\n What do you get when you cross an automobile with a household animal?\nWhat has a ring, but no finger?\nThree lives have I gentle enough to sooth the skin, light enough to caress the sky, hard enough to crack rocks\nThe one who makes it sells it,the one who buys it never uses it, the one who uses it never knows they use it. What is it?\nThe more you have of it the less you see. What is it?\n I am lighter then what I am made of, more of me is hidden then seen? What am I?\nWhen you have me, you feel like sharing me. But, if you do share me, you don't have me. What am I?\nSay my name and I dsiapear? What am I?\n I am always hungry, I must always be fed the finger I touch will soon turn red?\nForward im heavy but backword im not. What am I?\nI know a word of letters three, add two,and fewer there will be?\nWhen young I am sweet in the sun. When middle aged, I make you gay. When old I am valued more then ever.\nWhen set loose I fly away Never so cursed, as when I go astray. What am I?\nI drive men mad for love of me. Easliy beaten. Never free.\nI reach for the sky but clutch to the ground, Sometimes I leave but I’m always around. What am I?\nAlways in you , sometimes on you. If I surround you I can kill you what am I?\n What can point in every single direction but can reach the destination by itself?\nWhen you give me to others you have to keep me What am I?\nWhich letter of the alphabet has the most water?")
f.close()

f =open("answers.txt", "w+")
f.write("towel\ncarpet\ntelephone\nwater\ncoffin\ndarkness\niceberg\nsecret\nsilence\nfire\nton\nfew\ngrapes\nfart\ngold\ntree\nwater\nfinger\npromise\nC")
f.close()