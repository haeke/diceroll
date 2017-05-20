"""
    simulate a dice roll, return the result as a json object
    this implementation takes the number of dice and the number of the sides
    of the dice as a parameter
"""

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

def _roll(num_dice, sides):
    """return the dice n times """
    return { 'Roll %s' % str(i+1): random.randrange(sides) for i in range(num_dice)}

@app.route('/dice')
@app.route('/dice/<int:num_dice>/sides/<int:sides>')
def roll(num_dice=4, sides=6):
    return jsonify(_roll(num_dice, sides))

if __name__ == '__main__':
    app.run(debug=True)
