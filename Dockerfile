FROM python:3.11

RUN pip install --upgrade pip

RUN pip install \
    flask==3.0.0 \
    opentelemetry-api \
    opentelemetry-sdk \
    opentelemetry-instrumentation
