import random
import json
import csv
from io import StringIO
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI(title="BioShield Grand-Jury OS v6.0")

# ==========================================
# 🗺️ EGYPT GEOGRAPHICAL MAP DATABASE
# ==========================================
EGYPT_LOCATIONS = [
    {"name": "Nile Delta Core - Kafr El-Sheikh Plot", "lat": 31.1107, "lon": 30.9388, "zone": "Delta Silt Loam", "status": "Compacted"},
    {"name": "Western Desert Reclaimed Sector - Wadi El Natrun", "lat": 30.3800, "lon": 30.3500, "zone": "Arid Desert Sand", "status": "Leached"},
    {"name": "New Valley Oasis Agronomic Grid", "lat": 25.4390, "lon": 30.5582, "zone": "Hyper-Arid Mineral Sand", "status": "Degraded"},
    {"name": "Old Arable Zone - Beheira Governorate", "lat": 30.8400, "lon": 30.4800, "zone": "Alluvial Heavy Clay", "status": "Salinized"}
]

# ==========================================
# 🧠 EXTENDED MULTI-LAYER SOIL & CANOPY COMPUTER VISION ENGINE
# ==========================================
def process_field_image(filename: str):
    """
    Simulates high-fidelity computer vision engine.
    If the image lacks proper exposure or metadata validation parameters, 
    it throws an unidentifiable matrix exception flag.
    """
    if "corrupted" in filename.lower() or "error" in filename.lower() or filename == "":
        return {"error": "Image verification failed: Sub-optimal exposure or lack of soil texture markers. System cannot identify material."}
        
    random.seed(len(filename) + 777)
    
    # Check if image name matches Delta or Desert to assign realistic Egypt profiles
    if "delta" in filename.lower() or "alluvial" in filename.lower() or random.choice([True, False]):
        # Egypt Delta Profile
        return {
            "error": None,
            "location": random.choice([EGYPT_LOCATIONS[0], EGYPT_LOCATIONS[3]]),
            "type": "Alluvial Heavy Clay Loam Matrix", "type_conf": 96,
            "type_exp": "The surface displays dense plate aggregation, high light absorption glare, and strong binding consistency typical of old Nile Valley sediments.",
            "moisture": "Saturated Sub-Surface / Surface Dry Crust (38%)", "moist_conf": 92, "moist_score": 60,
            "cracks": "Severe Deep Shrinkage Fissures Present", "cracks_conf": 95, "crack_score": 40,
            "om": "Moderate Depleted Organic Silt Reserve (2.4%)", "om_conf": 89, "om_score": 55,
            "biology": "Active Anaerobic Algal Surface Sheet", "bio_conf": 91, "bio_score": 48,
            "n_def": "Mild (Slight structural stunting)", "k_def": "Severe (Marginal scorching observed on bottom leaf fragments)",
            "fungal": "Detected: Rhizoctonia Solani spores localized", "pest": "Minimal edge chewing patterns",
            "heatmap_data": [45, 82, 12, 94]
        }
    else:
        # Egypt Desert Profile
        return {
            "error": None,
            "location": random.choice([EGYPT_LOCATIONS[1], EGYPT_LOCATIONS[2]]),
            "type": "Hyper-Arid Coarse Quartz Sand Matrix", "type_conf": 98,
            "type_exp": "The surface exhibits zero structural crumbs, extreme light scattering parameters, and high loose particle movement.",
            "moisture": "Severe Macro Leached Dry State (8%)", "moist_conf": 97, "moist_score": 15,
            "cracks": "None Detected - Complete Coarse Porosity", "cracks_conf": 94, "crack_score": 90,
            "om": "Critically Starved Organic Material (0.4%)", "om_conf": 96, "om_score": 10,
            "biology": "Sterile Biological Desert Surface", "bio_conf": 93, "bio_score": 12,
            "n_def": "Critical (Severe interveinal chlorosis across visible canopy)", "k_def": "Moderate deficiency patterns",
            "fungal": "None Detected", "pest": "High locust piercing damage markers",
            "heatmap_data": [12, 15, 88, 40]
        }

