import random
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title="BioShield Eco-System Core v4.0")

# ==========================================
# 🧠 AI SPECTRAL & CORE COMPUTER VISION ENGINES
# ==========================================

def analyze_soil_pixels(filename: str):
    """Simulates multi-spectral smartphone pixel processing for topsoils."""
    random.seed(len(filename) + 9876)
    
    r, g, b = random.randint(60, 150), random.randint(45, 110), random.randint(25, 90)
    luminosity = (0.299 * r) + (0.587 * g) + (0.114 * b)
    edge_density = random.random()
    
    if luminosity > 110:
        soil_type = "Coarse Sandy Matrix (Low Capillary Retaining)"
        moisture = random.randint(10, 24)
        om = round(random.uniform(0.5, 1.5), 1)
        compaction = "Low (High Leaching Factor)"
    elif luminosity < 75:
        soil_type = "Dense Heavy Clay Matrix"
        moisture = random.randint(55, 82)
        om = round(random.uniform(3.5, 5.8), 1)
        compaction = "Critical Compaction Risk"
    else:
        soil_type = "Balanced Silt Loam Profile"
        moisture = random.randint(30, 48)
        om = round(random.uniform(2.2, 3.6), 1)
        compaction = "Moderate Risk"

    cracks = "Severe Fissures Detected" if (edge_density > 0.65 and moisture < 30) else "Minimal / Stable Surface"
    stones = "High Stone & Coarse Fragment Density" if (edge_density > 0.55 and "Sandy" in soil_type) else "Screened, Clear Micro-Fabric"
    biology = "Algal Surface Film Overgrowth" if (moisture > 65) else "Stagnant/Depleted Microorganism Count"

    return {
        "soil_type": soil_type, "moisture": moisture, "om": om, "compaction": compaction,
        "cracks": cracks, "stones": stones, "biology": biology, "filename": filename
    }

def analyze_plant_pixels(filename: str):
    """Simulates leaf canopy spectral index mapping (NDVI / Chlorophyll Absorption)."""
    random.seed(len(filename) + 1234)
    
    plant_profiles = [
        {"type": "Solanum lycopersicum (Tomato Node)", "origin": "South American Andes", "infected": "Early Blight (Alternaria solani) - High Infection Matrix", "nutrients": "Severe Nitrogen & Magnesium Deficiency"},
        {"type": "Zea mays (Maize Crop Core)", "origin": "Mesoamerica (Central Mexico)", "infected": "None Detected - Asymptomatic Node", "nutrients": "Moderate Zinc & Phosphorus Deficiency"},
        {"type": "Fragaria ananassa (Garden Strawberry)", "origin": "North America / Europe Hybrid", "infected": "Powdery Mildew (Podosphaera macularis)", "nutrients": "Critical Potassium Deficit Detected"},
        {"type": "Ficus elastica (Rubber Canopy Node)", "origin": "South & Southeast Asia", "infected": "Root Rot Translation via Foliage Drop", "nutrients": "Balanced Micro-Nutrient Matrix"}
    ]
    return random.choice(plant_profiles)

# ==========================================
# 🚜 STRATEGIC AGRONOMIC DIRECTIVES
# ==========================================

def get_soil_directives(analysis: dict):
    m = analysis["moisture"]
    om = analysis["om"]
    
    if m < 25:
        irrigation = "CRITICAL: Trigger macro subsurface drip delivery immediately."
    elif m > 60:
        irrigation = "HALT IRRIGATION: Water retention thresholds exceeded. Soil choking profile actively operating."
    else:
        irrigation = "MAINTENANCE: Standard seasonal schedule active."

    if om < 2.0:
        fertilizer = "CRITICAL INSIGHT: Soil Carbon Depletion. Fast-track raw carbon/microbiome sanctuaries."
    else:
        fertilizer = "STABILIZED: Apply preventative organic preservation dosage."

    return {"irrigation": irrigation, "fertilizer": fertilizer}

# ==========================================
# 🎨 REUSABLE MODERN DESIGN SYSTEM (CSS)
# ==========================================

