# Observability with OpenTelemetry in Python - An instrumentation guide

Observability key concepts:

* Logs
    * Descriptions
    * Example:
        * `Saturday was a sunny day`
        * `Resolving deltas: 100% (2/2), completed with 2 local objects.`
* Metrics
    * Measurements
    * Example:
        * Blood pressure
        * Temperature
        * Response code
* Traces
    * Sequence of events
    * Example:
        * Someone opened the door, then the light got turned on, then the door was closed
        * Sample span:
            ```json
            {
                "name": "sample_span",
                "context": {
                    "trace_id": "0x5b8aa5a2d2c872e8321cf37308d69df2",
                    "span_id": "0x051581bf3cb55c13"
                },
                "parent_id": null,
                "start_time": "2022-04-29T18:52:58.114201Z",
                "end_time": "2022-04-29T18:52:58.114687Z",
                "attributes": {
                    "http.route": "sample_route"
                },
                "events": [
                    {
                        "name": "Door opened",
                        "timestamp": "2022-04-29T18:52:58.114561Z",
                        "attributes": {
                            "event_attributes": 1
                        }
                    }
                ]
            }
            ```

OpenTelemetry semantics: Span, trace

## Preparation

Install Python

Create a virtual environment using for example [mkvirtenv](https://virtualenvwrapper.readthedocs.io/en/latest/) and then work on it:

```sh
mkvirtualenv opentelemetry
workon opentelemetry
```

Install requirements:

```sh
pip3 install -r requirements.txt
```

## No telemetry at all - [v1](./v1/)

```sh
python app.py
curl 'http://127.0.0.1:5000/add?first=6&second=1'
```

## Manual instrumentation - [v2](./v2/)/[v3](./v3/)

Run and observe the trace.

## Automatic - [v1](./v1/)

Python, Java, Node, Ruby, and .NET

Python supported frameworks are listed in the [opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation) repository.

```sh
opentelemetry-instrument --traces_exporter console --metrics_exporter console python app.py
```

## Mix - [v4](./v4/)

Create exception and observe auto trace:

```sh
opentelemetry-instrument --traces_exporter console --metrics_exporter console python app.py

curl 'http://127.0.0.1:5000/add?first=6&second=a'
```

## Grafana Tempo

Sample 100% of requests using [Grafana Tempo](https://grafana.com/oss/tempo/):

```sh
cd tempo/example/docker-compose/local

docker compose up -d

docker compose ps

docker compose down
```
