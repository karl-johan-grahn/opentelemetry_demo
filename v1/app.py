from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def add():
    first = int(request.args.get('first'))
    second = int(request.args.get('second'))
    return str(sum_numbers(first, second))


def sum_numbers(first: int, second: int) -> int:
    sum = first + second
    return sum
