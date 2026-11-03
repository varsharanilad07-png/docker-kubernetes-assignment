from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Docker Kubernetes Demo</title>
        </head>
        <body>
            <h1>Cloud Native Application</h1>
            <h2>Docker + Kubernetes</h2>
            <p>Application deployed successfully!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)