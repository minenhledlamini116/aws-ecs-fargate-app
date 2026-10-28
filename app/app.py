import os
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

BUILD = os.getenv("GIT_SHA", "dev")[:7]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Container demo</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #111827;
      color: #e5e7eb;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
    }
    .card {
      background: #1f2937;
      padding: 2rem 3rem;
      border-radius: 12px;
      text-align: center;
    }
    h1 { color: #34d399; margin-top: 0; }
    code { background: #374151; padding: 2px 8px; border-radius: 6px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Running on ECS Fargate v2</h1>
    <p>Container ID: <code>{{ host }}</code></p>
    <p>Build: <code>{{ build }}</code></p>
    <p>Time: {{ now }}</p>
    <p>Refresh the page to see which container answers.</p>
  </div>
</body>
</html>
"""


@app.route("/")
def home():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return render_template_string(PAGE, host=socket.gethostname(), build=BUILD, now=now)


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/info")
def info():
    return jsonify(host=socket.gethostname(), build=BUILD)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
