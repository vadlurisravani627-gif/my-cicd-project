from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>CI/CD Pipeline Demo</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .container {
                text-align: center;
                padding: 40px;
            }
            h1 {
                font-size: 48px;
                margin-bottom: 10px;
                color: #00d4ff;
            }
            .subtitle {
                font-size: 18px;
                color: #a0a0a0;
                margin-bottom: 40px;
            }
            .cards {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
                margin-bottom: 40px;
            }
            .card {
                background: rgba(255,255,255,0.1);
                border: 1px solid rgba(255,255,255,0.2);
                border-radius: 15px;
                padding: 30px;
                width: 200px;
                backdrop-filter: blur(10px);
            }
            .card .icon { font-size: 40px; margin-bottom: 10px; }
            .card h3 { font-size: 16px; color: #00d4ff; margin-bottom: 5px; }
            .card p { font-size: 13px; color: #a0a0a0; }
            .badge {
                display: inline-block;
                background: #00d4ff;
                color: #000;
                padding: 10px 30px;
                border-radius: 25px;
                font-weight: bold;
                font-size: 16px;
                margin-bottom: 20px;
            }
            .pipeline {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 30px;
                font-size: 14px;
            }
            .step {
                background: rgba(0, 212, 255, 0.2);
                border: 1px solid #00d4ff;
                border-radius: 8px;
                padding: 8px 15px;
                color: #00d4ff;
            }
            .arrow { color: #00d4ff; font-size: 20px; }
            .version {
                margin-top: 30px;
                font-size: 13px;
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 CI/CD Pipeline</h1>
            <p class="subtitle">Automated Deployment with GitHub Actions + Docker + Render</p>

            <div class="badge">✅ Pipeline is Live & Working!</div>

            <div class="cards">
                <div class="card">
                    <div class="icon">💻</div>
                    <h3>GitHub</h3>
                    <p>Source code version control</p>
                </div>
                <div class="card">
                    <div class="icon">⚙️</div>
                    <h3>GitHub Actions</h3>
                    <p>Automated CI/CD pipeline</p>
                </div>
                <div class="card">
                    <div class="icon">🐳</div>
                    <h3>Docker</h3>
                    <p>Container packaging</p>
                </div>
                <div class="card">
                    <div class="icon">☁️</div>
                    <h3>Render</h3>
                    <p>Cloud deployment</p>
                </div>
            </div>

            <div class="pipeline">
                <div class="step">Push Code</div>
                <div class="arrow">→</div>
                <div class="step">GitHub Actions</div>
                <div class="arrow">→</div>
                <div class="step">Docker Build</div>
                <div class="arrow">→</div>
                <div class="step">Auto Deploy</div>
                <div class="arrow">→</div>
                <div class="step">Live App ✅</div>
            </div>

            <p class="version">Deployed by Sravani | BTech CSE (AI & ML)</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)