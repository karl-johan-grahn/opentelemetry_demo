# OpenTelemetry and Python - A complete instrumentation guide
Based on https://www.cncf.io/blog/2022/04/22/opentelemetry-and-python-a-complete-instrumentation-guide/

Observability key koncepts:
* Logs
* Metrics
* Traces

OpenTelemetry semantics: Span, trace

Create virtual environment and then work on it:
```sh
mkvirtualenv opentelemetry
workon opentelemetry
```

## No telemetry at all - v1
```sh
flask run
curl 'http://127.0.0.1:5000/roll?sides=6&rolls=1'
```

## Manual instrumentation - v2/v3
Run and observe the trace.

## Automatic - v1
Python, Java, Node, Ruby, and .NET

Python supported frameworks:
https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation

```sh
opentelemetry-instrument --traces_exporter console flask run
```

## Mix - v4
Create exception and observe auto trace:
```sh
curl 'http://127.0.0.1:5000/roll?sides=6&rolls=a'
```

## Grafana Tempo
Sample 100% of requests:
https://grafana.com/oss/tempo/
