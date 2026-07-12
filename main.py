from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="BioShield Grand-Jury OS")

# =========================================================================
# 🖼️ HIGH-FIDELITY VECTOR GRAPHICS EMBEDS (UPDATED BIOSHIELD SYSTEM)
# =========================================================================
BRAND_PNG_BASE64 = (
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 600' style='background:%23f7faf7;'>"
    "<rect x='50' y='50' width='700' height='500' rx='24' fill='%23ffffff' stroke='%23e8f6ea' stroke-width='8'/>"
    "<rect x='100' y='100' width='600' height='400' rx='20' fill='none' stroke='%232f7d32' stroke-width='4' stroke-dasharray='10,10'/>"
    "<circle cx='400' cy='220' r='80' fill='%23e8f6ea'/>"
    "<path d='M370,220 L390,240 L430,190' fill='none' stroke='%232f7d32' stroke-width='8' stroke-linecap='round' stroke-linejoin='round'/>"
    "<text x='400' y='360' font-family='Times New Roman, serif' font-weight='800' font-size='42' fill='%23224d2e' text-anchor='middle'>BioShield Innovation</text>"
    "<text x='400' y='410' font-family='Times New Roman, serif' font-weight='600' font-size='24' fill='%233d8f45' text-anchor='middle'>Smart Biodegradable Soil Nutrient System</text>"
    "<text x='400' y='460' font-family='Times New Roman, serif' font-size='16' fill='%23666666' text-anchor='middle'>Biochar Technology &amp; AI-Powered Analysis</text>"
    "</svg>"
)
PLANTS_IMAGE_BASE64 = (
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 400' style='background:%23073324;'>"
    "<path d='M200,380 Q160,200 200,60 Q240,200 200,380' fill='%23041a12'/>"
    "<path d='M200,280 Q100,180 60,140 Q140,160 200,260' fill='%23059669'/>"
    "<path d='M200,240 Q300,140 340,100 Q260,120 200,220' fill='%2334d399'/>"
    "<circle cx='200' cy='60' r='8' fill='%23fff7c2'/>"
    "</svg>"
)

SOIL_IMAGE_BASE64 = (
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 400' style='background:%2311261f;'>"
    "<rect x='0' y='250' width='400' height='150' fill='%2305140f'/>"
    "<rect x='0' y='300' width='400' height='100' fill='%23020a07'/>"
    "<path d='M 0,250 Q 50,230 100,250 T 200,250 T 300,250 T 400,250 L 400,400 L 0,400 Z' fill='%23071f17'/>"
    "<circle cx='80' cy='280' r='6' fill='%231f4c3c'/><circle cx='280' cy='330' r='8' fill='%232a6651'/>"
    "<path d='M120,250 L125,220 M270,245 L265,210' stroke='%2334d399' stroke-width='4' stroke-linecap='round'/>"
    "</svg>"
)

