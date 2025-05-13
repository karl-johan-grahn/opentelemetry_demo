# Observability With OpenTelemetry in Python - An Instrumentation Guide

Observability key data signals:

* Logs
    * Descriptive verbose information about events
    * Examples:
        * `Saturday was a sunny day`
        * `Resolving deltas: 100% (2/2), completed with 2 local objects.`
* Metrics
    * Measurements
    * Examples:
        * Blood pressure
        * Temperature
        * Response code
* Traces
    * Sequences of event information
    * Example:
        * Someone opened a door, then light got turned on, then door was closed
        * Sample span:

            ```json
            {
                "name": "sample_span",
                "context": {
                    "trace_id": "0x4b8aa5a2d2c82548331cf37ff8d69df2",
                    "span_id": "0x054441bf3lik5c13"
                },
                "parent_id": null,
                "start_time": "2023-04-30T18:52:58.113201Z",
                "end_time": "2023-04-30T18:52:58.113687Z",
                "attributes": {
                    "http.route": "sample_route"
                },
                "events": [
                    {
                        "name": "Calculation",
                        "timestamp": "2022-04-30T18:52:58.113561Z",
                        "attributes": {
                            "event_attributes": 1
                        }
                    }
                ]
            }
            ```

    * OpenTelemetry semantics:
        * Span
        * Trace - collection of connected spans

## Preparation

To prepare your environment for this demo:

1. Install Python
1. Create a virtual environment using for example [`mkvirtenv`](https://virtualenvwrapper.readthedocs.io/en/latest/):

    ```sh
    mkvirtualenv opentelemetry
    ```

1. Work on the environment:

    ```sh
    workon opentelemetry
    ```

1. If using Visual Studio Code and running from there, select the virtual environment in the lower right corner of the editor
1. Install Python requirements which includes OpenTelemetry:

    ```sh
    pip3 install -r requirements.txt
    ```

## No Telemetry at All - [v1](./v1/)

Run the server application:

```sh
python app.py
```

Send a request:

```sh
curl 'http://127.0.0.1:3000/add?first=6&second=1'
```

Watch the server and note that no telemetry signals are emitted, as expected.

## Manual Instrumentation - [v2](./v2/) and [v3](./v3/)

Run the server application:

```sh
python app.py
```

Send a request:

```sh
curl 'http://127.0.0.1:3000/add?first=6&second=1'
```

Watch the server and observe that a trace signal is emitted.

## Automatic Instrumentation of [v1](./v1/)

Automatic instrumentation is available for Python, Java, Node, Ruby, and .NET.

Python supported frameworks are listed in the [opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation) repository.

Do auto-instrumentation of the application:

```sh
opentelemetry-instrument --traces_exporter console --metrics_exporter console python app.py
```

Send a request:

```sh
curl 'http://127.0.0.1:3000/add?first=6&second=1'
```

Watch the server and observe that a trace signal is emitted.

## Mix of Manual and Automatic Instrumentation - [v4](./v4/)

Do auto-instrumentation of the application:

```sh
opentelemetry-instrument --traces_exporter console --metrics_exporter console python app.py
```

Create an exception by using the wrong value for a parameter:

```sh
curl 'http://127.0.0.1:3000/add?first=6&second=a'
```

Watch the server and observe that a trace signal is emitted, with info about the exception.

## Sample All Requests

Sample 100% of requests using [Grafana Tempo](https://grafana.com/oss/tempo/):

1. Clone the [repo](https://github.com/grafana/tempo)
1. Run the example:

    ```sh
    cd tempo/example/docker-compose/local

    docker login ghcr.io

    docker compose up -d

    docker compose ps

    docker compose down
    ```
