from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos




@app.route("/player")
def player():
    return {'name':'bob'}







# from data import Bord



# if __name__ == '__main__':
# 	bord = Bord(num_player=1, difficulty=0)
	


