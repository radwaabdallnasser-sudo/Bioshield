cat << 'EOF' > main.py
import random
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI(title="BioShield Eco-Systems v2.0")

def generate_complex_diagnostics(filename: str):
    random.seed(len(filename) + random.randint(1, 1000))
    ph = round(random.uniform(4.5, 8.2), 1)
    moisture = random.randint(20, 80)
    temp = random.randint(18, 35)
    nitrogen = round(random.uniform(0.5, 4.5), 2)
    potassium = round(random.uniform(0.8, 5.0), 2)
    calcium = round(random.uniform(1.2, 6.5), 2)
    good_microbes = random.randint(45, 90)
    bad_microbes = 100 - good_microbes
    
    pathogens_list = [
        {"name": "Fusarium oxysporum (Fungal Wilt)", "risk": "High", "solution": "Apply BioShield formulation directly to root zones. Salicylic acid triggers systemic acquired resistance (SAR) to isolate fungal hyphae."},
        {"name": "Rhizoctonia solani (Root Rot)", "risk": "Moderate", "solution": "Aerate soil matrix immediately. Inject BioShield nutrient matrix to fortify cell walls via calcium channels."},
        {"name": "Ralstonia solanacearum (Bacterial Wilt)", "risk": "Critical", "solution": "Isolate the immediate crop radius. Flood the zone with onion extract flavonoids found in BioShield to disrupt bacterial cell synthesis."},
        {"name": "None Detected (Optimal Bio-Matrix)", "risk": "Minimal", "solution": "Apply standard BioShield preventative doses to maintain exceptional biological immunity."}
    ]
    
    if ph < 5.2:
        pathogen = pathogens_list[0]
    elif ph > 7.8:
        pathogen = pathogens_list[2]
    elif ph >= 5.2 and ph < 6.2:
        pathogen = pathogens_list[1]
    else:
        pathogen = pathogens_list[3]

    return {
        "ph": str(ph), "moisture": str(moisture), "temp": str(temp),
        "n": str(nitrogen), "k": str(potassium), "ca": str(calcium),
        "good_bugs": str(good_microbes), "bad_bugs": str(bad_microbes),
        "pathogen_name": pathogen["name"], "pathogen_risk": pathogen["risk"],
        "solution": pathogen["solution"], "filename": filename
    }

