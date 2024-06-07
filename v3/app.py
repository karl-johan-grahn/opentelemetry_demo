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


@app.route("/add")
def add():
    with tracer.start_as_current_span(
        "request_to_add_numbers",
        attributes={"endpoint": "/add"}
    ):
        first = int(request.args.get('first'))
        second = int(request.args.get('second'))
        return str(sum_numbers(first, second))


def sum_numbers(first: int, second: int) -> int:
    span = trace.get_current_span()
    span.add_event("log", {
        "add.first": first,
        "add.second": second,
    })
    sum = first + second
    return sum
