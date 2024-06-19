from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

from flask import Flask, request

# API entry point that holds configuration
provider = TracerProvider()
# Defines the method of sending the spans onwards to a consumer,
# in this case to the console, otherwise usually to a collector
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
# Actual object which creates the spans
tracer = trace.get_tracer(__name__)

app = Flask(__name__)


@app.route("/add")
def add():
    with tracer.start_as_current_span("request_to_add_numbers"):
        first = int(request.args.get('first'))
        second = int(request.args.get('second'))
        return str(sum_numbers(first, second))


def sum_numbers(first: int, second: int) -> int:
    sum = first + second
    return sum


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=3000)