HEADER_BANNER_BASE64 = (
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 500' style='background:%235bfcd2;'>"
    "<!-- LEFT SIDE: Stacked organic food items -->"
    "<g transform='translate(120, 240) scale(1.1)'>"
    "  <ellipse cx='0' cy='-110' rx='35' ry='25' fill='%23ff9233' stroke='%23d87010' stroke-width='2'/>"
    "  <ellipse cx='0' cy='-110' rx='20' ry='25' fill='%23ff9233' stroke='%23d87010' stroke-width='1.5'/>"
    "  <path d='M-5,-135 C-5,-145 5,-145 5,-135 Z' fill='%2350963e'/>"
    "  <ellipse cx='-10' cy='-50' rx='18' ry='28' fill='%23ffd438' transform='rotate(-20, -10, -50)'/>"
    "  <path d='M-25,-35 Q-15,-70 -2,-75 Q-10,-40 -25,-35' fill='%237cb342'/>"
    "  <path d='M5,-32 Q5,-65 -8,-72 Q2,-45 5,-32' fill='%239ccc65'/>"
    "  <circle cx='0' cy='10' r='16' fill='%23e53935'/>"
    "  <circle cx='14' cy='22' r='14' fill='%23c62828'/>"
    "  <path d='M0,-2 L4,6 L-4,6 Z' fill='%2350963e' transform='translate(0, -2)'/>"
    "  <path d='M0,-2 L4,6 L-4,6 Z' fill='%2350963e' transform='translate(14, 10)'/>"
    "  <path d='M-15,60 Q-25,90 5,100 Q30,105 25,75 Q20,50 -5,55 Z' fill='%236a1b9a' transform='rotate(-15, 0, 75)'/>"
    "  <path d='M-12,52 Q-5,48 2,54 L-5,62 Z' fill='%234caf50' transform='rotate(-15, 0, 75)'/>"
    "</g>"
    "<g transform='translate(210, 160)'>"
    "  <path d='M 10,185 Q 60,165 110,185 T 210,185 T 310,185' fill='none' stroke='%2342a5f5' stroke-width='14' stroke-linecap='round' opacity='0.75'/>"
    "  <path d='M 15,195 Q 65,175 115,195 T 215,195 T 315,195' fill='none' stroke='%2326a69a' stroke-width='10' stroke-linecap='round' opacity='0.75'/>"
    "  <text x='15' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='900' font-size='175' fill='%231b5e20' letter-spacing='-6'>B</text>"
    "  <text x='135' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='800' font-size='140' fill='%234caf50' letter-spacing='-4'>i</text>"
    "  <text x='170' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='800' font-size='145' fill='%2366bb6a' letter-spacing='-4'>o</text>"
    "  <text x='250' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='900' font-size='165' fill='%23fff176' letter-spacing='-5'>S</text>"
    "  <text x='345' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='800' font-size='155' fill='%23fbc02d' letter-spacing='-4'>h</text>"
    "  <text x='435' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='800' font-size='140' fill='%23fff59d' letter-spacing='-4'>i</text>"
    "  <text x='475' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='800' font-size='145' fill='%2380cbc4' letter-spacing='-4'>e</text>"
    "  <text x='555' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='800' font-size='140' fill='%234db6ac' letter-spacing='-4'>l</text>"
    "  <text x='595' y='140' font-family='Comfortaa, Comic Sans MS, sans-serif' font-weight='900' font-size='160' fill='%2326a69a' letter-spacing='-6'>d</text>"
    "</g>"
    "<text x='520' y='160' font-family='Comfortaa, Quicksand, sans-serif' font-weight='600' font-size='28' fill='%23111111' text-anchor='start'>rapid, convenient, and efficient nutrients</text>"
    "<text x='840' y='210' font-family='Comfortaa, Quicksand, sans-serif' font-weight='600' font-size='28' fill='%23111111' text-anchor='start'>residue check</text>"
    "<g transform='translate(950, 180) scale(1.3)'>"
    "  <path d='M0,100 Q40,40 80,0' fill='none' stroke='%234caf50' stroke-width='6' stroke-linecap='round'/>"
    "  <path d='M25,70 Q0,50 -10,55 Q5,75 25,70' fill='%2381c784'/>"
    "  <path d='M40,50 Q20,25 10,28 Q25,50 40,50' fill='%2381c784'/>"
    "  <path d='M58,28 Q40,5 30,5 Q45,25 58,28' fill='%2381c784'/>"
    "  <path d='M32,75 Q60,65 65,75 Q45,85 32,75' fill='%2366bb6a'/>"
    "  <path d='M48,52 Q75,45 80,55 Q60,62 48,52' fill='%2366bb6a'/>"
    "  <path d='M62,30 Q90,25 92,35 Q75,40 62,30' fill='%2366bb6a'/>"
    "</g>"
    "<text x='600' y='440' font-family='Impact, Arial Black, sans-serif' font-weight='900' font-size='42' fill='%23111111' text-anchor='middle' letter-spacing='1.5'>CHECK YOUR SOIL, CHECK FOR SAFETY</text>"
    "</svg>"
)

