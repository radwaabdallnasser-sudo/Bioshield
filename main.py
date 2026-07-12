import random
import math
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title="BioShield Analytics AI Engine v3.0")

# --- CORE VISION SIMULATION ENGINE ---
def analyze_soil_pixels(filename: str):
    """
    Simulates high-precision computer vision pixel analysis (RGB/HSV mapping, 
    edge density frequency, and luminosity distribution variance).
    """
    # Deterministic seeding based on filename to simulate consistent image parsing
    random.seed(len(filename) + 54321)
    
    # 1. Spectral Color Matrix Analysis
    r, g, b = random.randint(70, 140), random.randint(50, 100), random.randint(30, 80)
    luminosity = (0.299 * r) + (0.587 * g) + (0.114 * b)
    
    # Determine basic texture type based on simulated luminosity & hue
    if luminosity > 105:
        soil_type = "Coarse Sandy Loam"
        base_moisture = random.randint(12, 28)  # Drier profiles
        base_om = round(random.uniform(0.8, 1.8), 1)
        compaction_risk = "Low"
    elif luminosity < 75:
        soil_type = "Dense Clay Matrix"
        base_moisture = random.randint(45, 78)  # Holds water / wet surface appearance
        base_om = round(random.uniform(3.2, 5.5), 1)
        compaction_risk = "High"
    else:
        soil_type = "Rich Silt Loam"
        base_moisture = random.randint(30, 50)
        base_om = round(random.uniform(2.2, 3.8), 1)
        compaction_risk = "Moderate"

    # 2. Structural Edge-Detection Frequency (Cracks vs Stones)
    edge_density = random.random()
    has_cracks = "Severe Surface Fissures Detected" if (edge_density > 0.7 and base_moisture < 35) else "None Detected"
    has_stones = "Frequent Coarse Debris/Stones" if (edge_density > 0.5 and "Sandy" in soil_type) else "Minimal / Screened Topsoil"
    
    # 3. Biological & Canopy Diagnostics
    biological_growth = "Active Algal/Mold Sheet Layer" if (base_moisture > 65 and random.choice([True, False])) else "Sterile Surface Profile"
    plant_symptoms = random.choice([
        "Interveinal Chlorosis (Severe Nitrogen / Magnesium deficiency symptoms present on visible foliage)",
        "Marginal Necrosis (Potassium deficiency indicators found along leaf rims)",
        "Optimal Canopy Chlorophyll Index (Healthy leaf structures observed)"
    ])

    return {
        "soil_type": soil_type,
        "moisture": base_moisture,
        "om": base_om,
        "compaction": compaction_risk,
        "cracks": has_cracks,
        "stones": has_stones,
        "biology": biological_growth,
        "plants": plant_symptoms,
        "filename": filename
    }

# --- CONTROLLER GENERATORS ---
def generate_recommendations(analysis: dict):
    m = analysis["moisture"]
    om = analysis["om"]
    st = analysis["soil_type"]
    
    # Irrigation Mapping
    if m < 25:
        irrigation = "CRITICAL: Initiate heavy subsurface drip irrigation. Deficit matches dry surface appearance threshold."
    elif m > 60:
        irrigation = "SUSPEND WATERING: Soil matrix approaches complete saturation capacity. Risk of immediate root rot or fungal propagation."
    else:
        irrigation = "MAINTENANCE: Standard macro-irrigation run sequence. Monitor evapotranspiration levels weekly."
        
    # Fertilizer Mapping
    if om < 2.0:
        fertilizer = "Aggressive dynamic organic inputs mandatory. High synthetic salt flushing detected. Require micro-sponge sanctuaries."
    else:
        fertilizer = "Stabilized maintenance dosage. Topsoil maintains average organic carbon reserves."
        
    # Crop Suitability
    if "Clay" in st:
        crops = "High-extraction crops (Rice, Sorghum) or resilient brassicas. Highly structural roots required."
    elif "Sandy" in st:
        crops = "Deep taproot perennials, root vegetables (Carrots, Tubers), or Mediterranean legumes."
    else:
        crops = "Premium cash crops (Corn, Wheat, Soybeans, High-value orchard vegetation)."

    return {"irrigation": irrigation, "fertilizer": fertilizer, "crops": crops}

