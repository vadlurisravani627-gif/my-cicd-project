from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: #f0f8ff;">
            <h1> My CI/CD Pipeline Project</h1>
            <p><p>Deployed automatically using GitHub Actions + Docker + Render! 🚀</p>
            <p style="color: green;">✅ Pipeline is working!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)