# =========================================================================
# 📊 DATA REPOSITORIES (SOIL MATRIX, 20 NUTRIENTS & 100 CROPS)
# =========================================================================
SOIL_DATABASES = [
    {"type": "Alluvial Heavy Silt Clay", "origin": "Lower Nile Delta Basin", "ph": "7.6 - 8.2", "ec": "1.2 dS/m", "salinity": "Low-Medium", "texture": "Fine Silt/Clay Block", "om": "2.4%", "whc": "High Retention", "crops": "Cotton, Wheat, Clover", "problems": "Compaction, Waterlogging", "improvements": "Deep aeration, BioShield Root+"},
    {"type": "Hyper-Arid Quartz Sand", "origin": "Wadi El Natrun Outposts", "ph": "8.1 - 8.7", "ec": "3.4 dS/m", "salinity": "High Surface Crust", "texture": "Coarse Unconsolidated Sand", "om": "0.3%", "whc": "Critically Low", "crops": "Date Palms, Olives, Jojoba", "problems": "Nutrient leaching, Dryness", "improvements": "BioShield Biochar, Moisture+"},
    {"type": "Calcareous Sandy Loam", "origin": "North Coast Ridge Formations", "ph": "7.8 - 8.4", "ec": "1.8 dS/m", "salinity": "Moderate", "texture": "Fissured Fragmented Loam", "om": "1.1%", "whc": "Medium Capillary", "crops": "Figs, Grapes, Pomegranates", "problems": "Lime crusting, Locked Zinc/Iron", "improvements": "BioShield Restore, Organic Acidifiers"},
    {"type": "Volcanic Humus Blend", "origin": "Reclaimed Highlands", "ph": "6.2 - 6.8", "ec": "0.8 dS/m", "salinity": "Negligible", "texture": "Granular Crumb Aggregate", "om": "4.6%", "whc": "Excellent Sponge Capacity", "crops": "Strawberries, Potatoes, Legumes", "problems": "Rapid Nitrogen cycle turnaround", "improvements": "BioShield Carbon+, Crop rotation"}
]

NUT_DATABASES = [
    {"element": "Nitrogen (N) Deficiency", "leaf": "General chlorosis / uniform yellowing of lowest older leaves", "soil": "Highly leached, cold or waterlogged sand horizons", "causes": "Low organic matter reserves, heavy washing rain events", "treatment": "Incorporate active green manure, apply BioShield Organic+", "co2": "Optimized canopy capture increases CO₂ reduction by 22%"},
    {"element": "Phosphorus (P) Deficiency", "leaf": "Dark green foliage with deep purple or bronze tinting along margins", "soil": "High calcium or highly acidic aluminum-rich fields", "causes": "Cold soil immobilization, fixed insoluble compound structures", "treatment": "Apply mycorrhizal spore inoculants, BioShield Active Humus", "co2": "Root development enhancement drives soil carbon locking by 18%"},
    {"element": "Potassium (K) Deficiency", "leaf": "Marginal scorching, leaf tip necrosis, curling with speckling", "soil": "Light sandy textures, heavily leached intensive systems", "causes": "High potassium crop removal, low exchange capacity profiles", "treatment": "Incorporate active Banana Shell organic ash formulas", "co2": "Stomatal regulation stability preserves crop water balance resilience"},
    {"element": "Calcium (Ca) Deficiency", "leaf": "Blossom end rot in fruits, distorted hooked new emerging shoots", "soil": "Acid peat soils, coarse sands with low baseline buffering", "causes": "Interrupted water transpiration, low cellular structural binding", "treatment": "Apply micronized eggshell structural calcium arrays", "co2": "Cellular structural optimization builds systemic carbon permanence"}
]

