from flask import Flask, Response
from prometheus_client import Counter, Gauge, generate_latest

class PrometheusMetrics:
    def __init__(self, app: Flask):
        self.http_request_counter = Counter(
            'http_requests_total', 
            'Total number of HTTP requests with status codes 4xx and 5xx',
            ['method', 'route', 'status']
        )

        self.server_status_gauge = Gauge(
            'server_status',
            'Gauge for monitoring server up/down status. 1 means up, 0 means down.'
        )

        self.server_status_gauge.set(1)  # Set initial server status to up

        @app.after_request
        def after_request(response):
            if 400 <= response.status_code < 600:
                self.http_request_counter.labels(
                    method=request.method,
                    route=request.path,
                    status=response.status_code
                ).inc()
            return response

        # Endpoint to expose metrics
        @app.route('/metrics')
        def metrics():
            return Response(generate_latest(), mimetype='text/plain')

        # Handle server shutdown
        import atexit
        atexit.register(self.shutdown)

    def shutdown(self):
        self.server_status_gauge.set(0)  # Set server status to down

    def set_server_status(self, status: bool):
        self.server_status_gauge.set(1 if status else 0)
