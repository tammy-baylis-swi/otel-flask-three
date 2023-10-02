from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from opentelemetry.instrumentation.flask import FlaskInstrumentor

FlaskInstrumentor().instrument(enable_commenter=True, commenter_options={})

app = Flask(__name__)
tracer = trace.get_tracer(__name__)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

@app.route("/test/")
def test():
    with tracer.start_as_current_span("my_test_trace"):
        return "Done"