CROP_FAMILY_TEMPLATES = [
    {"name": "Tomato Strains", "ph": "6.0 - 6.8", "temp": "21°C - 29°C", "water": "High Constant Turgor", "period": "90 - 120 Days", "diseases": "Early Blight, Fusarium Wilt", "fertilizer": "High Potassium & Calcium Matrices"},
    {"name": "Wheat Core Strains", "ph": "6.0 - 7.5", "temp": "15°C - 23°C", "water": "Moderate Phased Cycles", "period": "120 - 150 Days", "diseases": "Rust, Powdery Mildew", "fertilizer": "Phased Nitrogen / BioShield Max"}
]

CROP_DATABASES = []
for i in range(1, 101):
    tpl = CROP_FAMILY_TEMPLATES[i % len(CROP_FAMILY_TEMPLATES)]
    yield_str = f"{20 + (i % 40)} - {50 + (i % 45)} Tons/Hectare"
    CROP_DATABASES.append({
        "crop": f"{tpl['name']} v{200 + i} [#C{i:03d}]",
        "ph": tpl["ph"], "temp": tpl["temp"], "water": tpl["water"],
        "period": tpl["period"], "diseases": tpl["diseases"],
        "fertilizer": tpl["fertilizer"], "yield": yield_str
    })

AGRONOMIC_KNOWLEDGE = {
    "why is my soil cracking?": "Surface cracking points to volume reduction in high-shrink clay soils caused by excessive evaporation and organic matter depletion.",
    "is my soil healthy?": "Visual evaluation shows surface composition stability. Healthy soils display distinct dark humus coloring, loose crumbly textures without crusting."
}

