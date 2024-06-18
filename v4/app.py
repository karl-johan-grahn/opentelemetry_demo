from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

from flask import Flask, request

# Now no traces are sent to console unless we specify that as exporter
# with opentelemetry-instrument, because a consumer has not been configured
tracer = trace.get_tracer(__name__)

app = Flask(__name__)


@app.route("/add")
def add():
    first = int(request.args.get('first'))
    second = int(request.args.get('second'))
    return str(sum_numbers(first, second))


def sum_numbers(first: int, second: int) -> int:
    with tracer.start_as_current_span("add_sum"):
        span = trace.get_current_span()
        span.add_event("log", {
            "add.first": first,
            "add.second": second,
        })
        sum = first + second
        return sum


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=3000)
