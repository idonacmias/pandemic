from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"







# from data import Bord



# if __name__ == '__main__':
# 	bord = Bord(num_player=1, difficulty=0)
	


