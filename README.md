# Otel Python and Flask 3.0.0

## Prerequisites

* Docker
* docker-compose

## To run - bootstrapped

```
docker-compose -f docker-compose.bootstrap.yml up
```

The call to `opentelemetry-bootstrap` will log in the foreground this skipping of the Flask instrumentor installation: `instrumentation for package flask<3.0,>=1.0 is available but version flask==3.0.0 is installed. Skipping.`

The app will still load and Otel API is still usable by the application code.


## To request - bootstrapped

```
curl -v http://0.0.0.0:5000/test/
```

The resulting trace exported to console will include one `INTERNAL` span for the call to Otel API, but will be missing the `SERVER` span expected of auto-instrumentation of a Flask app.


## To run - manual instrumentation

```
docker-compose -f docker-compose.incode.yml up
```

The call to `pip install opentelemetry-instrumentation-flask` will log in the foreground this conflict message: `DependencyConflict: requested: "flask >= 1.0, < 3.0" but found: "flask 3.0.0"`

The app will again still load and Otel API is still usable by the application code.

## To request - manual instrumentation

```
curl -v http://0.0.0.0:5001/test/
```

As with the bootstrapped app, the resulting trace exported to console will include one `INTERNAL` span for the call to Otel API, but will be missing the `SERVER` span expected of auto-instrumentation of a Flask app.
