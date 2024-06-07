# Observability with OpenTelemetry in Python - A quick instrumentation guide

Observability key concepts:

* Logs
* Metrics
* Traces

OpenTelemetry semantics: Span, trace

## Preparation

Install Python

Create a virtual environment using for example [mkvirtenv](https://virtualenvwrapper.readthedocs.io/en/latest/)

```sh
pip3 install -r requirements.txt
```

and then work on it:

```sh
mkvirtualenv opentelemetry
workon opentelemetry
```

## No telemetry at all - [v1](./v1/)

```sh
flask run
curl 'http://127.0.0.1:5000/roll?sides=6&rolls=1'
```

## Manual instrumentation - [v2](./v2/)/[v3](./v3/)

Run and observe the trace.

## Automatic - [v1](./v1/)

Python, Java, Node, Ruby, and .NET

Python supported frameworks are listed in the [opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation) repository.

```sh
opentelemetry-instrument --traces_exporter console flask run
```

## Mix - [v4](./v4/)

Create exception and observe auto trace:

```sh
opentelemetry-instrument --traces_exporter console flask run

curl 'http://127.0.0.1:5000/roll?sides=6&rolls=a'
```

## Grafana Tempo

Sample 100% of requests using [Grafana Tempo](https://grafana.com/oss/tempo/):

```sh
cd tempo/example/docker-compose/local

docker compose up -d

docker compose ps

docker compose down
```
