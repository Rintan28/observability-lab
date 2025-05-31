from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(_name_)

HTTP_REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['status'])

@app.route('/')
def index():
    import random
    if random.randint(0, 10) < 2:
        HTTP_REQUESTS.labels(status='500').inc()
        return "Internal Server Error", 500
    HTTP_REQUESTS.labels(status='200').inc()
    return "Hello, World!", 200

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)