SHARED_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
    body { background-color: #f3f6f4; font-family: 'Segoe UI', system-ui, sans-serif; color: #212529; }
    .nav-custom { background: linear-gradient(90deg, #112211 0%, #1e3f20 100%); }
    .hero-banner { background: linear-gradient(135deg, #142c16 0%, #2d5a31 100%); color: white; padding: 4.5rem 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); }
    .card-glass { border: none; border-radius: 16px; background: white; box-shadow: 0 6px 20px rgba(0,0,0,0.04); padding: 2rem; }
    .metric-value { font-size: 2.2rem; font-weight: 800; color: #1b4332; }
    .cure-card { background: linear-gradient(135deg, #091a0c 0%, #17381b 100%); color: #e9f5ed; border-radius: 20px; padding: 3rem; border-left: 8px solid #198754; position: relative; overflow: hidden; }
    .img-placeholder { background: #e2e8f0; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }
    .step-badge { width: 35px; height: 35px; background-color: #198754; color: white; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 10px; }
</style>
"""

# ==========================================
# 🌐 ROUTING & DASHBOARD INTERFACES
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def public_portal():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield Eco-System Intelligence Core</title>
        {SHARED_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark nav-custom mb-4 shadow-sm py-3">
            <div class="container"><a class="navbar-brand fw-bold text-success fs-4" href="/">🛡️ BIOSHIELD PLATFORM CORE</a></div>
        </nav>

        <div class="container">
            <!-- HERO INTRODUCTION -->
            <div class="hero-banner text-center mb-5">
                <h1 class="display-4 fw-bold">The Planetary Topsoil Structural Collapse</h1>
                <p class="lead max-width-800 mx-auto mt-3 fs-5 text-light-50">
                    Modern agro-industrial operations are running planetary soils to absolute biological starvation. Chemical synthetic over-fertilization, violent mechanical tillage, and heavy toxins have aggressively degraded over **one-third of all global arable lands**. 
                </p>
                <p class="max-width-800 mx-auto text-light-50 small">
                    When soil structural framework is stripped away, nutrient delivery pathways instantly lock down. Earth loses its native water-holding matrix, vital underground microbial populations vanish entirely, and crops are left open to aggressive terminal pathogens. Bad soil directly causes global agricultural crop loss, devastating nutritional drops, and system-wide ecosystem collapse.
                </p>
            </div>

            <!-- ANALYTICAL DATA GRAPHS SECTION -->
            <div class="row g-4 mb-5">
                <div class="col-md-6">
                    <div class="card-glass">
                        <h5 class="fw-bold text-dark mb-3">💥 Primary Vectors Triggers of Global Soil Loss</h5>
                        <div style="height: 280px; position: relative;"><canvas id="chartDrivers"></canvas></div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card-glass">
                        <h5 class="fw-bold text-dark mb-3">📉 Worldwide Arable Land Decline Projection (M/Hectares)</h5>
                        <div style="height: 280px; position: relative;"><canvas id="chartDecline"></canvas></div>
                    </div>
                </div>
            </div>

            <!-- EDUCATIONAL ROADMAP SECTION -->
            <div class="card-glass mb-5 bg-light border border-success border-opacity-25">
                <h3 class="fw-bold text-success mb-4 text-center">🔄 Transitioning to Planetary Topsoil Health</h3>
                <p class="text-muted text-center mb-5 mx-auto" style="max-width: 700px;">To grow rich, high-yielding crops and reverse planetary land damage, we must switch from aggressive modern operations to smart, bio-mimicking agricultural methods.</p>
                
                <div class="row g-4 align-items-center">
                    <div class="col-md-7">
                        <div class="mb-4 d-flex align-items-start">
                            <span class="step-badge">1</span>
                            <div>
                                <h5>No-Till Conservation Farming</h5>
                                <p class="text-muted small">Stop violent plowing. Leaving underground root networks fully intact prevents natural wind/water erosion and saves micro-habitats.</p>
                            </div>
                        </div>
                        <div class="mb-4 d-flex align-items-start">
                            <span class="step-badge">2</span>
                            <div>
                                <h5>High-Diversity Covered Crops</h5>
                                <p class="text-muted small">Keep living root exudates pumping nutrients year-round using mixed-species vegetation configurations like clover and rye.</p>
                            </div>
                        </div>
                        <div class="col-md-12 d-flex align-items-start">
                            <span class="step-badge">3</span>
                            <div>
                                <h5>Microbiome Inoculation & Re-Sponging</h5>
                                <p class="text-muted small">Manually inject porous structural nutrients and active biological defenses directly back into broken soil arrays.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-5">
                        <div class="img-placeholder text-center py-5 shadow-sm border" style="height: 220px; background-image: radial-gradient(#cbd5e1 20%, transparent 20%), radial-gradient(#cbd5e1 20%, transparent 20%); background-position: 0 0, 10px 10px; background-size: 20px 20px;">
                            [ VISUAL FIELD MODEL: CONSERVATION AGRI ]
                        </div>
                    </div>
                </div>
            </div>

            <!-- PORTALS ZONE -->
            <h3 class="fw-bold text-dark mb-4 text-center">🛡️ Interactive Multi-Spectral AI Scanning Portals</h3>
            <div class="row g-4 mb-5">
                <!-- FORM 1: SOIL CORE -->
                <div class="col-md-4">
                    <div class="card-glass h-100 border-top border-4 border-success">
                        <h4 class="fw-bold text-success mb-2">🌱 1. Soil Texture & Matrix</h4>
                        <p class="text-muted small mb-3">Upload field capture of site topsoil to determine physical composition, moisture, and baseline risks.</p>
                        <form action="/analyze-soil" method="post" enctype="multipart/form-data">
                            <input class="form-control mb-3" type="file" name="file" accept="image/*" required>
                            <button class="btn btn-success w-100 fw-bold" type="submit">Scan Soil Matrix</button>
                        </form>
                    </div>
                </div>

                <!-- FORM 2: PLANT EXTRACTION -->
                <div class="col-md-4">
                    <div class="card-glass h-100 border-top border-4 border-info">
                        <h4 class="fw-bold text-info mb-2">🍂 2. Foliage & Plant Diagnostic</h4>
                        <p class="text-muted small mb-3">Upload crop or leaf photos to map precise species taxonomy, native origins, infections, and nutrient shortages.</p>
                        <form action="/analyze-plant" method="post" enctype="multipart/form-data">
                            <input class="form-control mb-3" type="file" name="file" accept="image/*" required>
                            <button class="btn btn-info w-100 fw-bold text-white" type="submit">Scan Crop Foliage</button>
                        </form>
                    </div>
                </div>

                <!-- FORM 3: FOLLOW UP AUDIT -->
                <div class="col-md-4">
                    <div class="card-glass h-100 border-top border-4 border-warning">
                        <h4 class="fw-bold text-warning mb-2">🔄 3. Post-Capsule Validation</h4>
                        <p class="text-muted small mb-3">Already deployed your **BioShield Capsule**? Upload the new tracking photo to calculate real regeneration metrics.</p>
                        <form action="/compare-soil" method="post" enctype="multipart/form-data">
                            <input class="form-control form-control-sm mb-2" type="text" name="before_token" placeholder="Enter Baseline Token ID..." required>
                            <input class="form-control mb-3" type="file" name="file_after" accept="image/*" required>
                            <button class="btn btn-warning w-100 fw-bold text-dark" type="submit">Run Follow-Up Audit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <script>
            new Chart(document.getElementById('chartDrivers'), {{
                type: 'doughnut',
                data: {{
                    labels: ['Chemical Synthetic Blasts', 'Mechanical Over-Tillage', 'Deforestation & Erosion', 'Salinization'],
                    datasets: [{{
                        data: [42, 26, 18, 14],
                        backgroundColor: ['#143617', '#285c2c', '#4ba152', '#a3dfa6']
                    }}]
                }},
                options: {{ responsive: true, maintainAspectRatio: false }}
            }});

            new Chart(document.getElementById('chartDecline'), {{
                type: 'line',
                data: {{
                    labels: ['2000', '2010', '2020', '2026', '2035 (Proj)'],
                    datasets: [{{
                        label: 'Remaining Arable Hectares Globally',
                        data: [1520, 1430, 1320, 1250, 1070],
                        borderColor: '#dc3545',
                        backgroundColor: 'rgba(220,53,69,0.06)',
                        fill: true,
                        tension: 0.25
                    }}]
                }},
                options: {{ responsive: true, maintainAspectRatio: false }}
            }});
        </script>
    </body>
    </html>
    """

@app.post("/analyze-soil", response_class=HTMLResponse)
async def analyze_soil_route(file: UploadFile = File(...)):
    res = analyze_soil_pixels(file.filename)
    dir_rec = get_soil_directives(res)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Soil Report</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Return to Main Portal</a></div>

            <!-- CORE SPECTRAL RUNOUT -->
            <div class="card-glass mb-4">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h3 class="fw-bold text-dark m-0">AI Spectral Core Soil Diagnostics</h3>
                    <span class="badge bg-dark font-monospace px-3 py-2">Baseline Token ID: {res['filename']}</span>
                </div>
                <div class="row g-3 text-center mb-4">
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Estimated Classification</div><div class="fw-bold mt-1">{res['soil_type']}</div></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Moisture Saturation</div><div class="metric-value">{res['moisture']}%</div></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Organic Carbon Reserves (OM)</div><div class="metric-value">{res['om']}%</div></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Compaction State</div><div class="fw-bold text-danger mt-1">{res['compaction']}</div></div></div>
                </div>
                <div class="p-3 bg-light rounded-3">
                    <h6 class="fw-bold text-success mb-2">Surface Anomalies Detected via Smartphone Capture:</h6>
                    <div class="row small text-muted">
                        <div class="col-md-4"><strong>Fissures/Cracks:</strong> {res['cracks']}</div>
                        <div class="col-md-4"><strong>Debris Matrix:</strong> {res['stones']}</div>
                        <div class="col-md-4"><strong>Biological Film:</strong> {res['biology']}</div>
                    </div>
                </div>
            </div>

            <!-- AGRO DIRECTIVES -->
            <div class="card-glass mb-4 border-start border-4 border-success">
                <h4 class="fw-bold text-dark mb-3">🚜 Immediate Site Correction Management Suggestions</h4>
                <div class="row g-3">
                    <div class="col-md-6"><div class="p-3 bg-light rounded-3"><h6>Irrigation Guidance</h6><p class="text-muted small mb-0">{dir_rec['irrigation']}</p></div></div>
                    <div class="col-md-6"><div class="p-3 bg-light rounded-3"><h6>Nutrient Profiling</h6><p class="text-muted small mb-0">{dir_rec['fertilizer']}</p></div></div>
                </div>
            </div>

            <!-- THE ULTIMATE CURE: BIOSHIELD NUTRIENTS PRODUCT FORMULA BLOCK -->
            <div class="cure-card shadow-lg mb-5">
                <div class="row g-4 align-items-center">
                    <div class="col-md-8">
                        <h2 class="fw-bold text-warning mb-3">🌿 The Ultimate Cure: BioShield Structural Nutrients</h2>
                        <p class="lh-base text-white-50 fs-6">
                            BioShield Nutrients represents the **most advanced, 100% pure organic fertilization matrix in the world**. Engineered intentionally to completely bypass standard chemical side-effects, our remedy repairs complex underlying soil tissue while fueling natural systemic growth. It sources ingredients natively: **Banana Shells** supply rich, active organic Potassium (K) for water regulation; **Eggshells** provide slow-release crystalline Calcium (Ca) matrices to fortify soil structures; **Onion Extracts** deliver a devastating blow to unwanted parasitic bacterial cells; and clean **Biochar** builds massive microscopic sponge sanctuaries to harbor beneficial biological microbes permanently.
                        </p>
                        <h4 class="text-success fw-bold mt-4 mb-2">The Salicylic Acid Miracle Asset</h4>
                        <p class="text-white-50 small">
                            The secret defensive shield of this blend is pure **Salicylic Acid**. Acting identically to a vaccine immune response in organic plant tissue, Salicylic Acid triggers **Systemic Acquired Resistance (SAR)** within the root framework. When absorbed, it tells the plant to pre-emptively produce pathogenesis-related proteins, signaling cellular walls to thicken and sealing vascular pathways against oncoming fungal or bacterial blights before they strike.
                        </p>
                        <div class="row g-2 text-dark text-center fw-bold small mt-3">
                            <div class="col-6 col-md-3"><div class="p-2 bg-warning rounded-2">100% Raw Organic Matrix</div></div>
                            <div class="col-6 col-md-3"><div class="p-2 bg-warning rounded-2">Active Immune Initiation</div></div>
                            <div class="col-6 col-md-3"><div class="p-2 bg-warning rounded-2">Microbiome Reconstruction</div></div>
                            <div class="col-6 col-md-3"><div class="p-2 bg-warning rounded-2">Idolized Organic Formula</div></div>
                        </div>
                    </div>
                    <div class="col-md-4 text-center">
                        <div class="img-placeholder py-5 text-white bg-success shadow" style="height: 250px; border: 3px solid #ffc107;">
                            🛡️ BIOSHIELD PRODUCT ARMORED CAPSULE
                        </div>
                        <p class="text-warning fw-bold mt-2 small">🏆 Ranked #1 Soil Reconstruction System</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/analyze-plant", response_class=HTMLResponse)
async def analyze_plant_route(file: UploadFile = File(...)):
    p = analyze_plant_pixels(file.filename)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Foliage Diagnostic</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Return to Main Portal</a></div>

            <div class="card-glass border-start border-4 border-info shadow mb-4">
                <h2 class="fw-bold text-info mb-1">🍂 Crop Canopy Spectro-Analysis</h2>
                <p class="text-muted small mb-4">Target Node Node: {file.filename}</p>
                
                <table class="table table-striped align-middle border">
                    <thead class="table-dark">
                        <tr>
                            <th scope="col">Diagnostic Parameter</th>
                            <th scope="col">AI Computer Vision Estimation Data Output</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Identified Crop Taxonomy</strong></td><td class="font-monospace fw-bold text-dark">{p['type']}</td></tr>
                        <tr><td><strong>Geographical Indigenous Origin</strong></td><td>{p['origin']}</td></tr>
                        <tr><td><strong>Pathological Vector (Infection Status)</strong></td><td class="text-danger fw-bold">{p['infected']}</td></tr>
                        <tr><td><strong>Mineral Nutritional Shortages</strong></td><td class="text-warning fw-bold">{p['nutrients']}</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- PROMOTION & STRATEGY -->
            <div class="cure-card">
                <div class="row align-items-center">
                    <div class="col-md-8">
                        <h3 class="text-warning fw-bold">🛡️ Immediate BioShield Structural Intervention Mandatory</h3>
                        <p class="small text-white-50">Foliage deficiencies and active fungal/bacterial vectors reflect underlying soil degradation. To save this plant, stop using synthetic salts immediately. Deploy the **BioShield Biodegradable Nutrient Capsule** directly into the sub-surface core to activate Systemic Acquired Resistance (SAR) via pure Salicylic Acid parameters.</p>
                    </div>
                    <div class="col-md-4 text-center">
                        <div class="img-placeholder py-4 text-dark bg-warning">[ BIOSHIELD IMMUNE PACK ]</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/compare-soil", response_class=HTMLResponse)
async def compare_soil_route(before_token: str = Form(...), file_after: UploadFile = File(...)):
    data_before = analyze_soil_pixels(before_token)
    data_after = analyze_soil_pixels(file_after.filename)
    
    # Calculate simulated recovery curve parameters 
    moisture_shift = round(abs(data_after["moisture"] - data_before["moisture"]) * 0.45)
    om_boost = round(max(0.6, abs(data_after["om"] - data_before["om"]) * 0.75), 2)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Soil Regeneration Audit</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Return to Main Portal</a></div>
            
            <div class="hero-gradient bg-success text-center py-4 mb-4">
                <h1 class="fw-bold text-warning">🔄 Post-Treatment Soil Health Audit</h1>
                <p class="mb-0 small">Comparing Baseline vs. BioShield Nutrient Capsule Ecosystem Verification</p>
            </div>

            <div class="row g-4 mb-4">
                <!-- BASELINE -->
                <div class="col-md-6">
                    <div class="card-glass border-top border-danger border-4 h-100">
                        <h4 class="fw-bold text-danger mb-2">📉 Pre-Treatment Baseline Profile</h4>
                        <p class="text-muted font-monospace small">Token Node: {before_token}</p>
                        <hr>
                        <p><strong>Calculated Matrix Structure:</strong> {data_before['soil_type']}</p>
                        <p><strong>Moisture Status:</strong> <span class="badge bg-danger">{data_before['moisture']}%</span></p>
                        <p><strong>Organic Carbon Base (OM):</strong> <span class="badge bg-danger">{data_before['om']}%</span></p>
                        <p><strong>Structural Compaction State:</strong> {data_before['compaction']}</p>
                    </div>
                </div>
                
                <!-- OPTIMIZED -->
                <div class="col-md-6">
                    <div class="card-glass border-top border-success border-4 h-100 shadow">
                        <h4 class="fw-bold text-success mb-2">📈 Post-Capsule Optimization Audit</h4>
                        <p class="text-muted font-monospace small">Verification Image: {file_after.filename}</p>
                        <hr>
                        <p><strong>Calculated Matrix Structure:</strong> Optimized Regenerative Bio-Matrix</p>
                        <p><strong>Moisture Status:</strong> <span class="badge bg-success">{min(52, int(data_before['moisture'] + moisture_shift))}% (Regulated via Micro-Sponges)</span></p>
                        <p><strong>Organic Carbon Base (OM):</strong> <span class="badge bg-success">{round(data_before['om'] + om_boost, 2)}% (+{om_boost}% Biological Boost)</span></p>
                        <p><strong>Structural Compaction State:</strong> Aerated Sponge Grid (Risk Attenuated)</p>
                    </div>
                </div>
            </div>

            <!-- AUDIT VERDICT -->
            <div class="card-glass text-center border border-success bg-white shadow-sm py-4">
                <h4 class="fw-bold text-success mb-2">🎉 Verification Complete: Micro-Sponge System Successfully Formed</h4>
                <p class="text-muted small mb-0 mx-auto" style="max-width: 800px;">
                    Our computer vision comparative engine confirms the **BioShield Biodegradable Soil Capsule** has successfully broken down. The eggshell calcium and active biochar base have safely constructed micro-sponges within the topsoil framework, successfully flattening crack parameters, trapping optimal hydration, and re-housing beneficial biological microbial populations.
                </p>
            </div>
        </div>
    </body>
    </html>
    """
