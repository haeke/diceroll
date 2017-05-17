from flask import Flask, jsonify, request
from random import randint
app = Flask(__name__)

#results dictionarty
results = [{'result': 0}]

@app.route('/')
def index():
    return "This site is working"

@app.route("/diceroll", methods=['POST'])
def diceroll():

    roll1 = randint(1, 6)
    roll2 = randint(1, 6)

    result = roll1 + roll2

    results.append(result)

    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
