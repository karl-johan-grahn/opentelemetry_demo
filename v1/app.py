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


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=3000)
