import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import PlayerScores
from db import db

#load env variables
load_dotenv()

app = Flask(__name__)


######### Database Configuration ###########
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/mastermind"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#####################


####### API Routes ############
'''API route to get all player scores and post new scores to database'''
@app.route("/player-scores", methods=['GET', 'POST'])
def player_scores():
    if request.method == 'GET':
        all_scores = PlayerScores.query.all()
        output = []

        for score in all_scores:
            current_score = {}
            current_score['name'] = score.name
            current_score['score'] = score.score
            output.append(current_score)
        

        return jsonify(output)


    if request.method == 'POST':
        player_data = request.get_json()
        player = PlayerScores(name=player_data['name'], score=player_data['score'])
        db.session.add(player)
        db.session.commit()
        
        return jsonify(player_data)

'''API route to get all the scores from a specific player'''
@app.route("/player-scores/<name>", methods=['GET'])
def get_my_score(name):
    scores = PlayerScores.query.filter_by(name=name).all()
    output = []

    for score in scores:
            current_score = {}
            current_score['name'] = score.name
            current_score['score'] = score.score
            output.append(current_score)

    return jsonify(output)
    
'''API route to only return the top 10 scores'''   
@app.route("/high-scores", methods=['GET'])
def high_scores():
    all_scores = PlayerScores.query.all()
    output = []
    for score in all_scores:
        current_score = {}
        current_score['name'] = score.name
        current_score['score'] = score.score
        output.append(current_score)
    
    high_scores = sorted(output, key=lambda d: d['score'], reverse=True)[:10]

    return jsonify(high_scores)

#################################

if __name__ == "__main__":
    app.run(debug=True)