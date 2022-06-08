from random import randint
from flask import Flask, request

app = Flask(__name__)

@app.route("/roll")
def roll():
    sides = int(request.args.get('sides'))
    rolls = int(request.args.get('rolls'))
    return roll_sum(sides,rolls)

def roll_sum(sides, rolls):
    sum = 0
    for r in range(0,rolls):
        result = randint(1,sides)
        sum += result
    return str(sum)