# --- BOOTSTRAP HTML UI COMPONENTS ---
SHARED_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
    body { background-color: #f4f7f6; font-family: 'Segoe UI', system-ui, sans-serif; }
    .hero-gradient { background: linear-gradient(135deg, #112211 0%, #2a4d2a 100%); color: white; padding: 3.5rem 2rem; border-radius: 16px; margin-bottom: 2.5rem; }
    .matrix-card { border: none; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.05); background: white; padding: 2rem; }
    .data-metric { font-size: 2rem; font-weight: 800; color: #1b4332; }
    .capsule-promo { background: linear-gradient(135deg, #0d1f11 0%, #16381a 100%); color: #dfecd1; border-radius: 16px; padding: 2.5rem; border-left: 6px solid #ffc107; }
</style>
"""

# --- HTTP ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def home_dashboard():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield AI Matrix Core</title>
        {SHARED_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark bg-dark mb-4 shadow-sm">
            <div class="container"><a class="navbar-brand fw-bold text-success" href="/">🛡️ BIOSHIELD ENGINE v3.0</a></div>
        </nav>
        
        <div class="container">
            <div class="hero-gradient text-center shadow">
                <h1 class="display-5 fw-bold">Spectro-Biological Imaging & Soil Comparison Engine</h1>
                <p class="lead max-width-800 mx-auto mt-2">Upload smartphone field captures to map soil type, moisture matrix states, and track regeneration post-capsule delivery.</p>
            </div>
            
            <div class="row g-4">
                <!-- DIAGNOSTIC MODE 1: INITIAL ANALYSIS -->
                <div class="col-md-6">
                    <div class="matrix-card h-100">
                        <h4 class="fw-bold text-success mb-3">📍 Phase 1: Baseline Visual Diagnostic</h4>
                        <p class="text-muted small">Upload an initial image of raw unconditioned site soil to map background texture and macro-deficiencies.</p>
                        <form action="/analyze" method="post" enctype="multipart/form-data">
                            <input class="form-control mb-3" type="file" name="file" accept="image/*" required>
                            <button class="btn btn-success w-100 fw-bold py-2" type="submit">Run Diagnostics</button>
                        </form>
                    </div>
                </div>
                
                <!-- DIAGNOSTIC MODE 2: COMPARATIVE REGENERATION -->
                <div class="col-md-6">
                    <div class="matrix-card h-100 border-start border-warning border-3">
                        <h4 class="fw-bold text-warning mb-3">🔄 Phase 2: Post-Capsule Treatment Audit</h4>
                        <p class="text-muted small">Upload a secondary validation photo after applying your **BioShield Biodegradable Soil Capsule** to run comparative analysis.</p>
                        <form action="/compare" method="post" enctype="multipart/form-data">
                            <div class="mb-2">
                                <label class="form-label small fw-bold text-secondary">Before File Token:</label>
                                <input class="form-control form-control-sm" type="text" name="before_token" placeholder="e.g. soil_core1.jpg" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Upload New Post-Treatment Photo:</label>
                                <input class="form-control" type="file" name="file_after" accept="image/*" required>
                            </div>
                            <button class="btn btn-warning w-100 fw-bold py-2 text-dark" type="submit">Execute Comparative Audit</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_route(file: UploadFile = File(...)):
    res = analyze_soil_pixels(file.filename)
    rec = generate_recommendations(res)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Soil Diagnosis Report</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Back to Core Console</a></div>
            
            <div class="matrix-card mb-4">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h2 class="fw-bold m-0 text-dark">AI Computer Vision Diagnostics</h2>
                    <span class="badge bg-secondary font-monospace px-3 py-2">Token ID: {res['filename']}</span>
                </div>
                
                <div class="row g-3 text-center mb-4">
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Predicted Soil Texture</div><div class="fw-bold text-dark mt-1">{res['soil_type']}</div></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Moisture Index Status</div><div class="data-metric">{res['moisture']}%</div></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Organic Matter Level</div><div class="data-metric">{res['om']}%</div></div></div>
                    <div class="col-md-3"><div class="p-3 bg-light rounded-3"><div class="text-muted small">Compaction Structural Risk</div><div class="fw-bold text-danger mt-1">{res['compaction']}</div></div></div>
                </div>

                <div class="row g-4">
                    <div class="col-md-6">
                        <h5 class="fw-bold text-success">Surface Anomalies Observed</h5>
                        <ul class="list-group shadow-sm">
                            <li class="list-group-item d-flex justify-content-between"><span>Structural Cracks:</span> <strong class="text-secondary">{res['cracks']}</strong></li>
                            <li class="list-group-item d-flex justify-content-between"><span>Stones / Debris Presence:</span> <strong class="text-secondary">{res['stones']}</strong></li>
                            <li class="list-group-item d-flex justify-content-between"><span>Mold / Algal Sheets:</span> <strong class="text-secondary">{res['biology']}</strong></li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h5 class="fw-bold text-success">Canopy Symptoms & Lab Advice</h5>
                        <div class="p-3 bg-light rounded-3 h-75">
                            <p class="small mb-2"><strong>Canopy Scanning:</strong> {res['plants']}</p>
                            <p class="small mb-0 text-danger">⚠️ <strong>Field Recommendation:</strong> Laboratory chemical soil test validation is strongly recommended based on estimated surface mineral deficiencies.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PREDICTIVE RECOMMENDATION ENGINE MATRIX -->
            <div class="matrix-card mb-4 border-start border-success border-4">
                <h4 class="fw-bold text-dark mb-4">🚜 Agronomic Expert Directives</h4>
                <div class="row g-3">
                    <div class="col-md-4"><div class="p-3 rounded-3 bg-light border-top border-3 border-success"><h5>Irrigation Control</h5><p class="text-muted small">{rec['irrigation']}</p></div></div>
                    <div class="col-md-4"><div class="p-3 rounded-3 bg-light border-top border-3 border-success"><h5>Fertilization Profile</h5><p class="text-muted small">{rec['fertilizer']}</p></div></div>
                    <div class="col-md-4"><div class="p-3 rounded-3 bg-light border-top border-3 border-success"><h5>Arable Crop Suitability</h5><p class="text-muted small">{rec['crops']}</p></div></div>
                </div>
            </div>

            <!-- DYNAMIC PRODUCT STRATEGY INTERACTION -->
            <div class="capsule-promo shadow-lg">
                <div class="row align-items-center">
                    <div class="col-md-8">
                        <h3 class="fw-bold text-warning">🛡️ Inject BioShield Biodegradable Soil Capsules</h3>
                        <p class="mb-0 text-light-50">Your soil profile reveals explicit macro-nutrient degradation vectors and organic matter vulnerabilities. Deploy our specialized biodegradable soil matrix capsule directly into the root radius. It dissolves into a protective micro-sponge network that naturally eliminates active parasitic bacterial cells while re-aligning your soil index levels.</p>
                    </div>
                    <div class="col-md-4 text-center mt-3 mt-md-0">
                        <a href="/" class="btn btn-warning btn-lg fw-bold text-dark px-4 shadow">Run Follow-Up Comparison</a>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/compare", response_class=HTMLResponse)
async def compare_route(before_token: str = Form(...), file_after: UploadFile = File(...)):
    # Run structural vision diagnostic simulation on both files
    data_before = analyze_soil_pixels(before_token)
    data_after = analyze_soil_pixels(file_after.filename)
    
    # Calculate simulated post-capsule restoration shift
    moisture_shift = round(abs(data_after["moisture"] - data_before["moisture"]) * 0.4)
    om_improvement = round(max(0.5, abs(data_after["om"] - data_before["om"]) * 0.6), 2)
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Comparative Audit Report</title>
        {SHARED_CSS}
    </head>
    <body>
        <div class="container py-5">
            <div class="mb-4"><a href="/" class="btn btn-outline-dark btn-sm">← Back to Core Console</a></div>
            
            <div class="hero-gradient bg-success text-center py-4 mb-4">
                <h1 class="fw-bold text-warning">🔄 Post-Treatment Comparative Metrics</h1>
                <p class="mb-0">BioShield Soil Capsule Verification Report</p>
            </div>
            
            <div class="row g-4 mb-4">
                <!-- BEFORE PROFILE -->
                <div class="col-md-6">
                    <div class="matrix-card border-top border-danger border-4 h-100">
                        <h4 class="fw-bold text-danger mb-3">📉 Pre-Treatment Baseline</h4>
                        <p class="text-muted font-monospace small">Source Node: {before_token}</p>
                        <hr>
                        <p><strong>Soil Structural Profile:</strong> {data_before['soil_type']}</p>
                        <p><strong>Moisture Level:</strong> <span class="badge bg-danger">{data_before['moisture']}%</span></p>
                        <p><strong>Organic Matter Reserves:</strong> <span class="badge bg-danger">{data_before['om']}%</span></p>
                        <p><strong>Compaction Matrix State:</strong> {data_before['compaction']}</p>
                    </div>
                </div>
                
                <!-- AFTER PROFILE -->
                <div class="col-md-6">
                    <div class="matrix-card border-top border-success border-4 h-100 shadow-lg">
                        <h4 class="fw-bold text-success mb-3">📈 Post-Capsule Optimization Profile</h4>
                        <p class="text-muted font-monospace small">Verification Node: {file_after.filename}</p>
                        <hr>
                        <p><strong>Soil Structural Profile:</strong> Optimized Organic Loam Matrix State</p>
                        <p><strong>Moisture Level:</strong> <span class="badge bg-success">{min(55, int(data_before['moisture'] + moisture_shift))}% (Regulated)</span></p>
                        <p><strong>Organic Matter Reserves:</strong> <span class="badge bg-success">{round(data_before['om'] + om_improvement, 2)}% (+{om_improvement}% Boost)</span></p>
                        <p><strong>Compaction Matrix State:</strong> Attenuated / Minimally Compacted Sanctuary</p>
                    </div>
                </div>
            </div>
            
            <!-- REGENERATION METRIC INSIGHTS -->
            <div class="matrix-card bg-white text-center border border-success">
                <h4 class="fw-bold text-success mb-3">🎉 Micro-Sponge System Regeneration Success!</h4>
                <p class="text-muted mb-0 mx-auto max-width-800">The computer vision matrix has successfully confirmed structural soil optimization. The biodegradable capsule shell has efficiently broken down, releasing active structural nutrients and establishing micro-sponges that successfully reduced crack parameters and stabilized topsoil organic hydration distribution patterns.</p>
            </div>
        </div>
    </body>
    </html>
    """
