import os
from flask import Flask, render_template , request ,flash, jsonify
import json
import random

app = Flask(__name__)
app.secret_key= "secret_word"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Thanks {} , next press play to begin".format
    (request.form["name"]))
    return render_template("index.html" , page_title="LoginRiddleTwister")
    
@app.route('/leaderboard')
# # # incorrect code!
def leaderboard():
# #     all_params = request.args
# #     username = all_params['username']
# #     score = all_params['score']
# #     f = open("response.txt", "r")
# #     winners = f.readlines()
# #     for i in range (len(winners)):
# #     print(wordlist[i])
    # f.close()
    return render_template("leaderboard.html" , page_title="leaderboard")
    
@app.route('/riddle_game', methods=["GET", "POST"])
def riddle_game():
    args = request.args
    print(args['username'])
    return render_template("riddle_game.html" , page_title="riddle_game", user=args['username'])

@app.route('/get_riddle_api' , methods=["GET", "POST"])
def get_riddle_api():
    f = open("questions.txt", "r")
    all_questions = f.readlines()
    single_question = all_questions[random.randint(0, len(all_questions))]
    f.close()
    return jsonify(single_question.rstrip())

@app.route('/get_answer_api' , methods=["GET", "POST"])
def get_answer_api():
    all_params = request.args
    index = 0
    question = all_params['question'].replace('"', '')
    answer = all_params['answer'].replace('"', '')
    f = open("questions.txt", "r")
    all_questions = f.readlines()
    for quest in all_questions:
        if question.rstrip() == quest.rstrip():
            index = all_questions.index(quest)
            print(type(quest.rstrip()), "here")
    f.close()
    print(type(question), index)
   
    
    fa = open("answers.txt", "r")
    all_answers = fa.readlines()
    fa.close()
    print(answer.rstrip(),all_answers[index].rstrip().lower(), "both answers")
    if (all_answers[index].rstrip().lower() == answer.rstrip().lower()):
        return jsonify(True)
    else:
        return jsonify(False)
    
# print everything that that is there in the string to see what is there
# break down the functionality of each step! for understanding

@app.route('/get_username_and_score_api', methods=["GET", "POST"])
def get_username_and_score_api():
    all_params = request.args
    username = all_params['username']
    score = all_params['score']
    f = open("response.txt", "a")
    f.write(username + "\n")
    f.write(score + "\n")
    f.close
    return jsonify("True")
    
    
    



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

f = open("questions.txt", "r")
f.readlines()
f.close()

f = open("answers.txt", "r")
f.readlines()
f.close()

f = open ("response.txt", "a")
f.write()
f.close

# f = open ("hint.txt","w")
# f.write("bathroom item\n","combines two words\n","used for communication\n","you need it to survive\n",
# "vampire\n","In the absence of light you have...\n","sunk the titanic\n","military covert mission\n")
# f.close