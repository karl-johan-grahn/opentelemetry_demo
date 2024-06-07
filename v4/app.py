from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

from random import randint
from flask import Flask, request

provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)


@app.route("/roll")
def roll():
    sides = int(request.args.get('sides'))
    rolls = int(request.args.get('rolls'))
    return roll_sum(sides, rolls)


def roll_sum(sides, rolls):
    with tracer.start_as_current_span("roll_sum"):
        span = trace.get_current_span()
        sum = 0
        for r in range(0, rolls):
            result = randint(1, sides)
            span.add_event("log", {
                "roll.sides": sides,
                "roll.result": result,
            })
            sum += result
        return str(sum)
