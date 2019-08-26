import os
from flask import Flask, render_template , request ,flash, jsonify
import json
import random
import numpy

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
    username = []
    score =[]
    final_user_list = []
    all_params = request.args
    f = open("response.txt", "r")
    winners = f.readlines()
    f.close()
    for i in range (0,len(winners)):
    #  print(winners[i])
        if (i % 2 == 0):
            # print(winners[i],"username")
            username.append(winners[i].replace('\n', ''))
        else:
            # print(winners[i],"score")
            score.append(int(winners[i].replace('\n', '')))
    print(username, score)
    original_index_of_score = numpy.argsort(score)
    score = sorted(score)
    for index in original_index_of_score:
         final_user_list.append(username[index])
    print(final_user_list, score)
    if len(score) <= 10:
        return render_template("leaderboard.html" , page_title="leaderboard", userlist = final_user_list, user_score = score)
    else:
        score = score[-10:]
        final_user_list = final_user_list[-10:]
        return render_template("leaderboard.html" , page_title="leaderboard", userlist = final_user_list, user_score = score)
    
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

f = open ("hint_1.txt","w")
f.write("bathroom item\n","combines two words\n","used for communication\n","you need it to survive\n",
"vampire\n","In the absence of light you have...\n","it sunk the titanic\n","no one knows...\n","a loss of words\n"
,"oxygen,heat,fuel\n","the weight of a small car\n","only a little left\n","a fruit for roman kings\n"
,"a hydrogen sulfide gas\n","a precious metal\n","they give us free oxygen\n","we would not survive more then week without it\n"
,"you use it to point\n","something you make on ayour wedding day\n","more then eighty percent of the earth is covered in it\n")
f.close

f = open ("hint_2.txt","w")
f.write("you use it to dry off\n","soft under your toes\n","a device\n","the human body is made up 50%-75% of it\n",
"zombies rise from the dead\n","power outage\n","exist in the arctic\n","top secret\n","nothing to say\n"
,"leaves a path of chared pieces\n","african forest elephant\n","survivers\n","turn into raisins when dried\n"
,"whoopy cushion\n","low quatity high demand\n","a place where monkeys live\n","low supply in the desert\n"
,"used to pick things up\n","best friends keep them\n","air,land and...\n")
f.close