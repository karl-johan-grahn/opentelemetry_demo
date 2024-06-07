from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

from random import randint
from flask import Flask, request

# API entry point that holds configuration
provider = TracerProvider()
# Defines the method of sending the spans onwards,
# in this case to the console, otherwise usually to a collector
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
# Actual object which creates the spans
tracer = trace.get_tracer(__name__)

app = Flask(__name__)


@app.route("/roll")
def roll():
    with tracer.start_as_current_span("request_to_roll_the_dice"):
        sides = int(request.args.get('sides'))
        rolls = int(request.args.get('rolls'))
        return roll_sum(sides, rolls)


def roll_sum(sides, rolls):
    sum = 0
    for r in range(0, rolls):
        result = randint(1, sides)
        sum += result
    return str(sum)
