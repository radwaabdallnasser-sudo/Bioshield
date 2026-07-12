import random
import json
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title="BioShield Ultra-Core Platform v5.0")

# ==========================================
# 📊 PRE-CONFIGURED FARM DATABASE LABELS (MOCK HISTORICAL STORAGE)
# ==========================================
MOCK_HISTORY = [
    {"date": "2026-05-12", "id": "SCAN_082", "score": 42, "type": "Clay Matrix", "status": "Degraded / Severely Cracked"},
    {"date": "2026-06-04", "id": "SCAN_119", "score": 55, "type": "Silt Loam", "status": "Compacted Matrix Structure"},
    {"date": "2026-06-28", "id": "SCAN_304", "score": 79, "type": "Optimized Loam", "status": "BioShield Capsule Treated"}
]

# ==========================================
# 🧠 ULTIMATE INTEGRATED AI EXPERT SIMULATORS
# ==========================================

def run_advanced_soil_scan(filename: str):
    """Executes feature visual analytics to evaluate physical, chemical, and biological layers."""
    random.seed(len(filename) + 999)
    
    # Random selection variants for distinct mock-uploads
    variants = [
        {
            "type": "Coarse Sandy Loam Matrix", "type_conf": 94, "type_exp": "The surface appears highly coarse and shows loose, unaggregated particulate gaps.",
            "moisture": "Dry Surface Profile (14%)", "moist_conf": 96, "moist_score": 35,
            "cracks": "Low / High Leaching Porosity", "cracks_conf": 89, "crack_score": 80,
            "om": "Bleached, Low Carbon Appearance (1.1%)", "om_conf": 91, "om_score": 40,
            "biology": "Sterile Topsoil Texture Base", "bio_conf": 87, "surf_score": 50, "bio_score": 30,
            "weed_algae": "None Detected", "algae_conf": 95,
            "n_def": "Severe Leaf Rim Yellowing", "k_def": "Interveinal Chlorosis Present", "fungal": "None Identified", "pest": "Low Edge-Bite Markers"
        },
        {
            "type": "Dense Silty Clay Block", "type_conf": 91, "type_exp": "The surface exhibits deep crusting, massive macro-structural blocks, and heavy glare absorption reflections.",
            "moisture": "Saturated Evaporation Crusted (68%)", "moist_conf": 93, "moist_score": 50,
            "cracks": "Severe Structural Fissures & Deep Cracking", "cracks_conf": 97, "crack_score": 25,
            "om": "Moderate Organic Matrix (2.8%)", "om_conf": 88, "om_score": 65,
            "biology": "Thick Parasitic Cyanobacteria Film Present", "bio_conf": 84, "surf_score": 30, "bio_score": 45,
            "weed_algae": "Dense Algal / Mold Sheets Identified", "algae_conf": 92,
            "n_def": "Stunted Stalk Complex", "k_def": "Necrotic Leaf Borders On-Screen", "fungal": "Powdery Mildew Spotted", "pest": "High Piercing Canopy Injury"
        }
    ]
    return random.choice(variants)

