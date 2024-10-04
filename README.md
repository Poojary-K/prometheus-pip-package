# Flask Prometheus Metrics

A Python package for integrating Prometheus metrics tracking into Flask applications. This package simplifies the process of monitoring your Flask app's performance and status.

## Features

- Easy integration with Flask applications.
- Track HTTP request metrics.
- Monitor application health using Prometheus metrics.
- Supports custom metrics and gauges.

## Installation

You can install the package directly from GitLab using pip:

```bash
pip install git+https://gitlab.ird.mu-sigma.com/Poojary.K/prometheus-pip-package.git
```

## Usage

### Basic Setup

1. Import the package in your Flask application:

```python
from flask import Flask
from flask_prometheus_metrics import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Hello, World!"
```

2. Start your Flask application:

```bash
flask run
```

3. Access the metrics at the `/metrics` endpoint:

```
http://localhost:5000/metrics
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## Acknowledgements

- Flask - A micro web framework for Python.
- Prometheus - An open-source monitoring and alerting toolkit.