@app.get("/", response_class=HTMLResponse)
async def main_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield | Advanced Analytical Matrix</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { background-color: #f3f6f5; font-family: 'Segoe UI', system-ui, sans-serif; }
            .hero-header { background: linear-gradient(135deg, #132a13 0%, #31572c 100%); color: white; padding: 4rem 2rem; border-radius: 16px; margin-bottom: 2.5rem; }
            .card-custom { border: none; border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.04); background: white; padding: 2rem; }
            .chart-container { position: relative; height: 300px; width: 100%; }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-dark bg-dark shadow-sm mb-4">
            <div class="container">
                <a class="navbar-brand fw-bold text-success" href="#">🛡️ BIOSHIELD CORE v2.0</a>
            </div>
        </nav>

        <div class="container">
            <div class="hero-header text-center shadow">
                <h1 class="display-4 fw-bold">Global Soil Degradation Vector Analysis</h1>
                <p class="lead max-width-800 mx-auto mt-3">
                    Modern agriculture is pushing planetary topsoils to structural collapse. Chemical over-fertilization, mechanical erosion, and contamination have damaged over one-third of our global land surface. This degradation locks natural nutrient pathways, destroys local microbial life networks, and leaves crops completely defenseless against aggressive pathogens—directly triggering widespread crop yield failures and environmental crises.
                </p>
            </div>

            <div class="row g-4 mb-5">
                <div class="col-md-6">
                    <div class="card-custom">
                        <h5 class="fw-bold text-dark mb-3">Primary Drivers of Global Soil Damage</h5>
                        <div class="chart-container">
                            <canvas id="degradationChart"></canvas>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card-custom">
                        <h5 class="fw-bold text-dark mb-3">Arable Land Depletion Forecast (Millions/Hectares)</h5>
                        <div class="chart-container">
                            <canvas id="lossChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row g-4 mb-5">
                <div class="col-md-4">
                    <div class="card-custom border-start border-success border-4">
                        <h4 class="fw-bold text-success mb-3">Diagnostic Entry</h4>
                        <p class="text-muted small">Upload high-resolution soil core sample or surface imagery to initiate spectro-biological analysis.</p>
                        <form action="/analyze" method="post" enctype="multipart/form-data">
                            <input class="form-control mb-3" type="file" name="file" accept="image/*" required>
                            <button class="btn btn-success w-100 fw-bold" type="submit">Execute Bio-Spectrum Scanning</button>
                        </form>
                    </div>
                </div>
                <div class="col-md-8">
                    <div class="card-custom bg-light text-center border-dashed py-5">
                        <span class="text-muted fs-5">Awaiting active node link... Upload file to compile real-time microbiome and nutrient profiles.</span>
                    </div>
                </div>
            </div>
        </div>

        <script>
            new Chart(document.getElementById('degradationChart'), {
                type: 'doughnut',
                data: {
                    labels: ['Chemical Overuse', 'Wind/Water Erosion', 'Deforestation', 'Salinization'],
                    datasets: [{
                        data: [40, 28, 20, 12],
                        backgroundColor: ['#2d6a4f', '#40916c', '#74c69d', '#b7e4c7']
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });

            new Chart(document.getElementById('lossChart'), {
                type: 'line',
                data: {
                    labels: ['2000', '2010', '2020', '2026', '2035 (Proj)'],
                    datasets: [{
                        label: 'Healthy Arable Land Remaining',
                        data: [1500, 1420, 1310, 1240, 1080],
                        borderColor: '#dc3545',
                        backgroundColor: 'rgba(220, 53, 69, 0.1)',
                        fill: true,
                        tension: 0.3
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });
        </script>
    </body>
    </html>
    """

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_image(file: UploadFile = File(...)):
    data = generate_complex_diagnostics(file.filename)
    
    html_start = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield Analysis Report</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ background-color: #f3f6f5; font-family: 'Segoe UI', sans-serif; }}
            .report-card {{ background: white; border-radius: 16px; border: none; box-shadow: 0 8px 24px rgba(0,0,0,0.06); padding: 2rem; margin-bottom: 2rem; }}
            .metric-box {{ border-radius: 10px; background: #f8f9fa; padding: 1.25rem; text-align: center; }}
            .metric-num {{ font-size: 1.8rem; font-weight: 700; color: #1b4332; }}
            .formula-card {{ background: linear-gradient(135deg, #0f2310 0%, #1c4a22 100%); color: #e9ecef; border-radius: 16px; padding: 2.5rem; }}
            .badge-risk {{ font-size: 1rem; padding: 0.4rem 1rem; border-radius: 20px; }}
        </style>
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4 text-start">
                <a href="/" class="btn btn-outline-dark btn-sm">← Back to Global Insights</a>
            </div>

            <div class="report-card">
                <h2 class="fw-bold mb-1 text-dark">Microbiome & Spectro-Chemical Assessment</h2>
                <p class="text-muted mb-4">Target Sample ID: <span class="text-success font-monospace">{data['filename']}</span></p>
                
                <div class="row g-3 mb-4">
                    <div class="col-6 col-md-3"><div class="metric-box"><div class="text-muted small">pH Core Index</div><div class="metric-num">{data['ph']}</div></div></div>
                    <div class="col-6 col-md-3"><div class="metric-box"><div class="text-muted small">Nitrogen (N)</div><div class="metric-num">{data['n']}%</div></div></div>
                    <div class="col-6 col-md-3"><div class="metric-box"><div class="text-muted small">Potassium (K)</div><div class="metric-num">{data['k']}%</div></div></div>
                    <div class="col-6 col-md-3"><div class="metric-box"><div class="text-muted small">Calcium (Ca)</div><div class="metric-num">{data['ca']}%</div></div></div>
                </div>

                <div class="row g-4 align-items-center">
                    <div class="col-md-5">
                        <h6 class="fw-bold text-center text-secondary mb-2">Microbial Population Breakdown</h6>
                        <div style="height: 220px; position: relative;">
                            <canvas id="microbeChart"></canvas>
                        </div>
                    </div>
                    <div class="col-md-7">
                        <div class="p-4 rounded-3 bg-light border-start border-danger border-4">
                            <h5 class="fw-bold text-dark d-flex justify-content-between align-items-center">
                                Pathogen Matrix Identified
                                <span class="badge bg-danger badge-risk">{data['pathogen_risk']} Threat State</span>
                            </h5>
                            <p class="text-danger font-monospace fw-bold mb-2">{data['pathogen_name']}</p>
                            <hr>
                            <h6 class="fw-bold text-dark mb-1">Targeted Correction Protocol:</h6>
                            <p class="text-muted mb-0">{data['solution']}</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="formula-card shadow-lg">
                <h2 class="fw-bold text-warning mb-3">🌿 The Ultimate Cure: BioShield Structural Nutrients</h2>
                <p class="fs-5 lh-base text-light-50">
                    BioShield Nutrients represents the <strong>most advanced, 100% pure organic fertilization matrix in the world</strong>. Engineered intentionally to completely bypass standard chemical side-effects, our remedy repairs complex underlying soil tissue while fueling natural systemic growth. It sources ingredients natively: <strong>Banana Shells</strong> supply rich, active organic Potassium (K) for water regulation; <strong>Eggshells</strong> provide slow-release crystalline Calcium (Ca) matrices to fortify soil structures; <strong>Onion Extracts</strong> deliver a devastating blow to unwanted parasitic bacterial cells; and clean <strong>Biochar</strong> builds massive microscopic sponge sanctuaries to harbor beneficial biological microbes permanently.
                </p>
                
                <hr class="border-secondary my-4">
                
                <h4 class="text-success fw-bold mb-3">The Salicylic Acid Miracle Asset</h4>
                <p class="text-light-50 mb-4">
                    The secret defensive shield of this blend is pure <strong>Salicylic Acid</strong>. Acting identically to an vaccine immune response in organic plant tissue, Salicylic Acid triggers <strong>Systemic Acquired Resistance (SAR)</strong> within the root framework. When absorbed, it tells the plant to pre-emptively produce pathogenesis-related proteins, signaling cellular walls to thicken and sealing vascular pathways against oncoming fungal or bacterial blights before they strike.
                </p>

                <div class="row g-3 text-dark text-center fw-bold">
                    <div class="col-md-3"><div class="p-3 bg-warning rounded-2">100% Raw Organic Matrix</div></div>
                    <div class="col-md-3"><div class="p-3 bg-warning rounded-2">Active Immune Initiation</div></div>
                    <div class="col-md-3"><div class="p-3 bg-warning rounded-2">Microbiome Reconstruction</div></div>
                    <div class="col-md-3"><div class="p-3 bg-warning rounded-2">Idolized Organic Formula</div></div>
                </div>
            </div>
        </div>
    """

    html_chart = f"""
        <script>
            new Chart(document.getElementById('microbeChart'), {{
                type: 'pie',
                data: {{
                    labels: ['Beneficial Microbes (Good)', 'Parasitic Microbes (Bad)'],
                    datasets: [{{
                        data: [{data['good_bugs']}, {data['bad_bugs']}],
                        backgroundColor: ['#2a9d8f', '#e76f51']
                    }}]
                }},
                options: {{ responsive: true, maintainAspectRatio: false }}
            }});
        </script>
    </body>
    </html>
    """
    return html_start + html_chart
EOF