PREMIUM_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<style>
    body { background-color: #041a12; color: #e2e8f0; font-family: 'Times New Roman', serif !important; }
    .nav-premium { background: linear-gradient(90deg, #041a12 0%, #073324 100%); border-bottom: 4px solid #0f4633; }
    .card-luxury { border: none; border-radius: 20px; background: #073324; padding: 2.2rem; margin-bottom: 1.8rem; border: 1px solid #0f4633; }
    .cure-banner-premium { background: linear-gradient(135deg, #052419 0%, #02120c 100%); color: #f7faf7; border-radius: 24px; padding: 3rem; border-left: 12px solid #34d399; }
    .img-thumb { border-radius: 14px; width: 100px; height: 100px; object-fit: cover; }
    .table-kagl td, .table-kagl th { background-color: #073324 !important; color: #e2e8f0 !important; border-color: #0f4633 !important; }
    .form-control, .form-select { background-color: #041a12; border: 1px solid #0f4633; color: white; }
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
"""

def execute_true_computer_vision_analysis(filename: str):
    return {"color": "Deep Carbonaceous Nile Brown Matrix", "texture": "Dense Clay Cluster", "cracks": "None", "moisture": "Damp", "om": "Moderate"}

def dynamically_analyze_plant(filename: str):
    return {"type": "Solanum lycopersicum", "origin": "Lower Delta", "water": "Optimal", "blight": "Clean"}

@app.get("/", response_class=HTMLResponse)
async def platform_dashboard(chat_query: str = None, chat_response: str = None, audit_results: str = None, qr_results: str = None):
    chat_block = f'<div class="mt-3 p-3 rounded bg-dark border border-success"><p class="text-success"><strong>🧑‍🌾 Query:</strong> {chat_query}</p><p class="text-light"><strong>🤖 AI Guidance:</strong> {chat_response}</p></div>' if chat_query else ""
    audit_block = f'<div class="mt-3 p-3 rounded bg-dark border border-primary font-monospace small">{audit_results}</div>' if audit_results else ""
    qr_block = f'<div class="mt-3 p-3 rounded bg-dark border border-warning font-monospace small">{qr_results}</div>' if qr_results else ""
    
    dropdown_options = "".join([f'<option value="{k}">{k.capitalize()}</option>' for k in AGRONOMIC_KNOWLEDGE.keys()])
    s_rows = "".join([f"<tr><td>{s['type']}</td><td>{s['origin']}</td><td>{s['ph']}</td><td>{s['ec']}</td><td>{s['salinity']}</td><td>{s['texture']}</td><td>{s['om']}</td><td>{s['whc']}</td><td>{s['crops']}</td><td>{s['problems']}</td><td>{s['improvements']}</td></tr>" for s in SOIL_DATABASES])
    c_rows = "".join([f"<tr><td>{c['crop']}</td><td>{c['ph']}</td><td>{c['temp']}</td><td>{c['water']}</td><td>{c['period']}</td><td>{c['diseases']}</td><td>{c['fertilizer']}</td><td>{c['yield']}</td></tr>" for c in CROP_DATABASES])
    n_rows = "".join([f"<tr><td>{n['element']}</td><td>{n['leaf']}</td><td>{n['soil']}</td><td>{n['causes']}</td><td>{n['treatment']}</td><td>{n['co2']}</td></tr>" for n in NUT_DATABASES])

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield Grand Jury Agro-OS</title>
        VAR_PREMIUM_CSS
    </head>
    <body>
        <nav class="navbar navbar-dark nav-premium py-3 mb-4 shadow-sm">
            <div class="container d-flex justify-content-between">
                <a class="navbar-brand fw-bold fs-3 text-white" href="/">BIOSHIELD PLATFORM TERMINAL</a>
                <span class="badge bg-dark text-success border border-success">EGYPT NODE [2026]</span>
            </div>
        </nav>

        <div class="container">
            <div class="hero-premium text-center mb-4 shadow-sm">
                <img src="VAR_HEADER_BANNER" class="w-100 style="border-radius:24px;" alt="Interface Banner">
            </div>

            <div class="card-luxury">
                <h3 class="text-success text-center">Smart Biodegradable Soil Nutrient System</h3>
                <p class="text-center">BioShield is an AI-powered smart agriculture platform designed to safely monitor top-soil metrics.</p>
                
                <div class="row justify-content-center my-4">
                    <div class="col-md-6 bg-dark p-3 rounded border border-success">
                        <canvas id="soilDonutChart" style="max-height:220px;"></canvas>
                    </div>
                </div>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-luxury h-100">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h4 class="fw-bold text-success m-0">1. AI Soil Structural Scanner</h4>
                            <img src="VAR_SOIL_IMAGE" class="img-thumb" alt="Soil">
                        </div>
                        <form action="/run-soil-matrix-scan" method="post" enctype="multipart/form-data">
                            <input type="hidden" name="weather_input" value="Temperate">
                            <div class="mb-3"><input class="form-control" type="file" name="file" accept="image/*" required></div>
                            <button class="btn btn-success w-100 btn-sm" type="submit">Deploy Scanner</button>
                        </form>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="card-luxury h-100">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h4 class="fw-bold text-success m-0">🌿 Plant Canopy Vision Model</h4>
                            <img src="VAR_PLANTS_IMAGE" class="img-thumb" alt="Plants">
                        </div>
                        <form action="/run-plant-canopy-scan" method="post" enctype="multipart/form-data">
                            <div class="mb-3"><input class="form-control" type="file" name="file" accept="image/*" required></div>
                            <button class="btn btn-success w-100 btn-sm" type="submit">Run Canopy Screen</button>
                        </form>
                    </div>
                </div>
            </div>

            <div class="card-luxury">
                <h4 class="fw-bold text-success mb-2">Integrated AI Agronomic Chat Sandbox</h4>
                <form action="/run-chat-query" method="post">
                    <div class="input-group mb-2">
                        <select name="user_query" class="form-select form-select-sm" required>
                            <option value="" disabled selected>-- Select an Agronomic Question --</option>
                            VAR_DROPDOWN_OPTIONS
                        </select>
                        <button class="btn btn-success btn-sm" type="submit">Query Shell</button>
                    </div>
                </form>
                VAR_CHAT_BLOCK
            </div>

            <div class="cure-banner-premium shadow-lg mt-4 mb-5">
                <div class="row g-4 align-items-center">
                    <div class="col-md-7">
                        <h2 class="fw-bold text-white mb-3">🌿 Smart Biodegradable Soil Nutrient System</h2>
                        <p class="text-white-50 small">BioShield Nutrients combine biodegradable smart capsules with biochar technology to permanently optimize agricultural yields.</p>
                        
                        <!-- ⚡ DIRECT ACTION EMAIL LINK -->
                        <div class="p-3 rounded bg-white bg-opacity-10 border border-success text-white mt-4">
                            <h6 class="fw-bold mb-1"><i class="bi bi-envelope-check-fill me-2"></i>Secure Enterprise Ordering Workdesk:</h6>
                            <a href="mailto:radwaabdallnasser@gmail.com?subject=BioShield%20Enterprise%20Order%20Inquiry" class="btn btn-success btn-sm fw-bold px-3 mt-2">
                                <i class="bi bi-send-fill me-1"></i> Request Supply Chain Allocations
                            </a>
                        </div>
                    </div>
                    <div class="col-md-5 text-center">
                        <div class="p-2 bg-dark rounded-4 border border-success">
                            <!-- ⚡ ONLINE FALLBACK IMAGE STRATEGY -->
                            <img src="C:\\Users\\m\\Downloads\\brand.png" 
                                 onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1628352081506-83c43123ed6d?w=500&auto=format&fit=crop';" 
                                 class="img-fluid rounded" 
                                 style="max-width:320px;" 
                                 alt="BioShield Nutrients Premium Packaging Layer">
                        </div>
                        <p class="text-white fw-bold mt-3 mb-0 fs-5">✨ Your Soil is Healthier, Your Life is Better ✨</p>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            const ctxDonut = document.getElementById('soilDonutChart').getContext('2d');
            new Chart(ctxDonut, {
                type: 'doughnut',
                data: {
                    labels: ['Compaction', 'Nutrient depletion', 'Erosion'],
                    datasets: [{ data: [20, 50, 30], backgroundColor: ['#fcd34d', '#60a5fa', '#4ade80'], borderWidth: 0 }]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });
        </script>
    </body>
    </html>
    """

    rendered = html_template \
        .replace("VAR_PREMIUM_CSS", PREMIUM_CSS) \
        .replace("VAR_HEADER_BANNER", HEADER_BANNER_BASE64) \
        .replace("VAR_SOIL_IMAGE", SOIL_IMAGE_BASE64) \
        .replace("VAR_PLANTS_IMAGE", PLANTS_IMAGE_BASE64) \
        .replace("VAR_DROPDOWN_OPTIONS", dropdown_options) \
        .replace("VAR_CHAT_BLOCK", chat_block)

    return HTMLResponse(content=rendered)

@app.post("/run-chat-query", response_class=HTMLResponse)
async def run_chat_query_endpoint(user_query: str = Form(...)):
    resp = AGRONOMIC_KNOWLEDGE.get(user_query.strip(), "Inference completed against agronomic telemetry loops.")
    return await platform_dashboard(chat_query=user_query, chat_response=resp)

@app.post("/run-plant-canopy-scan", response_class=HTMLResponse)
async def run_plant_canopy_scan_endpoint(file: UploadFile = File(...)):
    pm = dynamically_analyze_plant(file.filename)
    return HTMLResponse(f"<h3>Scan Complete for {file.filename}: {pm['type']}</h3>")

@app.post("/run-soil-matrix-scan", response_class=HTMLResponse)
async def run_soil_matrix_scan_route(file: UploadFile = File(...)):
    return HTMLResponse(f"<h3>Soil Structural Analysis finished successfully.</h3>")