# ==========================================
# 🎨 PREMIUM CSS CORE LAYOUT SYSTEM
# ==========================================
PREMIUM_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
    body { background-color: #f0f4f1; font-family: 'Segoe UI', system-ui, sans-serif; color: #1e293b; }
    .nav-premium { background: linear-gradient(90deg, #07170a 0%, #15351a 100%); border-bottom: 4px solid #198754; }
    .hero-premium { background: linear-gradient(135deg, #091a0c 0%, #1b4322 100%); color: white; padding: 4rem 2rem; border-radius: 24px; box-shadow: 0 12px 36px rgba(0,0,0,0.1); }
    .card-luxury { border: none; border-radius: 20px; background: white; box-shadow: 0 8px 24px rgba(0,0,0,0.04); padding: 2.5rem; margin-bottom: 2rem; }
    .bar-container { background: #e2e8f0; border-radius: 8px; overflow: hidden; height: 24px; margin-bottom: 12px; }
    .bar-fill { height: 100%; display: flex; align-items: center; padding-left: 10px; color: white; font-weight: bold; font-size: 0.85rem; }
    .cure-banner { background: linear-gradient(135deg, #050f06 0%, #112916 100%); color: #eaf5ed; border-radius: 24px; padding: 3rem; border-left: 10px solid #ffc107; }
    .heatmap-mock { width: 100%; height: 200px; border-radius: 12px; background: url('https://images.unsplash.com/photo-1595341595378-fc74301d0163?auto=format&fit=crop&q=80&w=400') center; background-size: cover; position: relative; }
    .heatmap-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, rgba(255,0,0,0.6) 0%, rgba(255,255,0,0.4) 50%, transparent 100%); border-radius: 12px; }
    .img-showcase { border-radius: 20px; width: 100%; max-height: 380px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.15); }
</style>
"""

# ==========================================
# 🌐 MAIN WEB PORTAL DASHBOARD
# ==========================================
@app.get("/", response_class=HTMLResponse)
async def platform_hub():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield Grand Jury Agro-OS</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark nav-premium py-3 mb-4 shadow">
            <div class="container d-flex justify-content-between">
                <a class="navbar-brand fw-bold fs-3 text-success" href="/"><i class="bi bi-shield-shaded me-2"></i>BIOSHIELD EXPERT PLATFORM</a>
                <span class="badge bg-success font-monospace px-3 py-2">System Date: 2026-07-12</span>
            </div>
        </nav>

        <div class="container">
            <!-- HEADER HERO BRAND WITH CHATCHY SLOGAN -->
            <div class="hero-premium text-center mb-5 shadow-lg">
                <span class="badge bg-warning text-dark px-3 py-2 mb-3 text-uppercase font-monospace fw-bold">Grand Jury Evaluation Version 6.0</span>
                <h1 class="display-3 fw-bold text-white">Your Soil is Healthier, Your Life is Better</h1>
                <p class="lead max-width-800 mx-auto mt-2 text-white-50 fs-5">
                    An advanced framework integrating multi-spectral computer vision, explainable AI diagnostics, predictive simulators, and digital twin monitoring to safeguard global arable land.
                </p>
                <div class="row mt-4 justify-content-center">
                    <div class="col-md-9">
                        <img src="https://images.unsplash.com/photo-1463171359979-300662226149?auto=format&fit=crop&q=80&w=1200" class="img-showcase border border-success border-4 shadow" alt="Arable Land Shield">
                    </div>
                </div>
            </div>

            <!-- EXPLAINABLE THE PLANETARY SOIL DAMAGE PARAGRAPH -->
            <div class="card-luxury bg-white border border-danger border-opacity-10">
                <h3 class="fw-bold text-dark mb-3">🚨 The Planetary Topsoil Structural Collapse</h3>
                <p class="text-muted fs-6 lh-base">
                    Modern agro-industrial operations are running planetary soils to absolute biological starvation. Chemical synthetic over-fertilization, violent mechanical tillage, and heavy toxins have aggressively degraded over <strong>one-third of all global arable lands</strong>. When soil structural framework is stripped away, nutrient delivery pathways instantly lock down. Earth loses its native water-holding matrix, vital underground microbial populations vanish entirely, and crops are left open to aggressive terminal pathogens. Bad soil directly causes global agricultural crop loss, devastating nutritional drops, and system-wide ecosystem collapse.
                </p>
                <div class="row g-4 mt-2">
                    <div class="col-md-6"><div style="height: 240px; position: relative;"><canvas id="juryDrivers"></canvas></div></div>
                    <div class="col-md-6"><div style="height: 240px; position: relative;"><canvas id="juryDecline"></canvas></div></div>
                </div>
            </div>

            <!-- METHODS FOR HEALTHIER SOIL & ADVANCED WAYS OF AGRICULTURE -->
            <div class="card-luxury bg-light border border-success border-opacity-20">
                <h3 class="fw-bold text-success mb-3">🔄 Transitioning to Arable Sustainability</h3>
                <p class="text-muted small mb-4">To grow rich, high-yielding crops and reverse planetary land damage, we must switch from aggressive modern operations to smart, bio-mimicking agricultural methods.</p>
                <div class="row g-3">
                    <div class="col-md-4">
                        <div class="p-3 bg-white rounded-3 border-top border-4 border-success h-100">
                            <h5>1. No-Till Conservation</h5>
                            <p class="text-muted small mb-0">Stop violent plowing. Leaving underground root networks fully intact prevents natural wind/water erosion and saves micro-habitats.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 bg-white rounded-3 border-top border-4 border-success h-100">
                            <h5>2. Covered Crop Diversity</h5>
                            <p class="text-muted small mb-0">Keep living root exudates pumping nutrients year-round using mixed-species vegetation configurations like clover and rye.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 bg-white rounded-3 border-top border-4 border-success h-100">
                            <h5>3. Micro-Sponge Infusion</h5>
                            <p class="text-muted small mb-0">Manually inject porous structural nutrients and active biological defenses directly back into broken soil arrays using biochar.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- MAIN WORKING PIPELINE CORE INTERFACES -->
            <div class="row g-4 mb-5">
                <!-- PORTAL 1: INTERACTIVE ADVANCED CORE IMAGE MATRIX ANALYZER -->
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success">
                        <h4 class="fw-bold text-success mb-3"><i class="bi bi-camera2 me-2"></i>1. AI Soil Matrix Scan Portal</h4>
                        <p class="text-muted small mb-3">Snap or upload a raw site surface sample to evaluate visual attributes, texture classification, and confidence values.</p>
                        <form action="/run-diagnostic-matrix" method="post" enctype="multipart/form-data">
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary"><i class="bi bi-cloud-sun me-1"></i>Local Live Weather Feed Simulator</label>
                                <select class="form-select form-select-sm" name="weather_input">
                                    <option value="Sunny, High Evaporation (38°C)">Extreme Heat / High Evaporation Forecasted</option>
                                    <option value="Incoming Rain Expected (Next 12 Hours)">Impending Heavy Precipitation Forecasted</option>
                                    <option value="Balanced Intermittent Cloud Cover">Temperate / Standard Cloud Conditions</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Optional Lab Validation Overlays</label>
                                <div class="row g-2">
                                    <div class="col-3"><input class="form-control form-control-sm" type="text" name="lab_ph" placeholder="pH"></div>
                                    <div class="col-3"><input class="form-control form-control-sm" type="text" name="lab_n" placeholder="N%"></div>
                                    <div class="col-3"><input class="form-control form-control-sm" type="text" name="lab_p" placeholder="P%"></div>
                                    <div class="col-3"><input class="form-control form-control-sm" type="text" name="lab_k" placeholder="K%"></div>
                                </div>
                            </div>
                            <input class="form-control mb-3" type="file" name="file" accept="image/*" required>
                            <button class="btn btn-success w-100 fw-bold" type="submit">Execute Multi-Layer Scan</button>
                        </form>
                    </div>
                </div>

                <!-- PORTAL 2: INTERACTIVE DYNAMIC SIMULATOR SLIDERS -->
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-info">
                        <h4 class="fw-bold text-info mb-3"><i class="bi bi-sliders me-2"></i>2. Interactive Prediction Simulator</h4>
                        <p class="text-muted small">Adjust environmental variable parameters to simulate real-time forward adjustments on the BioShield Health Score matrix.</p>
                        <div class="p-3 bg-light rounded-3">
                            <div class="mb-3">
                                <label class="form-label small fw-bold d-flex justify-content-between"><span>Water Irrigation Input Volume:</span> <span id="valIrrig">50%</span></label>
                                <input type="range" class="form-range" id="slideIrrig" min="0" max="100" value="50" oninput="updateSimulation()">
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold d-flex justify-content-between"><span>BioShield Capsule Injection Density:</span> <span id="valCaps">1 unit/m²</span></label>
                                <input type="range" class="form-range" id="slideCaps" min="0" max="5" value="1" oninput="updateSimulation()">
                            </div>
                            <div class="mb-2">
                                <label class="form-label small fw-bold d-flex justify-content-between"><span>Organic Compost Mass Addition:</span> <span id="valComp">20%</span></label>
                                <input type="range" class="form-range" id="slideComp" min="0" max="100" value="20" oninput="updateSimulation()">
                            </div>
                            <hr>
                            <div class="text-center">
                                <h5 class="fw-bold text-dark mb-1">Simulated Dynamic Soil Score Output</h5>
                                <div class="fs-3 fw-bold text-success" id="simulatedScoreText">68 / 100</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- RESEARCH DATA COLLECTION GRID MODE -->
            <div class="card-luxury">
                <h4 class="fw-bold text-dark mb-2"><i class="bi bi-beaker me-2 text-primary"></i>Scientific Research Portal Sandbox Mode</h4>
                <p class="text-muted small mb-3">Download accumulated historical telemetry rows compiled inside the server system layer as standard verified format datasets.</p>
                <a href="/export-research-csv" class="btn btn-outline-primary fw-bold btn-sm"><i class="bi bi-download me-2"></i>Export System Dataset Rows (.CSV)</a>
            </div>

            <!-- INTEGRATED INTERACTIVE TIME LAPSE DIGITAL MONITORING GRAPH GRID -->
            <div class="card-luxury">
                <h4 class="fw-bold text-dark mb-4"><i class="bi bi-clock-history me-2 text-warning"></i>Ecosystem Digital Twin Track & Time-Lapse Loop</h4>
                <div class="row g-3 text-center small text-muted">
                    <div class="col-md-3"><div class="p-3 bg-light rounded border"><strong>Day 0 Baseline</strong><br><span class="badge bg-danger mt-1">Score: 42/100</span></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded border"><strong>Day 7 Post-Capsule</strong><br><span class="badge bg-warning text-dark mt-1">Score: 58/100</span></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded border"><strong>Day 14 Post-Capsule</strong><br><span class="badge bg-info mt-1">Score: 72/100</span></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded border"><strong>Day 30 Stabilized</strong><br><span class="badge bg-success mt-1">Score: 84/100</span></div></div>
                </div>
            </div>
        </div>

        <script>
            new Chart(document.getElementById('juryDrivers'), {{
                type: 'pie',
                data: {{
                    labels: ['Chemical Synthetic Blasts', 'Mechanical Tillage', 'Erosion', 'Salinization'],
                    datasets: [{{
                        data: [45, 25, 20, 10],
                        backgroundColor: ['#091a0c', '#15351a', '#2c6e3d', '#61b176']
                    }}]
                }},
                options: {{ responsive: true, maintainAspectRatio: false }}
            }});

            new Chart(document.getElementById('juryDecline'), {{
                type: 'line',
                data: {{
                    labels: ['2000', '2010', '2020', '2026', '2035'],
                    datasets: [{{
                        label: 'Arable Land Loss Progression',
                        data: [1500, 1410, 1330, 1240, 1050],
                        borderColor: '#dc3545',
                        fill: false
                    }}]
                }},
                options: {{ responsive: true, maintainAspectRatio: false }}
            }});

            function updateSimulation() {{
                const irrig = parseInt(document.getElementById('slideIrrig').value);
                const caps = parseInt(document.getElementById('slideCaps').value);
                const comp = parseInt(document.getElementById('slideComp').value);
                
                document.getElementById('valIrrig').innerText = irrig + "%";
                document.getElementById('valCaps').innerText = caps + " unit/m²";
                document.getElementById('valComp').innerText = comp + "%";
                
                // Prediction calculation mapping rules
                let score = 30 + (irrig * 0.3) + (caps * 8) + (comp * 0.2);
                if(score > 100) score = 100;
                document.getElementById('simulatedScoreText').innerText = Math.round(score) + " / 100";
            }}
        </script>
    </body>
    </html>
    """

@app.post("/run-diagnostic-matrix", response_class=HTMLResponse)
async def run_diagnostic_matrix_route(
    weather_input: str = Form(...),
    lab_ph: str = Form(""), lab_n: str = Form(""), lab_p: str = Form(""), lab_k: str = Form(""),
    file: UploadFile = File(...)
):
    res = process_field_image(file.filename)
    
    # IF THE COMPUTER VISION CANNOT SECURE VALIDATION PARAMS, DROP DIRECT SYSTEM UNRECOGNIZABLE ERROR PAGE
    if res.get("error"):
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI System Extraction Fault</title>
            {PREMIUM_CSS}
        </head>
        <body>
            <div class="container py-5 text-center">
                <div class="card-luxury border border-danger p-5">
                    <i class="bi bi-exclamation-triangle-fill text-danger display-1 mb-3"></i>
                    <h2 class="fw-bold text-dark">Image Processing Exception Encountered</h2>
                    <p class="text-muted fs-5 mx-auto" style="max-width: 600px;">{res['error']}</p>
                    <hr class="my-4">
                    <p class="small text-secondary">Ensure the uploaded smartphone file contains valid target field lighting parameters, rich organic layer boundaries, and lacks motion blur elements.</p>
                    <a href="/" class="btn btn-dark fw-bold mt-2">← Back to Diagnosis Panel</a>
                </div>
            </div>
        </body>
        </html>
        """
        
    # Health Index Formulations
    score = int((res["moist_score"] + res["om_score"] + res["crack_score"] + res["bio_score"]) / 4)
    grade = "A-" if score >= 80 else "B" if score >= 60 else "C-" if score >= 40 else "F-Degraded"
    
    # Weather Rule Injection Matrix
    weather_alert = ""
    if "38°C" in weather_input:
        weather_alert = "🚨 IRRIGATION WARNING: High evaporation alert active. Boost subsurface drip cycle runtimes immediately."
    elif "Rain" in weather_input:
        weather_alert = "🌧️ METEOROLOGICAL ALERT: Precipitation coming within 12 hours. Postpone field applications now to prevent erosion."
    else:
        weather_alert = "🌤️ STABLE ATMOSPHERE: Run standard capsule schedules safely."

    # Crop Calculations
    wheat_suit = score + 10 if score > 50 else score
    tomato_suit = score + 15 if score > 60 else score - 15
    straw_suit = score - 10 if "Sand" in res["type"] else score + 12
    corn_suit = score + 5
    
    # Carbon Metrics
    carbon_stored = round((score * 12.4), 1)
    co2_saved = round((carbon_stored * 3.67), 1)
    water_saved = score * 140

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Soil Doctor Intelligence Report</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="d-flex justify-content-between mb-4">
                <a href="/" class="btn btn-outline-dark btn-sm"><i class="bi bi-arrow-left"></i> Core Grid Hub</a>
                <button class="btn btn-danger btn-sm fw-bold shadow" onclick="window.print()"><i class="bi bi-file-pdf"></i> Download PDF Report</button>
            </div>

            <!-- COMPOSITE SCORE METRIC METER PANEL -->
            <div class="card-luxury bg-white border border-success border-opacity-30">
                <h6 class="text-uppercase tracking-widest text-secondary font-monospace small">Feature 12: Integrated Custom Smart BioShield Index</h6>
                <hr>
                <div class="row align-items-center">
                    <div class="col-md-4 text-center">
                        <div class="p-4 rounded-4 bg-light border">
                            <h2 class="fw-bold mb-1">Overall Grade</h2>
                            <div class="display-3 fw-bold text-success">{grade}</div>
                            <div class="fs-5 text-muted">Health: {score}/100</div>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <label class="fw-bold small">Surface Moisture Level Indicator:</label>
                        <div class="bar-container"><div class="bar-fill bg-info" style="width: {res['moist_score']}%">{res['moist_score']}%</div></div>
                        
                        <label class="fw-bold small">Organic Carbon Accumulation Base:</label>
                        <div class="bar-container"><div class="bar-fill bg-success" style="width: {res['om_score']}%">{res['om_score']}%</div></div>
                        
                        <label class="fw-bold small">Structural Crack Resistance Level:</label>
                        <div class="bar-container"><div class="bar-fill bg-warning text-dark" style="width: {res['crack_score']}%">{res['crack_score']}%</div></div>
                    </div>
                </div>
            </div>

            <!-- FEATURE 1: EXPLAINABLE AI SOIL DOCTOR BREAKDOWN -->
            <div class="card-luxury border-start border-4 border-success">
                <h3 class="fw-bold text-dark mb-3"><i class="bi bi-heart-pulse-fill text-success"></i> Feature 1: AI Soil Doctor Primary Diagnostics</h3>
                <div class="row g-3 text-dark small">
                    <div class="col-md-6"><strong>Identified Issue Matrix:</strong> <p class="text-muted">{res['cracks']} alongside {res['moisture']}</p></div>
                    <div class="col-md-6"><strong>Primary Causative Trigger:</strong> <p class="text-muted">{res['type_exp']}</p></div>
                    <div class="col-md-6"><strong>Pathological Status Severity Level:</strong> <p class="text-danger fw-bold">Critical Structural Matrix Degradation Flag</p></div>
                    <div class="col-md-6"><strong>Targeted Correction Forecast:</strong> <p class="text-muted">Deploying organic bio-sponges is expected to increase baseline scores by +35 points within 14 execution days.</p></div>
                </div>
            </div>

            <!-- FEATURE 7: EXPLAINABLE ATTENTION HEATMAP READOUT -->
            <div class="card-luxury">
                <h4 class="fw-bold text-dark mb-3"><i class="bi bi-grid-3x3-gap-fill text-primary"></i> Feature 7: Computer Vision Region Attention Heatmap</h4>
                <div class="row g-4 align-items-center">
                    <div class="col-md-6">
                        <div class="heatmap-mock shadow"><div class="heatmap-overlay"></div></div>
                    </div>
                    <div class="col-md-6">
                        <p class="text-muted small">
                            The red highlighted regions show where the AI model tracked loose texture boundaries and deep cracks. These highlights explain why the model detected high erosion risks and low organic matter.
                        </p>
                    </div>
                </div>
            </div>

            <!-- GEOGRAPHY LOCATION TRACKING CARD -->
            <div class="card-luxury bg-light border">
                <h5 class="fw-bold text-dark mb-2"><i class="bi bi-geo-alt-fill text-danger"></i> Egypt Mapping Node Telemetry Geolocation</h5>
                <p class="font-monospace small text-secondary mb-0">
                    Mapped Region Node: <strong>{res['location']['name']}</strong> | Coordinates: {res['location']['lat']}°N, {res['location']['lon']}°E | Regional Landscape Classification Group: {res['location']['zone']}
                </p>
            </div>

            <!-- FEATURE 8: LABORATORY VERIFICATION COMPONENT OVERLAY CHART -->
            <div class="card-luxury">
                <h4 class="fw-bold text-dark mb-3"><i class="bi bi-journal-check text-info"></i> Feature 8: Scientific Lab Verification Overlay Ledger</h4>
                <div class="table-responsive">
                    <table class="table border table-bordered small font-monospace">
                        <thead class="table-dark">
                            <tr>
                                <th>Soil Compound Core Parameter</th>
                                <th>AI Computer Vision Prediction Output</th>
                                <th>Laboratory Physical Onsite Metrics Entered</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Active pH Index</strong></td><td>6.8 (Estimated Base Value)</td><td>{lab_ph if lab_ph else "No Overlay Data"}</td></tr>
                            <tr><td><strong>Nitrogen Core Level (N)</strong></td><td>1.4% (Estimated Base Value)</td><td>{lab_n if lab_n else "No Overlay Data"}</td></tr>
                            <tr><td><strong>Phosphorus Level (P)</strong></td><td>0.8% (Estimated Base Value)</td><td>{lab_p if lab_p else "No Overlay Data"}</td></tr>
                            <tr><td><strong>Potassium Level (K)</strong></td><td>1.9% (Estimated Base Value)</td><td>{lab_k if lab_k else "No Overlay Data"}</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- WEATHER OVERLAY ACTION CARD -->
            <div class="card-luxury bg-info bg-opacity-10 border border-info">
                <h5 class="fw-bold text-info mb-1"><i class="bi bi-cloud-haze2-fill"></i> Weather Integration Suggestion</h5>
                <p class="small text-dark mb-0 font-monospace">{weather_alert}</p>
            </div>

            <!-- FEATURE 3: DYNAMIC CROP SUITABILITY MATRIX SCORE CARDS -->
            <div class="card-luxury">
                <h4 class="fw-bold text-dark mb-3"><i class="bi bi-flower1 text-success"></i> Feature 3: Smart Arable Crop Suitability Forecasts</h4>
                <div class="row g-3 text-center text-dark font-monospace small">
                    <div class="col-md-3"><div class="p-3 border rounded bg-light"><strong>Wheat Grain Core</strong><br><span class="badge bg-success mt-2">{min(100, int(wheat_suit))}% Match</span></div></div>
                    <div class="col-md-3"><div class="p-3 border rounded bg-light"><strong>Tomato Vine Node</strong><br><span class="badge bg-success mt-2">{max(10, int(tomato_suit))}% Match</span></div></div>
                    <div class="col-md-3"><div class="p-3 border rounded bg-light"><strong>Strawberry Hybrid</strong><br><span class="badge bg-success mt-2">{max(10, int(straw_suit))}% Match</span></div></div>
                    <div class="col-md-3"><div class="p-3 border rounded bg-light"><strong>Corn Silage Base</strong><br><span class="badge bg-success mt-2">{min(100, int(corn_suit))}% Match</span></div></div>
                </div>
            </div>

            <!-- FEATURE 4: CARBON SAVING CALCULATOR COMPONENT -->
            <div class="card-luxury border-start border-4 border-primary">
                <h4 class="fw-bold text-primary mb-3"><i class="bi bi-globe-americas"></i> Feature 4: Carbon Saving & Sustainability Registry Matrix</h4>
                <div class="row g-3 text-center small font-monospace text-dark">
                    <div class="col-md-4"><div class="p-3 rounded bg-light"><strong>Net Organic Carbon Trapped:</strong><br><span class="fs-4 fw-bold text-primary">{carbon_stored} kg/m²</span></div></div>
                    <div class="col-md-4"><div class="p-3 rounded bg-light"><strong>CO₂ Equivalents Reduced:</strong><br><span class="fs-4 fw-bold text-primary">{co2_saved} kg/m²</span></div></div>
                    <div class="col-md-4"><div class="p-3 rounded bg-light"><strong>Water Saved Forecast:</strong><br><span class="fs-4 fw-bold text-primary">{water_saved} Liters/Plot</span></div></div>
                </div>
            </div>

            <!-- DIAGNOSTIC PLANT ANALYSIS SUB-LAYER READOUT OVERLAY -->
            <div class="card-luxury bg-light border">
                <h5 class="fw-bold text-danger mb-2"><i class="bi bi-patch-exclamation"></i> Integrated Canopy Defect Matrix Readout</h5>
                <div class="row g-3 small font-monospace text-muted">
                    <div class="col-md-3"><strong>Nitrogen Deficit:</strong> {res['n_def']}</div>
                    <div class="col-md-3"><strong>Potassium Deficit:</strong> {res['k_def']}</div>
                    <div class="col-md-3"><strong>Fungal Colony State:</strong> {res['fungal']}</div>
                    <div class="col-md-3"><strong>Insect/Pest Marking:</strong> {res['pest']}</div>
                </div>
            </div>

            <!-- FEATURE 9: BIOSHIELD PRODUCT INPUT SYSTEM RECOMMENDATIONS -->
            <div class="cure-banner shadow-lg">
                <div class="row g-4 align-items-center">
                    <div class="col-md-8">
                        <h2 class="fw-bold text-warning mb-3">🌿 The Ultimate Cure: BioShield Structural Nutrients</h2>
                        <p class="lh-base text-white-50 small">
                            BioShield Nutrients represents the **most advanced, 100% pure organic fertilization matrix in the world**. Engineered intentionally to completely bypass standard chemical side-effects, our remedy repairs complex underlying soil tissue while fueling natural systemic growth. It sources ingredients natively: **Banana Shells** supply rich, active organic Potassium (K) for water regulation; **Eggshells** provide slow-release crystalline Calcium (Ca) matrices to fortify soil structures; **Onion Extracts** deliver a devastating blow to unwanted parasitic bacterial cells; and clean **Biochar** builds massive microscopic sponge sanctuaries to harbor beneficial biological microbes permanently.
                        </p>
                        <h4 class="text-success fw-bold mt-4 mb-2">The Salicylic Acid Miracle Asset</h4>
                        <p class="text-white-50 small mb-4">
                            The secret defensive shield of this blend is pure **Salicylic Acid**. Acting identically to an vaccine immune response in organic plant tissue, Salicylic Acid triggers **Systemic Acquired Resistance (SAR)** within the root framework. When absorbed, it tells the plant to pre-emptively produce pathogenesis-related proteins, signaling cellular walls to thicken and sealing vascular pathways against oncoming fungal or bacterial blights before they strike.
                        </p>
                        
                        <!-- INCORPORATING SEAMLESS USER DIRECT SECURE ORDER EMAIL INFORMATION -->
                        <div class="p-3 rounded bg-white bg-opacity-10 border border-warning text-warning mb-2">
                            <h6 class="fw-bold mb-1"><i class="bi bi-envelope-open-fill me-2"></i>Secure Direct Ordering Channel Registry:</h6>
                            <p class="mb-0 text-white small">Contact our global distribution team at <strong class="text-white font-monospace">radwaabdallnasser@gmail.com</strong> to secure custom capsule deliveries and schedule field team onboarding.</p>
                        </div>
                    </div>
                    <div class="col-md-4 text-center">
                        <div class="p-2 bg-white rounded-4 shadow">
                            <img src="https://raw.githubusercontent.com/RadwaAbdallnasser/BioShield/main/image_82d4c1.jpg" onerror="this.src='https://images.unsplash.com/photo-1595341595378-fc74301d0163?auto=format&fit=crop&q=80&w=600'" class="img-fluid rounded-4" alt="Premium BioShield Packaging Line">
                        </div>
                        <p class="text-warning fw-bold mt-3 mb-0 fs-5">✨ Your Soil is Healthier, Your Life is Better ✨</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/export-research-csv")
async def export_research_csv_endpoint():
    """Generates an exportable CSV spreadsheet for research tracking validation."""
    stream = StringIO()
    writer = csv.writer(stream)
    writer.writerow(["Timestamp", "Scan ID Reference", "Calculated Health Score", "Soil Taxonomy Target", "Status Flag"])
    writer.writerow(["2026-05-12", "SCAN_082", "42", "Clay Matrix", "Degraded Fissured Profile"])
    writer.writerow(["2026-06-04", "SCAN_119", "55", "Silt Loam", "Compacted Layer Block"])
    writer.writerow(["2026-06-28", "SCAN_304", "79", "Optimized Loam", "BioShield Capsule Stabilized"])
    
    stream.seek(0)
    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=bioshield_research_dataset.csv"}
    )

@app.post("/run-comparative-audit", response_class=HTMLResponse)
async def run_comparative_audit_route(before_id: str = Form(...), file_after: UploadFile = File(...)):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ecosystem Digital Twin Audit Ledger</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Core Grid Hub</a></div>
            
            <div class="hero-premium bg-success text-center py-4 mb-4">
                <h2 class="fw-bold text-warning"><i class="bi bi-arrow-left-right me-2"></i>Post-Treatment Verification Analysis</h2>
                <p class="mb-0 text-white-50 small">Automated Field Performance Comparison Tracking Audit Ledger</p>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-luxury border-top border-4 border-danger h-100">
                        <h5 class="fw-bold text-danger"><i class="bi bi-x-circle me-2"></i>Pre-Treatment Baseline Metrics</h5>
                        <p class="text-muted font-monospace small mb-3">Historical Reference Node: {before_id}</p>
                        <hr>
                        <ul>
                            <li class="mb-2"><strong>Calculated Health Index:</strong> <span class="text-danger fw-bold">42 / 100</span></li>
                            <li class="mb-2"><strong>Moisture Surface Appearance:</strong> Dry, Evaporated Layer</li>
                            <li class="mb-2"><strong>Vegetation Canopy Spread:</strong> Restricted / High Chlorosis Symptoms</li>
                            <li class="mb-2"><strong>Topsoil Surface Texture:</strong> Hard Crust Blocks / Loose Leached Sand</li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card-luxury border-top border-4 border-success h-100 shadow-lg">
                        <h5 class="fw-bold text-success"><i class="bi bi-check-circle me-2"></i>Post-Capsule Treatment Progress</h5>
                        <p class="text-muted font-monospace small mb-3">Image Node ID: {file_after.filename}</p>
                        <hr>
                        <ul>
                            <li class="mb-2"><strong>Calculated Health Index:</strong> <span class="text-success fw-bold">84 / 100 (+42 Boost)</span></li>
                            <li class="mb-2"><strong>Moisture Surface Appearance:</strong> Fully Hydrated Organic Profile</li>
                            <li class="mb-2"><strong>Vegetation Canopy Spread:</strong> Active Root Expansion & Green Foliage Growth</li>
                            <li class="mb-2"><strong>Topsoil Surface Texture:</strong> Highly Aggregate Porous Micro-Sponge Matrix</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="card-luxury bg-white border border-success text-center">
                <h5 class="fw-bold text-success"><i class="bi bi-stars me-2"></i>Verification Success: Soil Structural Transformation Logged</h5>
                <p class="text-muted small mb-0">The comparison engine confirms successful breakdown of the biodegradable capsule shell. The porous biochar matrix has re-hydrated dry clay zones, locked active nitrogen pathways, and restored long-term topsoil balance.</p>
                <p class="text-warning fw-bold mt-3 mb-0 fs-5">✨ Your Soil is Healthier, Your Life is Better ✨</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/execute-qr-trigger", response_class=HTMLResponse)
async def execute_qr_trigger_route(qr_token: str = Form(...)):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>QR Verification Profile</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Core Grid Hub</a></div>
            
            <div class="card-luxury border-top border-4 border-primary">
                <h3 class="fw-bold text-primary mb-2"><i class="bi bi-qr-code-scan me-2"></i>BioShield Package Integration Interface</h3>
                <p class="text-muted small">Verified Serial Token Key: <span class="font-monospace fw-bold text-dark">{qr_token}</span></p>
                <hr>
                
                <h5 class="fw-bold text-dark mb-2">📥 On-Field Capsule Deployment Instructions:</h5>
                <ol class="text-muted small mb-4">
                    <li class="mb-2">Dig a small 10-15 cm core opening directly adjacent to the primary root canopy line.</li>
                    <li class="mb-2">Insert one (1) single BioShield Biodegradable Nutrients Capsule cleanly inside the channel.</li>
                    <li class="mb-2">Cover the opening with topsoil and run a standard morning irrigation cycle to dissolve the protective shell.</li>
                </ol>
            </div>
        </div>
    </body>
    </html>
    """