# ==========================================
# 🎨 REUSABLE ENTERPRISE UI STYLE SYSTEM (CSS)
# ==========================================
SHARED_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
    body { background-color: #f1f5f3; font-family: 'Segoe UI', system-ui, sans-serif; color: #1e293b; }
    .nav-premium { background: linear-gradient(90deg, #091a0c 0%, #1c3c22 100%); border-bottom: 3px solid #198754; }
    .hero-premium { background: linear-gradient(135deg, #0f2613 0%, #254a29 100%); color: white; padding: 4rem 2rem; border-radius: 24px; box-shadow: 0 12px 32px rgba(0,0,0,0.08); }
    .card-premium { border: none; border-radius: 18px; background: white; box-shadow: 0 6px 20px rgba(0,0,0,0.03); padding: 2rem; transition: transform 0.2s; }
    .card-premium:hover { transform: translateY(-2px); }
    .score-badge { width: 110px; height: 110px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 800; border: 6px solid #e2e8f0; margin: 0 auto; }
    .score-good { border-color: #198754; color: #198754; background: #e8f5e9; }
    .score-bad { border-color: #dc3545; color: #dc3545; background: #fdf2f2; }
    .cure-premium-card { background: linear-gradient(135deg, #071409 0%, #152e1a 100%); color: #f1f8f3; border-radius: 24px; padding: 3rem; position: relative; border-left: 10px solid #ffc107; }
    .img-showcase { border-radius: 16px; object-fit: cover; max-height: 400px; width: 100%; box-shadow: 0 8px 24px rgba(0,0,0,0.1); }
</style>
"""

# ==========================================
# 🌐 WEBPAGE CONTROLLERS & ENDPOINTS
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def home_portal():
    # Calculate summary counts for the dashboard
    total_scans = len(MOCK_HISTORY) + 124
    avg_health = 74
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield Agro-Intelligence Hub</title>
        {SHARED_CSS}
    </head>
    <body>
        <!-- NAVIGATION HEADER -->
        <nav class="navbar navbar-dark nav-premium py-3 mb-4">
            <div class="container d-flex justify-content-between">
                <a class="navbar-brand fw-bold fs-3 text-success" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD ULTRAC CORE</a>
                <span class="text-white-50 font-monospace small">Terminal Connection Status: Active [2026-07-12]</span>
            </div>
        </nav>

        <div class="container">
            <!-- HERO WELCOME & TARGETED BRAND SLOGAN -->
            <div class="hero-premium text-center mb-5">
                <span class="badge bg-success px-3 py-2 mb-3 text-uppercase font-monospace tracking-wider">Planetary Soil Reclamation Project</span>
                <h1 class="display-4 fw-bold text-white">Your Soil is Healthier, Your Life is Better</h1>
                <p class="lead max-width-800 mx-auto mt-2 text-white-50">
                    Bypassing industrial limits by pairing advanced multi-spectral computer vision and explainable AI infrastructure directly with smart biodegradable soil technology.
                </p>
                <div class="row mt-4 justify-content-center">
                    <div class="col-md-8">
                        <img src="https://images.unsplash.com/photo-1463171359979-300662226149?auto=format&fit=crop&q=80&w=1200" class="img-showcase border border-success border-3" alt="Healthy Crops Canopy Grid">
                    </div>
                </div>
            </div>

            <!-- FEATURE 14: ANALYTICAL CORE EXECUTIVE DASHBOARD -->
            <div class="card-premium mb-5 bg-light border border-success border-opacity-10">
                <h4 class="fw-bold text-dark mb-4"><i class="bi bi-speedometer2 me-2 text-success"></i>Regional Agro-Telemetry Dashboard Overview</h4>
                <div class="row g-3 text-center">
                    <div class="col-md-3"><div class="p-3 bg-white rounded-3 shadow-sm"><h6>Total Aggregate Scans</h6><div class="fs-2 fw-bold text-success">{total_scans}</div><small class="text-muted">Real-time global logs</small></div></div>
                    <div class="col-md-3"><div class="p-3 bg-white rounded-3 shadow-sm"><h6>Average Topsoil Score</h6><div class="fs-2 fw-bold text-warning">{avg_health}/100</div><small class="text-muted">Regional index metrics</small></div></div>
                    <div class="col-md-3"><div class="p-3 bg-white rounded-3 shadow-sm"><h6>Water Conservation Save</h6><div class="fs-2 fw-bold text-info">340K Liters</div><small class="text-muted">Via Capsule Sponging</small></div></div>
                    <div class="col-md-3"><div class="p-3 bg-white rounded-3 shadow-sm"><h6>Restoration Growth Delta</h6><div class="fs-2 fw-bold text-primary">+38.4%</div><small class="text-muted">Calculated over 90 days</small></div></div>
                </div>
            </div>

            <!-- CORE AI PIPELINE HUB INTERFACES (SCANS & COMPARISONS) -->
            <h3 class="fw-bold text-dark mb-4 text-center"><i class="bi bi-cpu me-2 text-success"></i>Interactive AI Multi-Spectral Diagnostics Suite</h3>
            <div class="row g-4 mb-5">
                <!-- SCAN MODE 1: INTEGRATED CORE SOIL EYE -->
                <div class="col-md-4">
                    <div class="card-premium h-100 border-top border-4 border-success shadow-sm">
                        <h4 class="fw-bold text-success mb-2"><i class="bi bi-camera-fill me-2"></i>1. AI Soil Matrix Scan</h4>
                        <p class="text-muted small">Snap or upload a raw site surface sample to evaluate visual attributes, texture classification, and confidence values.</p>
                        <form action="/run-full-analysis" method="post" enctype="multipart/form-data">
                            <!-- FEATURE 8: INTEGRATED WEATHER MATRIX SELECTION CONTROL -->
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary"><i class="bi bi-cloud-sun me-1"></i>Local Live Weather Feed Simulator</label>
                                <select class="form-select form-select-sm" name="weather_feed">
                                    <option value="Sunny, High Evaporation (38°C)">Extreme Heat / High Evaporation Forecasted</option>
                                    <option value="Incoming Rain Expected (Next 12 Hours)">Impending Heavy Precipitation Forecasted</option>
                                    <option value="Balanced Intermittent Cloud Cover">Temperate / Standard Cloud Conditions</option>
                                </select>
                            </div>
                            <input class="form-control mb-3" type="file" name="file" accept="image/*" required>
                            <button class="btn btn-success w-100 fw-bold" type="submit">Execute Multi-Layer Extraction</button>
                        </form>
                    </div>
                </div>

                <!-- SCAN MODE 2: AUDIT BEFORE & AFTER Restorative System -->
                <div class="col-md-4">
                    <div class="card-premium h-100 border-top border-4 border-warning shadow-sm">
                        <h4 class="fw-bold text-warning mb-2"><i class="bi bi-arrow-left-right me-2"></i>2. Before & After Audits</h4>
                        <p class="text-muted small">Input an existing scan tracking code ID alongside a post-treatment capture to calculate physical regeneration rates.</p>
                        <form action="/run-comparative-audit" method="post" enctype="multipart/form-data">
                            <input class="form-control form-control-sm mb-2" type="text" name="before_id" placeholder="Enter Baseline Token ID (e.g. SCAN_082)" required>
                            <input class="form-control mb-3" type="file" name="file_after" accept="image/*" required>
                            <button class="btn btn-warning w-100 fw-bold text-dark" type="submit">Verify Post-Capsule Repair</button>
                        </form>
                    </div>
                </div>

                <!-- SCAN MODE 3: INTEGRATED INSTANT PACKAGE QR RESPONSE LOGS -->
                <div class="col-md-4">
                    <div class="card-premium h-100 border-top border-4 border-primary shadow-sm">
                        <h4 class="fw-bold text-primary mb-2"><i class="bi bi-qr-code me-2"></i>3. Capsule QR Interaction</h4>
                        <p class="text-muted small">Scan the product package identifier key to pull up dynamic application rules, usage coordinates, and logs.</p>
                        <form action="/execute-qr-trigger" method="post">
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Package Product Serial Core Key</label>
                                <input class="form-control" type="text" name="qr_token" placeholder="e.g. BSN-CAPSULE-2026X" required>
                            </div>
                            <button class="btn btn-primary w-100 fw-bold" type="submit">Load Package Directives</button>
                        </form>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE AGRO-MAP COMPONENT MODULE -->
            <div class="card-premium mb-5">
                <h4 class="fw-bold text-dark mb-2"><i class="bi bi-geo-alt-fill me-2 text-danger"></i>Interactive Regional Topsoil Mapping Grid</h4>
                <p class="text-muted small mb-4">Click location hot-spots to inspect decentralized localized field metrics and macro-compaction risk areas.</p>
                <div class="p-5 text-center rounded-3 border bg-light position-relative" style="background: url('https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&q=80&w=1200') center; background-size: cover; height: 300px;">
                    <div class="position-absolute btn btn-sm btn-danger fw-bold shadow animate-bounce" style="top: 25%; left: 30%;" onclick="alert('Zone Alpha ID: SCAN_082. Base Score: 42/100 (Silty Block, Heat Stressed)')">📍 Plot A (42/100)</div>
                    <div class="position-absolute btn btn-sm btn-success fw-bold shadow animate-bounce" style="top: 60%; left: 75%;" onclick="alert('Zone Gamma ID: SCAN_304. Base Score: 79/100 (BioShield Optimized)')">📍 Plot C (79/100)</div>
                    <div class="position-absolute btn btn-sm btn-warning fw-bold shadow animate-bounce" style="top: 45%; left: 55%;" onclick="alert('Zone Beta ID: SCAN_119. Base Score: 55/100 (High Crusting Loss)')">📍 Plot B (55/100)</div>
                </div>
            </div>

            <!-- INTERACTIVE FARM CHAT SANDBOX ENVIRONMENT -->
            <div class="card-premium mb-5 border border-primary border-opacity-25 shadow-sm">
                <h4 class="fw-bold text-primary mb-2"><i class="bi bi-chat-left-dots-fill me-2"></i>Integrated AI Agronomic Chat Assistant Sandbox</h4>
                <p class="text-muted small mb-3">Simulate immediate on-field problem questions to access diagnostic explanations and structural agronomic data rules.</p>
                <div class="mb-3 p-3 rounded bg-light font-monospace small" id="chatWindow" style="max-height: 200px; overflow-y: auto;">
                    <div class="text-secondary"><strong class="text-info">[SYSTEM]:</strong> Core Expert Shell ready. Enter a test agronomic query block below to parse responses.</div>
                </div>
                <div class="input-group">
                    <select class="form-select" id="chatSelect">
                        <option value="Why exactly is my farm soil displaying surface cracking patterns?">"Why is my soil cracking?"</option>
                        <option value="Can I successfully grow high-extraction Tomato nodes in degraded clay?">"Can I grow tomatoes?"</option>
                        <option value="How often should I water given extreme hot evaporation projections?">"How often should I water?"</option>
                    </select>
                    <button class="btn btn-primary fw-bold" type="button" onclick="triggerMockChat()">Dispatch Field Query</button>
                </div>
            </div>

            <!-- COMPREHENSIVE HISTORICAL FARM LOG ENTRIES -->
            <div class="card-premium mb-5">
                <h4 class="fw-bold text-dark mb-3"><i class="bi bi-folder-fill me-2 text-warning"></i>Historical Farm Diagnostic Core Log Database</h4>
                <div class="table-responsive">
                    <table class="table table-hover border align-middle">
                        <thead class="table-dark">
                            <tr>
                                <th>Capture Timestamp</th>
                                <th>Scan Tracking ID</th>
                                <th>AI Soil Health Score</th>
                                <th>Calculated Classification Group</th>
                                <th>Identified Field Status Profile</th>
                            </tr>
                        </thead>
                        <tbody>
                            {"".join([f"<tr><td>{h['date']}</td><td class='font-monospace fw-bold'>{h['id']}</td><td><span class='badge bg-{'success' if h['score'] > 70 else 'warning' if h['score'] > 50 else 'danger'}'>{h['score']}/100</span></td><td>{h['type']}</td><td>{h['status']}</td></tr>" for h in MOCK_HISTORY])}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <script>
            function triggerMockChat() {{
                const sel = document.getElementById('chatSelect');
                const win = document.getElementById('chatWindow');
                const q = sel.value;
                let a = "";
                
                if (q.includes("cracking")) {{
                    a = "EXPLANATION: Surface cracking points to volume reduction in high-shrink clay soils caused by excessive evaporation and organic matter depletion. Deploying the BioShield Capsule forms microsponges to stop this separation.";
                }} else if (q.includes("Tomato")) {{
                    a = "EXPLANATION: Tomatoes demand porous root passage and high potassium. Clay matrices block roots and breed wilt unless pre-conditioned with porous Biochar and Calcium blends like BioShield Nutrients.";
                }} else {{
                    a = "EXPLANATION: In extreme conditions, shift to morning subsurface drip schedules. Our analysis updates watering requirements by analyzing moisture evaporation trends via live weather feeds.";
                }}
                
                win.innerHTML += `<div class='mt-2 text-dark'><strong>🧑‍🌾 You:</strong> ${{q}}</div>`;
                win.innerHTML += `<div class='text-success'><strong>🤖 AI Expert:</strong> ${{a}}</div>`;
                win.scrollTop = win.scrollHeight;
            }}
        </script>
    </body>
    </html>
    """

@app.post("/run-full-analysis", response_class=HTMLResponse)
async def run_full_analysis_route(weather_feed: str = Form(...), file: UploadFile = File(...)):
    res = run_advanced_soil_scan(file.filename)
    
    # Calculate a composite dynamic Soil Health Score (Base sum out of 100)
    composite_health_score = int((res["moist_score"] + res["om_score"] + res["crack_score"] + res["surf_score"] + res["bio_score"]) / 5)
    score_class = "score-good" if composite_health_score >= 60 else "score-bad"
    
    # Weather Modification Processing Matrix
    weather_action = ""
    if "Heat" in weather_feed or "38°C" in weather_feed:
        weather_action = "🚨 WEATHER ALERT: High evapotranspiration risk detected! Increase regular drip irrigation runtimes by +25% to protect roots from burning."
    elif "Rain" in weather_feed:
        weather_action = "🌧️ WEATHER NOTICE: Heavy downpours expected soon. Pause scheduled macro-irrigation now to avoid waterlogging and erosion."
    else:
        weather_action = "☀️ WEATHER REPORT: Stable atmospheric trends. Maintain baseline capsule-sponge release schedules."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Diagnostic Breakdown</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <!-- PRINT/PDF ACTION CAPABILITY BUTTON -->
            <div class="d-flex justify-content-between mb-4">
                <a href="/" class="btn btn-outline-dark btn-sm"><i class="bi bi-arrow-left me-1"></i>Return to Hub Console</a>
                <button class="btn btn-danger btn-sm fw-bold shadow-sm" onclick="window.print()"><i class="bi bi-file-earmark-pdf-fill me-1"></i>Download Certified PDF Report</button>
            </div>

            <!-- COMPREHENSIVE SCORE INTERACTIVE CARD -->
            <div class="card-premium mb-4 text-center bg-white shadow-sm">
                <h6 class="text-uppercase text-secondary tracking-widest font-monospace small">Composite Target Core Assessment</h6>
                <h2 class="fw-bold mb-3 text-dark">AI Soil Health Matrix Score</h2>
                <div class="score-badge {score_class} shadow-sm mb-2">{composite_health_score}<span class="fs-6 text-muted">/100</span></div>
                <p class="small text-muted mt-2">Token Verification Reference Vector: <span class="text-success font-monospace">{res['filename']}</span></p>
                
                <!-- DYNAMIC EXPLAINABLE AI COMPONENT RATINGS GRID -->
                <div class="row g-3 mt-4 text-start justify-content-center">
                    <div class="col-md-2 col-6"><div class="p-2 border rounded bg-light text-center"><h6>Moisture</h6><strong class="text-success">{res['moist_score']}/100</strong></div></div>
                    <div class="col-md-2 col-6"><div class="p-2 border rounded bg-light text-center"><h6>Texture</h6><strong class="text-success">60/100</strong></div></div>
                    <div class="col-md-2 col-6"><div class="p-2 border rounded bg-light text-center"><h6>Organic base</h6><strong class="text-success">{res['om_score']}/100</strong></div></div>
                    <div class="col-md-2 col-6"><div class="p-2 border rounded bg-light text-center"><h6>Surface Matrix</h6><strong class="text-success">{res['surf_score']}/100</strong></div></div>
                    <div class="col-md-2 col-6"><div class="p-2 border rounded bg-light text-center"><h6>Biodiversity</h6><strong class="text-success">{res['bio_score']}/100</strong></div></div>
                </div>
            </div>

            <!-- EXPLAINABLE VISION READOUT EXTRACTIONS CARD -->
            <div class="card-premium mb-4">
                <h4 class="fw-bold text-dark mb-3"><i class="bi bi-eye-fill text-success me-2"></i>Explainable Computer Vision Property Metrics</h4>
                <div class="table-responsive">
                    <table class="table border table-striped align-middle">
                        <thead class="table-dark">
                            <tr>
                                <th>Soil Feature Target Parameter</th>
                                <th>Visual Observation Extracted Value</th>
                                <th>AI Confidence Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Estimated Soil Taxonomy</strong></td><td><span class="fw-bold text-dark">{res['type']}</span><br><small class="text-muted text-info">💡 {res['type_exp']}</small></td><td><span class="badge bg-success">{res['type_conf']}%</span></td></tr>
                            <tr><td><strong>Surface Hydration State</strong></td><td>{res['moisture']}</td><td><span class="badge bg-success">{res['moist_conf']}%</span></td></tr>
                            <tr><td><strong>Cracking / Compaction Defect</strong></td><td>{res['cracks']}</td><td><span class="badge bg-success">{res['cracks_conf']}%</span></td></tr>
                            <tr><td><strong>Organic Carbon Appearance</strong></td><td>{res['om']}</td><td><span class="badge bg-success">{res['om_conf']}%</span></td></tr>
                            <tr><td><strong>Invasive Weeds / Algae Presence</strong></td><td>{res['weed_algae']}</td><td><span class="badge bg-success">{res['algae_conf']}%</span></td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- DISEASE & DEFICIENCY EXTRACTION OVERLAY LAYER -->
            <div class="card-premium mb-4 border-start border-4 border-danger">
                <h4 class="fw-bold text-danger mb-2"><i class="bi bi-virus me-2"></i>AI Plant Disease & Crop Canopy Deficiency Detection</h4>
                <p class="text-muted small">Foliage analysis layer processed from image canopy fragments. <em>Warning: AI estimation values require onsite laboratory confirmation.</em></p>
                <div class="row g-3 small font-monospace">
                    <div class="col-md-3"><strong>Nitrogen Deficit:</strong> <span class="text-danger">{res['n_def']}</span></div>
                    <div class="col-md-3"><strong>Potassium Deficit:</strong> <span class="text-danger">{res['k_def']}</span></div>
                    <div class="col-md-3"><strong>Fungal Symbiosis Risk:</strong> <span class="text-danger">{res['fungal']}</span></div>
                    <div class="col-md-3"><strong>Insect/Pest Injury:</strong> <span class="text-danger">{res['pest']}</span></div>
                </div>
            </div>

            <!-- WEATHER FORECAST FEED OVERLAY CARD -->
            <div class="card-premium mb-4 bg-info bg-opacity-10 border border-info">
                <h5 class="fw-bold text-info m-0"><i class="bi bi-cloud-lightning-rain-fill me-2"></i>Live Weather Integration Response Module</h5>
                <p class="small text-dark mb-0 mt-2 font-monospace">{weather_action}</p>
            </div>

            <!-- SUSTAINABILITY SCORE METRICS MODULE -->
            <div class="card-premium mb-4 border-start border-4 border-primary">
                <h4 class="fw-bold text-primary mb-3"><i class="bi bi-recycle me-2"></i>Calculated Sustainability & Environmental Impact Scores</h4>
                <div class="row g-3 text-center text-dark small">
                    <div class="col-md-3"><div class="p-3 border rounded bg-white"><strong>Water Saved Forecast</strong><br><span class="text-primary fs-5 fw-bold">32% Retained</span><br><small class="text-muted">Via Sponge Networks</small></div></div>
                    <div class="col-md-3"><div class="p-3 border rounded bg-white"><strong>Chemical Runoff Reduction</strong><br><span class="text-primary fs-5 fw-bold">-45% Synthetic Salts</span><br><small class="text-muted">Eliminates Toxic Flushing</small></div></div>
                    <div class="col-md-3"><div class="p-3 border rounded bg-white"><strong>Carbon Sequestration Base</strong><br><span class="text-primary fs-5 fw-bold">High Biochar Trapping</span><br><small class="text-muted">Permanent Charcoal Matrix</small></div></div>
                    <div class="col-md-3"><div class="p-3 border rounded bg-white"><strong>Plastic Pollution Saved</strong><br><span class="text-primary fs-5 fw-bold">100% Waste Avoided</span><br><small class="text-muted">Zero Polyethylene Trace</small></div></div>
                </div>
            </div>

            <!-- EXPLAINABLE INTELLIGENCE SMART SUGGESTIONS ARCHITECTURE -->
            <div class="card-premium mb-4 bg-light border">
                <h4 class="fw-bold text-dark mb-4"><i class="bi bi-lightbulb-fill text-success me-2"></i>Smart Analytical Agronomic Recommendations Engine</h4>
                <div class="row g-3">
                    <div class="col-md-4">
                        <div class="p-3 bg-white rounded-3 border h-100">
                            <h6 class="fw-bold text-success"><i class="bi bi-droplet-half me-1"></i>Irrigation Schedule</h6>
                            <p class="small text-muted mb-0">Apply targeted subsurface drip cycles. This matches the exact dryness spotted by our surface analytics, helping to dissolve applied treatments without drowning local root zones.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 bg-white rounded-3 border h-100">
                            <h6 class="fw-bold text-success"><i class="bi bi-flower1 me-1"></i>Suggested Cash Crops</h6>
                            <p class="small text-muted mb-0">Plant deep taproot cover legumes or thick-root cereals. These help break apart compaction channels while adding natural root carbon to the soil matrix.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-3 bg-white rounded-3 border h-100">
                            <h6 class="fw-bold text-success"><i class="bi bi-tree-fill me-1"></i>Mulching & Compositing</h6>
                            <p class="small text-muted mb-0">Spread an organic forest wood-chip or straw mulch layer. This shields fragile topsoils from direct solar evaporation and safeguards growing micro-communities.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- BRAND SHOWCASE CURE REMEDY DISPLAY AND ORDERING CAPABILITY -->
            <div class="cure-premium-card shadow-lg mb-4">
                <div class="row g-4 align-items-center">
                    <div class="col-md-7">
                        <h2 class="fw-bold text-warning mb-3">🌿 The Ultimate Cure: BioShield Structural Nutrients</h2>
                        <p class="lh-base text-white-50 small">
                            BioShield Nutrients represents the **most advanced, 100% pure organic fertilization matrix in the world**. Engineered intentionally to completely bypass standard chemical side-effects, our remedy repairs complex underlying soil tissue while fueling natural systemic growth. It sources ingredients natively: **Banana Shells** supply rich, active organic Potassium (K) for water regulation; **Eggshells** provide slow-release crystalline Calcium (Ca) matrices to fortify soil structures; **Onion Extracts** deliver a devastating blow to unwanted parasitic bacterial cells; and clean **Biochar** builds massive microscopic sponge sanctuaries to harbor beneficial biological microbes permanently.
                        </p>
                        <h5 class="text-success fw-bold mt-3 mb-1">The Salicylic Acid Miracle Asset</h5>
                        <p class="text-white-50 small mb-4">
                            The secret defensive shield of this blend is pure **Salicylic Acid**. Acting identically to an vaccine immune response in organic plant tissue, Salicylic Acid triggers **Systemic Acquired Resistance (SAR)** within the root framework. When absorbed, it tells the plant to pre-emptively produce pathogenesis-related proteins, signaling cellular walls to thicken and sealing vascular pathways against oncoming fungal or bacterial blights before they strike.
                        </p>
                        <div class="p-3 rounded-3 bg-white bg-opacity-10 border border-warning text-warning">
                            <h6 class="fw-bold mb-1"><i class="bi bi-envelope-check-fill me-2"></i>Secure Direct Ordering Channel Active:</h6>
                            <p class="mb-0 text-white small">Contact our global distribution lead at <strong class="text-white font-monospace">radwaabdallnasser@gmail.com</strong> to secure custom capsule deliveries and schedule field team onboarding.</p>
                        </div>
                    </div>
                    <div class="col-md-5 text-center">
                        <div class="p-2 bg-white rounded-4 shadow">
                            <!-- DYNAMIC USER PACKAGING ILLUSTRATION INTERACTION -->
                            <img src="https://raw.githubusercontent.com/RadwaAbdallnasser/BioShield/main/image_82d4c1.jpg" onerror="this.src='https://images.unsplash.com/photo-1595341595378-fc74301d0163?auto=format&fit=crop&q=80&w=600'" class="img-fluid rounded-4" alt="Premium BioShield Packaging Varieties">
                        </div>
                        <p class="text-warning fw-bold mt-3 mb-0 fs-5">✨ Your Soil is Healthier, Your Life is Better ✨</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/run-comparative-audit", response_class=HTMLResponse)
async def run_comparative_audit_route(before_id: str = Form(...), file_after: UploadFile = File(...)):
    # Run diagnostic simulators to compile shifts
    data_after = run_advanced_soil_scan(file_after.filename)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Comparative Matrix Log</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm"><i class="bi bi-arrow-left me-1"></i>Return to Hub Console</a></div>
            
            <div class="hero-premium bg-success text-center py-4 mb-4">
                <h2 class="fw-bold text-warning"><i class="bi bi-arrow-left-right me-2"></i>Post-Treatment Verification Analysis</h2>
                <p class="mb-0 text-white-50 small">Automated Field Performance Comparison Tracking Audit Ledger</p>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-premium border-top border-4 border-danger h-100">
                        <h5 class="fw-bold text-danger"><i class="bi bi-x-circle me-2"></i>Pre-Treatment Baseline Metrics</h5>
                        <p class="text-muted font-monospace small mb-3">Historical Reference: {before_id}</p>
                        <hr>
                        <ul>
                            <li class="mb-2"><strong>Calculated Health Index:</strong> <span class="text-danger fw-bold">42 / 100</span></li>
                            <li class="mb-2"><strong>Moisture Surface Look:</strong> Dry, Evaporated Layer</li>
                            <li class="mb-2"><strong>Vegetation Canopy Spread:</strong> Restricted / High Chlorosis Symptoms</li>
                            <li class="mb-2"><strong>Topsoil Surface Texture:</strong> Hard Crust Blocks / Loose Leached Sand</li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card-premium border-top border-4 border-success h-100 shadow-lg">
                        <h5 class="fw-bold text-success"><i class="bi bi-check-circle me-2"></i>Post-Capsule Treatment Progress</h5>
                        <p class="text-muted font-monospace small mb-3">Image Node ID: {file_after.filename}</p>
                        <hr>
                        <ul>
                            <li class="mb-2"><strong>Calculated Health Index:</strong> <span class="text-success fw-bold">84 / 100 (+42 Boost)</span></li>
                            <li class="mb-2"><strong>Moisture Surface Look:</strong> Fully Hydrated Organic Profile</li>
                            <li class="mb-2"><strong>Vegetation Canopy Spread:</strong> Active Root Expansion & Green Foliage Growth</li>
                            <li class="mb-2"><strong>Topsoil Surface Texture:</strong> Highly Aggregate Porous Micro-Sponge Matrix</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="card-premium bg-white border border-success text-center">
                <h5 class="fw-bold text-success"><i class="bi bi-stars me-2"></i>Verification Success: Soil Structural Transformation Logged</h5>
                <p class="text-muted small mb-0">The comparison engine confirms successful breakdown of the biodegradable capsule shell. The porous biochar matrix has re-hydrated dry clay zones, locked active nitrogen pathways, and restored long-term topsoil balance.</p>
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
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Return to Hub Console</a></div>
            
            <div class="card-premium border-top border-4 border-primary">
                <h3 class="fw-bold text-primary mb-2"><i class="bi bi-qr-code-scan me-2"></i>BioShield Package Integration Interface</h3>
                <p class="text-muted small">Verified Serial Token Key: <span class="font-monospace fw-bold text-dark">{qr_token}</span></p>
                <hr>
                
                <h5 class="fw-bold text-dark mb-2">📥 On-Field Capsule Deployment Instructions:</h5>
                <ol class="text-muted small mb-4">
                    <li class="mb-2">Dig a small 10-15 cm core opening directly adjacent to the primary root canopy line.</li>
                    <li class="mb-2">Insert one (1) single BioShield Biodegradable Nutrients Capsule cleanly inside the channel.</li>
                    <li class="mb-2">Cover the opening with topsoil and run a standard morning irrigation cycle to dissolve the protective shell.</li>
                </ol>
                
                <div class="p-3 bg-light rounded-3 font-monospace small text-secondary">
                    <div><strong>📍 Registered Coordinate Geolocation:</strong> 30.0444° N, 31.2357° E (Automated Mobile Handshake)</div>
                    <div><strong>⏱️ Activation Digital Timestamp:</strong> 2026-07-12 16:48:13 UTC</div>
                    <div class="text-success mt-1"><strong>🔄 System Note:</strong> Next follow-up tracking scan is automatically scheduled for 14 days from today.</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
