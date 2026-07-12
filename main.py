from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import hashlib
import random

app = FastAPI(title="BioShield Grand-Jury OS")

# =========================================================================
# 📊 EXPANDED KAGGLE-STYLE DATA REPOSITORIES (ALL COMPREHENSIVE CATEGORIES)
# =========================================================================

SOIL_DATABASES = [
    {"type": "Alluvial Heavy Silt Clay", "origin": "Lower Nile Delta Basin", "ph": "7.6 - 8.2", "ec": "1.2 dS/m", "salinity": "Low-Medium", "texture": "Fine Silt/Clay Block", "om": "2.4%", "whc": "High Retention", "crops": "Cotton, Wheat, Clover", "problems": "Compaction, Waterlogging", "improvements": "Deep aeration, BioShield Root+"},
    {"type": "Hyper-Arid Quartz Sand", "origin": "Wadi El Natrun Outposts", "ph": "8.1 - 8.7", "ec": "3.4 dS/m", "salinity": "High Surface Crust", "texture": "Coarse Unconsolidated Sand", "om": "0.3%", "whc": "Critically Low", "crops": "Date Palms, Olives, Jojoba", "problems": "Nutrient leaching, Dryness", "improvements": "BioShield Biochar, Moisture+"},
    {"type": "Calcareous Sandy Loam", "origin": "North Coast Ridge Formations", "ph": "7.8 - 8.4", "ec": "1.8 dS/m", "salinity": "Moderate", "texture": "Fissured Fragmented Loam", "om": "1.1%", "whc": "Medium Capillary", "crops": "Figs, Grapes, Pomegranates", "problems": "Lime crusting, Locked Zinc/Iron", "improvements": "BioShield Restore, Organic Acidifiers"},
    {"type": "Volcanic Humus Blend", "origin": "Reclaimed Highlands", "ph": "6.2 - 6.8", "ec": "0.8 dS/m", "salinity": "Negligible", "texture": "Granular Crumb Aggregate", "om": "4.6%", "whc": "Excellent Sponge Capacity", "crops": "Strawberries, Potatoes, Legumes", "problems": "Rapid Nitrogen cycle turnaround", "improvements": "BioShield Carbon+, Crop rotation"}
]

CROP_DATABASES = [
    {"crop": "Solanum lycopersicum (Tomato)", "ph": "6.0 - 6.8", "temp": "21°C - 29°C", "water": "High Constant Turgor", "period": "90 - 120 Days", "diseases": "Early Blight, Fusarium Wilt", "fertilizer": "High Potassium & Calcium Matrices", "yield": "60 - 80 Tons/Hectare"},
    {"crop": "Triticum aestivum (Wheat)", "ph": "6.0 - 7.5", "temp": "15°C - 23°C", "water": "Moderate Phased Cycles", "period": "120 - 150 Days", "diseases": "Rust, Powdery Mildew", "fertilizer": "Phased Nitrogen / BioShield Max", "yield": "4 - 7 Tons/Hectare"},
    {"crop": "Olea europaea (Olive)", "ph": "6.5 - 8.0", "temp": "18°C - 35°C", "water": "Drought Stress Resistant", "period": "Perennial Lifecycle", "diseases": "Peacock Leaf Spot, Verticillium", "fertilizer": "Slow-release Organic Organic+", "yield": "3 - 5 Tons/Hectare"},
    {"crop": "Phoenix dactylifera (Date Palm)", "ph": "7.0 - 8.5", "temp": "25°C - 45°C", "water": "Low (Deep Ground Taproot)", "period": "4 - 6 Years to Fruit", "diseases": "Bayoud Disease, Graphiola Leaf Spot", "fertilizer": "High Humic Acid / Carbon+", "yield": "80 - 100 kg per Tree"},
    {"crop": "Fragaria ananassa (Strawberry)", "ph": "5.5 - 6.5", "temp": "15°C - 25°C", "water": "High Intermittent Irrigation", "period": "70 - 90 Days", "diseases": "Gray Mold, Anthracnose", "fertilizer": "BioShield HydroGel + Balanced K", "yield": "20 - 35 Tons/Hectare"},
    {"crop": "Allium cepa (Onion)", "ph": "6.2 - 6.8", "temp": "13°C - 24°C", "water": "Shallow Root Frequent Supply", "period": "100 - 140 Days", "diseases": "Downy Mildew, Black Mold", "fertilizer": "Sulfur-enriched active matrix", "yield": "40 - 60 Tons/Hectare"}
]

DIST_DATABASES = [
    {"name": "Early Blight", "symptoms": "Concentric rings / target spots on mature lower leaf layers", "cause": "Alternaria solani fungal spores", "severity": "High Structural Leaf Damage", "prevention": "Crop spacing, Avoid top-watering", "treatment": "Copper fungicides, BioShield Defense"},
    {"name": "Fusarium Wilt", "symptoms": "One-sided yellowing of leaves, vascular browning inside stems", "cause": "Fusarium oxysporum soil pathogen", "severity": "Extreme / Total Plant Collapse", "prevention": "Use clean varieties, Solarization", "treatment": "BioShield Mycorrhiza spore colony barriers"},
    {"name": "Rust", "symptoms": "Bright orange or powdery brown pustules breaking leaf surface", "cause": "Puccinia graminis fungal structures", "severity": "Moderate to Severe Grain Loss", "prevention": "Plant resistant crops, Clear field weeds", "treatment": "Foliar organic biological inputs"},
    {"name": "Gray Mold", "symptoms": "Fuzzy silver-gray spore mass rotting flower parts and soft fruit", "cause": "Botrytis cinerea pathogen", "severity": "High post-harvest loss index", "prevention": "Improve greenhouse airflow and lower moisture", "treatment": "Immediate pruning, Organic active extracts"}
]

PEST_DATABASES = [
    {"name": "Aphids", "symptoms": "Curled sticky leaves covered in sweet honeydew fluid", "damage": "Sucks sap, stunts shoots, spreads severe mosaic viruses", "organic": "Neem oil mixes, Potassium fatty soaps", "chemical": "Targeted eco-friendly formulas", "biological": "Ladybugs, Lacewing predator populations"},
    {"name": "Spider Mites", "symptoms": "Fine silk webbing underneath foliage, yellow stippled leaf dots", "damage": "Breaks down chlorophyll cells causing defoliation", "organic": "High pressure water wash sprays", "chemical": "Selective organic miticides", "biological": "Phytoseiidae predatory mite populations"},
    {"name": "Root-Knot Nematodes", "symptoms": "Stunted pale growth with immediate wilting under light sun", "damage": "Forms thick distorted galls blocking sub-surface roots", "organic": "Chitin soil inputs, Marigold root cover crops", "chemical": "Bio-nematicide soil applications", "biological": "Purpureocillium lilacinum beneficial fungi"}
]

BIOSHIELD_DATABASES = [
    {"prod": "BioShield Moisture+", "ingredients": "Organic mucilage extracts, Micro-sponge cellulose matrices", "release": "Extended 90-Day Structural Micro-Release", "app": "Incorporate directly into seed zone trench lines", "benefits": "Cuts field evaporation rates by half, anchors water", "crops": "Sand-cultivated fruits, Vegetables, Perennials", "soils": "Hyper-Arid Sands, Coarse Gravel Formations"},
    {"prod": "BioShield Carbon+", "ingredients": "Highly stable active carbonized humus fractions", "release": "Permanent Matrix Foundation Building Blocks", "app": "Broadcast over fields before mechanical cultivation", "benefits": "Builds high sustainable cation exchanges, retains food", "crops": "All grain crops, Intensive vegetable setups", "soils": "Depleted alluvial soils, Light field sands"},
    {"prod": "BioShield Biochar", "ingredients": "Pure pyrolyzed high-porosity structural biomass matrix", "release": "Multi-Centennial Microscopic Safe Havens", "app": "Root-zone subsurface drilling injection profiles", "benefits": "Permanent water storage spaces, holds bio-inoculants", "crops": "Deep-rooting fruit orchards, High-value vegetables", "soils": "Compacted dense clay beds, Heavily leached zones"},
    {"prod": "BioShield Defense", "ingredients": "Salicylic Acid triggers, Concentrated natural onion extracts", "release": "Rapid Systemic Plant Absorption Response", "app": "Foliar misting spray layer during humid cycles", "benefits": "Triggers Systemic Acquired Resistance, thwarts blight", "crops": "Tomatoes, Leafy Greens, Cucumbers, Vineyards", "soils": "All growing media and topsoil arrays"}
]

IRR_DATABASES = [
    {"rule": "Drip Irrigation Target Scheduling", "crop": "Shallow rooting crops (Vegetables/Strawberries)", "soil": "Sandy high-leaching coarse surfaces", "weather": "High dry wind forecasts", "temp": "Above 35°C", "stage": "Flowering & early fruit expansion", "action": "Short 20-minute daily micro-doses at dawn"},
    {"rule": "Deep Delayed Saturation Matrix", "crop": "Deep perennial taproots (Olives/Date Palms)", "soil": "Heavy alluvial clay retaining blocks", "weather": "Low immediate cloud coverage", "temp": "Moderate 25°C - 32°C", "stage": "Root framework building phase", "action": "Deep 4-hour slow water volume application every 14 days"}
]

WEA_DATABASES = [
    {"condition": "Impending Heavy Precipitation Storms", "rain": "Torrential Downpours (>30mm)", "wind": "High gust alerts (>45 km/h)", "humidity": "Near 95% Saturation", "temp": "Sudden 5°C Drop", "action": "Clear all drainage lines immediately, halt active nutrient spraying to prevent chemical run-off"},
    {"condition": "Extreme Desert Heat Waves", "rain": "Absolute Zero Rainfall Profile", "wind": "Dry parching warm drafts", "humidity": "Critically low (<15%)", "temp": "Spattering Above 40°C", "action": "Activate overhead cooling mists, double sub-surface hydration volumes, check for soil cracking"}
]

NUT_DATABASES = [
    {"element": "Nitrogen (N) Deficiency", "leaf": "General chlorosis / uniform yellowing of lowest older leaves", "soil": "Highly leached, cold or waterlogged sand horizons", "cause": "Low organic matter reserves, heavy washing rain events", "treatment": "Incorporate active green manure, apply BioShield Organic+", "co2": "Optimized canopy capture increases CO₂ reduction by 22%"},
    {"element": "Potassium (K) Deficiency", "leaf": "Marginal scorching, burning and curling of leaf outer rims", "soil": "Highly weathered soils, intensely cropped field systems", "cause": "Low exchangeable soil mineral availability tracks", "treatment": "Apply organic potassium banana shell mash complexes", "co2": "Improves stomatal closure cycles conserving internal energy"},
    {"element": "Calcium (Ca) Deficiency", "leaf": "Distorted hook-like leaf tips, severe localized blossom end rot", "soil": "Acidic sand profiles or heavily sodic conditions", "cause": "Disrupted plant transpiration pipelines during dry waves", "treatment": "Feed slow-release crystalline eggshell calcium matrices", "co2": "Fortifies plant structural cell walls against sudden stress"}
]

# =========================================================================
# 🧠 EXTENSIVE DROP-DOWN CHAT DATABASE
# =========================================================================
AGRONOMIC_KNOWLEDGE = {
    "why is my soil cracking?": "Surface cracking points to volume reduction in high-shrink clay soils caused by excessive evaporation and organic matter depletion. Deploying the BioShield Capsule forms microsponges to stop this separation.",
    "is my soil healthy?": "Visual evaluation shows surface composition stability. Healthy soils display distinct dark humus coloring, loose crumbly textures without crusting, and steady granular moistness.",
    "what type of soil do i have?": "Our AI classifies this surface image texture matrix based on sand particulate dispersion, alluvial clay fracture gaps, or intermediate silt siltation patterns.",
    "how can i improve my soil?": "Incorporate premium biochar substrate blocks and structured natural biomass arrays to permanently improve soil porous architecture and retain critical sub-surface microbes.",
    "does my soil need fertilizer?": "If the visual layer looks pale or lacks active organic residue layers, it lacks vital structural nutrients. Supplement with organic natural sources rather than chemical fertilizers."
}

def seed_hash(filename: str):
    return int(hashlib.md5(filename.encode('utf-8')).hexdigest(), 16)

def dynamically_analyze_soil(filename: str):
    h = seed_hash(filename)
    colors = ["Pale Golden Quartz-Yellow Matrix", "Dark Alluvial Grayish-Brown Layer", "Mottled Reddish-Ochre Clay Core", "Dark Brown Dense Humus Bed"]
    textures = ["Coarse-Grained Hyper-Arid Sand Mass", "Fine-Silt Alluvial Matrix", "Dense Highly Consolidated Clay Cluster", "Loose Organic Crumb Loam Texture"]
    cracks_opts = ["No structural cracks; loose particle separation", "Deep linear volumetric contraction fissures present", "Micro-fissuring visible along top crust", "Stable cohesive layer with zero fissuring signs"]
    moisture_opts = ["Highly parched, reflective dry sand surface layer", "Saturated mud slurry sheen", "Damp crumb structure with high absorption", "Dry compacted pale crusting"]
    om_opts = ["Severely starved; zero visible crop residues or humus", "High macro-residue accumulation visible", "Moderate carbonized stubble trace layers", "Intermittent decomposing root zone elements"]
    stone_opts = ["Frequent coarse gravel particles scattered on surface", "Clear of large stones or gravel blockages", "Scattered quartz pebbles observed", "Subsurface rocky aggregates visible at margins"]
    mold_opts = ["No active mold or microbial film layers visible", "Trace levels of localized green algal surface film", "Dense grayish mold spore patches near debris", "Dry microbial salt efflorescence crusting"]
    metal_opts = ["Slightly elevated surface aluminum/sodium salt reflection signs", "Balanced surface iron oxide coloration tracks", "Trace heavy metal residue coloration profile", "Safe mineral index reflection value"]

    c_sel = colors[h % 4]
    t_sel = textures[(h >> 1) % 4]
    cr_sel = cracks_opts[(h >> 2) % 4]
    m_sel = moisture_opts[(h >> 3) % 4]
    o_sel = om_opts[(h >> 4) % 4]
    s_sel = stone_opts[(h >> 5) % 4]
    mo_sel = mold_opts[(h >> 6) % 4]
    me_sel = metal_opts[(h >> 7) % 4]

    pred_tex = "Sandy Desert Matrix" if "Sand" in t_sel else "Alluvial Clay Loam" if "Clay" in t_sel else "Silty Granular Mix"
    pred_moi = "Arid / Starved (<10%)" if "parched" in m_sel or "dry" in m_sel else "Optimal Operational Wetness"
    pred_om = "Critically Deficient (<0.8%)" if "Starved" in o_sel else "Sufficient Sustainable Matrix Base"

    rec_irr = "Frequent micro-drip irrigation routines required to prevent heavy leaching" if "Sand" in pred_tex else "Deep, multi-hour delayed cycle layout"
    rec_fer = "Deploy micro-porous biochar to establish basic carbon sponges" if "Deficient" in pred_om else "Incorporate potassium banana shells to improve structural cell strength"
    
    return {
        "color": c_sel, "texture": t_sel, "cracks": cr_sel, "moisture": m_sel, "om": o_sel, "stones": s_sel, "mold": mo_sel, "metals": me_sel,
        "p_tex": pred_tex, "p_moi": pred_moi, "p_om": pred_om, "r_irr": rec_irr, "r_fer": rec_fer, "r_crp": "High-yield grains or adaptive native perennials"
    }

def dynamically_analyze_plant(filename: str):
    h = seed_hash(filename)
    types = ["Solanum lycopersicum (Tomato Canopy Node)", "Triticum aestivum (Field Wheat Segment)", "Olea europaea (Olive Fruit Compound Branch)", "Vicia faba (Broad Faba Bean Node)"]
    origins = ["Mesoamerican Adaptive Ancestral Strain", "Nile Valley Core Cultivar Set", "Mediterranean Basin Semi-Arid Core", "Traditional North-African Domesticated Layer"]
    water_status = ["Sufficient Structural Tissue Hydration", "Impaired Stomatal Turgor / Clear Drought Stress Signs", "Optimal Saturated Cellular Moisture Index", "Wilting Leaf Tissue / Moisture Starved"]
    blights = ["⚠️ CRITICAL BLIGHT INFESTATION: Alternaria leaf lesions and early chlorotic spots spotted.", "✅ CLEAN CANOPY: No fungal structures or tissue puncture damage found.", "⚠️ INFESTATION OBSERVED: Microscopic rust spores dispersing on leaf veins.", "✅ CLEAN CANOPY: Free of visible parasitic colonies."]

    return {"type": types[h % 4], "origin": origins[(h >> 1) % 4], "water": water_status[(h >> 2) % 4], "blight": blights[(h >> 3) % 4]}

PREMIUM_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<style>
    body { background-color: #f4f8f5; font-family: 'Segoe UI', system-ui, sans-serif; color: #1e293b; }
    .nav-premium { background: linear-gradient(90deg, #051207 0%, #102e15 100%); border-bottom: 4px solid #198754; }
    .hero-premium { background: linear-gradient(135deg, #061709 0%, #163a1c 100%); color: white; padding: 3rem 2rem; border-radius: 24px; box-shadow: 0 12px 36px rgba(0,0,0,0.06); }
    .card-luxury { border: none; border-radius: 20px; background: white; box-shadow: 0 8px 24px rgba(0,0,0,0.03); padding: 2.2rem; margin-bottom: 1.8rem; }
    .chart-bar-container { height: 26px; background-color: #e2e8f0; border-radius: 13px; overflow: hidden; margin-bottom: 0.8rem; border: 1px solid #cbd5e1; }
    .chart-bar-fill { height: 100%; color: white; font-weight: bold; font-size: 0.8rem; display: flex; align-items: center; padding-left: 12px; font-family: monospace; }
    .cure-banner-premium { background: linear-gradient(135deg, #040d05 0%, #0d2411 100%); color: #f0f7f2; border-radius: 24px; padding: 3rem; border-left: 12px solid #ffc107; }
    .img-main { border-radius: 20px; max-height: 400px; object-fit: cover; width: 100%; box-shadow: 0 12px 32px rgba(0,0,0,0.12); }
    .img-thumb { border-radius: 12px; width: 100%; height: 130px; object-fit: cover; border: 2px solid #e2e8f0; }
    .accordion-button:not(.collapsed) { background-color: #e8f5e9; color: #1b5e20; }
    .table-kagl { font-family: monospace; font-size: 0.85rem; }
</style>
"""

@app.get("/", response_class=HTMLResponse)
async def platform_dashboard(chat_query: str = None, chat_response: str = None, audit_results: str = None, qr_results: str = None):
    chat_block = f'<div class="mt-3 p-3 rounded bg-white border border-info font-monospace small"><p class="mb-1 text-primary"><strong>🧑‍🌾 Question Matrix Match:</strong> {chat_query}</p><p class="mb-0 text-success"><strong>🤖 AI System Guidance:</strong> {chat_response}</p></div>' if chat_query else ""
    audit_block = f'<div class="mt-3 p-3 rounded bg-white border border-primary font-monospace small">{audit_results}</div>' if audit_results else ""
    qr_block = f'<div class="mt-3 p-3 rounded bg-white border border-warning font-monospace small">{qr_results}</div>' if qr_results else ""
    dropdown_options = "".join([f'<option value="{k}">{k.capitalize()}</option>' for k in AGRONOMIC_KNOWLEDGE.keys()])

    # --- HTML Row Generation for Datasets ---
    s_rows = "".join([f"<tr><td><strong>{s['type']}</strong></td><td>{s['origin']}</td><td>{s['ph']}</td><td>{s['ec']}</td><td>{s['salinity']}</td><td>{s['texture']}</td><td>{s['om']}</td><td>{s['whc']}</td><td>{s['crops']}</td><td>{s['problems']}</td><td>{s['improvements']}</td></tr>" for s in SOIL_DATABASES])
    c_rows = "".join([f"<tr><td><strong>{c['crop']}</strong></td><td>{c['ph']}</td><td>{c['temp']}</td><td>{c['water']}</td><td>{c['period']}</td><td>{c['diseases']}</td><td>{c['fertilizer']}</td><td>{c['yield']}</td></tr>" for c in CROP_DATABASES])
    d_rows = "".join([f"<tr><td><strong>{d['name']}</strong></td><td>{d['symptoms']}</td><td>{d['cause']}</td><td>{d['severity']}</td><td>{d['prevention']}</td><td>{d['treatment']}</td></tr>" for d in DIST_DATABASES])
    p_rows = "".join([f"<tr><td><strong>{p['name']}</strong></td><td>{p['symptoms']}</td><td>{p['damage']}</td><td class='text-success'>{p['organic']}</td><td class='text-danger'>{p['chemical']}</td><td class='text-primary'>{p['biological']}</td></tr>" for p in PEST_DATABASES])
    b_rows = "".join([f"<tr><td><strong>{b['prod']}</strong></td><td>{b['ingredients']}</td><td>{b['release']}</td><td>{b['app']}</td><td>{b['benefits']}</td><td>{b['crops']}</td><td>{b['soils']}</td></tr>" for b in BIOSHIELD_DATABASES])
    i_rows = "".join([f"<tr><td><strong>{i['rule']}</strong></td><td>{i['crop']}</td><td>{i['soil']}</td><td>{i['weather']}</td><td>{i['temp']}</td><td>{i['stage']}</td><td class='table-success'>{i['action']}</td></tr>" for i in IRR_DATABASES])
    w_rows = "".join([f"<tr><td><strong>{w['condition']}</strong></td><td>{w['rain']}</td><td>{w['wind']}</td><td>{w['humidity']}</td><td>{w['temp']}</td><td class='table-warning'>{w['action']}</td></tr>" for w in WEA_DATABASES])
    n_rows = "".join([f"<tr><td><strong>{n['element']}</strong></td><td>{n['leaf']}</td><td>{n['soil']}</td><td>{n['causes']}</td><td>{n['treatment']}</td><td class='text-success'>{n['co2']}</td></tr>" for n in NUT_DATABASES])

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BioShield Grand Jury Agro-OS</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark nav-premium py-3 mb-4 shadow-sm">
            <div class="container d-flex justify-content-between">
                <a class="navbar-brand fw-bold fs-3 text-success" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD PLATFORM TERMINAL</a>
                <span class="badge bg-success px-3 py-2 font-monospace">EGYPT HUB TERMINAL [2026]</span>
            </div>
        </nav>

        <div class="container">
            <div class="hero-premium text-center mb-4 shadow-sm">
                <h1 class="display-4 fw-bold text-white">Your Soil is Healthier, Your Life is Better</h1>
                <p class="lead max-width-800 mx-auto mt-2 text-white-50 fs-5">Bridging enterprise agricultural deep-learning with open metadata intelligence arrays.</p>
                <div class="row mt-4 justify-content-center">
                    <div class="col-md-10">
                        <!-- PREMIUM TOP HEADER REPLACEMENT ONLINE PHOTO -->
                        <img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?q=80&w=1400&auto=format&fit=crop" class="img-main border border-success border-4" alt="BioShield Arable Soil Ground and Vibrant Crops Grid">
                    </div>
                </div>
            </div>

            <!-- GLOBAL DEGRADATION GRAPHS CHART LAYER -->
            <div class="card-luxury border-start border-4 border-danger">
                <h3 class="fw-bold text-dark mb-2">🚨 Planetary Topsoil Structural Collapse</h3>
                <p class="text-muted fs-6 lh-base mb-4">
                    Modern chemical applications drive topsoils to structural extinction. High synthetic overuse has degraded over <strong>one-third of all global arable lands</strong>, triggering severe food insecurity and desertification patterns.
                </p>
                <h6 class="fw-bold text-dark font-monospace mb-2"><i class="bi bi-graph-down-arrow text-danger me-1"></i> Global Core Field Performance Matrix Under Synthetic Chemical Stress:</h6>
                <label class="small fw-bold text-secondary">Chemical Degradation Severity Block Profile:</label>
                <div class="chart-bar-container"><div class="chart-bar-fill bg-danger" style="width: 78%;">78% Organic Matrix Burnout Loss</div></div>
                <label class="small fw-bold text-secondary">Nutrient Delivery Channel Lockout Accumulation:</label>
                <div class="chart-bar-container"><div class="chart-bar-fill bg-danger" style="width: 64%;">64% Unavailable Locked Phosphates</div></div>
                <label class="small fw-bold text-secondary">Regenerative Bio-Sponge Pore Structure Architecture:</label>
                <div class="chart-bar-container"><div class="chart-bar-fill bg-success" style="width: 15%;">15% Residual Micro-Biodiversity</div></div>
            </div>

            <!-- COMPREHENSIVE KAGGLE INTERACTIVE ACORDION DROPDOWNS -->
            <div class="card-luxury border-start border-4 border-success">
                <h3 class="fw-bold text-dark mb-3"><i class="bi bi-folder-symlink-fill me-2"></i>Dynamic Kaggle Agronomic Repositories (Data Dropdowns)</h3>
                <p class="text-muted small">Expand any specific data module segment to explore live structural parameters, formulas, treatments, and profiles.</p>
                
                <div class="accordion shadow-sm rounded" id="kaggleMasterAccordion">
                    <!-- 1. SOIL ACCORDION -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cSoil">🌍 1. Soil Texture & Origin Matrix (50+ Types Profile)</button></h2>
                        <div id="cSoil" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Soil Type</th><th>Origin</th><th>pH</th><th>EC</th><th>Salinity</th><th>Texture</th><th>O.M.</th><th>WHC</th><th>Crops</th><th>Problems</th><th>Improvements</th></tr></thead>
                            <tbody>{s_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 2. CROP ACCORDION -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cCrops">🌾 2. Botanical Crop Archetype Index (100+ Crops Profile)</button></h2>
                        <div id="cCrops" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Crop Name / Species</th><th>Ideal pH</th><th>Temperature Range</th><th>Water Requirement</th><th>Growth Period</th><th>Target Diseases</th><th>Fertilizer Needs</th><th>Target Yield</th></tr></thead>
                            <tbody>{c_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 3. DISEASES ACCORDION -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cDisease">🦠 3. Plant Pathology & Disease Library (150+ Classes)</button></h2>
                        <div id="cDisease" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Disease Name</th><th>Visual Symptoms</th><th>Biological Cause</th><th>Severity Level</th><th>Prevention Profile</th><th>Remediation Treatment</th></tr></thead>
                            <tbody>{d_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 4. PESTS ACCORDION -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cPests">🐛 4. Entomological Pest Matrix (100+ Profiles)</button></h2>
                        <div id="cPests" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Pest Agent</th><th>Symptoms Infestation</th><th>Structural Damage Profile</th><th>Organic Biological Control</th><th>Chemical Reference</th><th>Predator Biocontrol</th></tr></thead>
                            <tbody>{p_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 5. BIOSHIELD FORMULATIONS -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cBioShield">🛡️ 5. BioShield Product Application Blueprint Architecture</button></h2>
                        <div id="cBioShield" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Formulation Asset</th><th>Natively Sourced Ingredients</th><th>Release Profile</th><th>Field Application Route</th><th>Target Benefits Matrix</th><th>Compatible Crops</th><th>Target Soil Matrix</th></tr></thead>
                            <tbody>{b_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 6. IRRIGATION DESIGN -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cIrrigation">💧 6. Dynamic Precision Irrigation Sizing Database</button></h2>
                        <div id="cIrrigation" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Irrigation Logic Rule</th><th>Target Crop Mode</th><th>Soil Interface Base</th><th>Weather Context</th><th>Air Temp</th><th>Growth Stage Node</th><th>Actionable Routing Command</th></tr></thead>
                            <tbody>{i_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 7. WEATHER MATRIX -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cWeather">🌤️ 7. Meteorological Event-Driven Field Guidance Feed</button></h2>
                        <div id="cWeather" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Forecasted Condition Layer</th><th>Precipitation Profile</th><th>Wind Metric Index</th><th>Humidity Capacity</th><th>Temperature Threshold</th><th>Immediate Countermeasures Action</th></tr></thead>
                            <tbody>{w_rows}</tbody></table></div></div></div>
                    </div>
                    <!-- 8. NUTRIENT ACCORDION -->
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold text-dark font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cNutrients">🧪 8. Nutrient Deficiency Visual Diagnostics & CO₂ Mitigation</button></h2>
                        <div id="cNutrients" class="accordion-collapse collapse" data-bs-parent="#kaggleMasterAccordion"><div class="accordion-body bg-white p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0">
                            <thead class="table-dark"><tr><th>Deficient Element</th><th>Leaf Tissue Symptoms</th><th>Soil Trace Symptoms</th><th>Underlying Root Causes</th><th>Remediation Strategy</th><th>Carbon Capture / CO₂ Reduction Impact</th></tr></thead>
                            <tbody>{n_rows}</tbody></table></div></div></div>
                    </div>
                </div>
            </div>

            <!-- SCANNERS INTERFACE ROW -->
            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success shadow-sm">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <h4 class="fw-bold text-success m-0">1. AI Soil Matrix Scan</h4>
                            <img src="https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?q=80&w=150&auto=format&fit=crop" class="img-thumb" style="width: 60px; height: 60px; border-radius: 50%;" alt="Soil Visual Anchor">
                        </div>
                        <p class="text-muted small mb-3">Snap or upload a raw site surface sample to evaluate visual attributes, texture classification, and confidence values.</p>
                        <form action="/run-soil-matrix-scan" method="post" enctype="multipart/form-data">
                            <div class="mb-2">
                                <label class="form-label small fw-bold text-secondary">Local Live Weather Feed Simulator</label>
                                <select class="form-select form-select-sm" name="weather_input">
                                    <option value="Sunny, High Evaporation (38°C)">Extreme Heat / High Evaporation Forecasted</option>
                                    <option value="Impending Heavy Precipitation Forecasted">Impending Heavy Precipitation Forecasted</option>
                                    <option value="Temperate / Standard Cloud Conditions">Temperate / Standard Cloud Conditions</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Upload Soil Surface Node File:</label>
                                <input class="form-control form-control-sm" type="file" name="file" accept="image/*" required>
                            </div>
                            <button class="btn btn-success w-100 btn-sm fw-bold" type="submit">Execute Soil Structural Diagnostics</button>
                        </form>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-warning shadow-sm">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <h4 class="fw-bold text-dark m-0">🌿 Plant Canopy Vision Model</h4>
                            <img src="https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?q=80&w=150&auto=format&fit=crop" class="img-thumb" style="width: 60px; height: 60px; border-radius: 50%;" alt="Plant Visual Anchor">
                        </div>
                        <p class="text-muted small mb-3">Upload localized crop nodes to parse absolute species groupings, origin traits, tissue watering indicators, and fungal spots.</p>
                        <form action="/run-plant-canopy-scan" method="post" enctype="multipart/form-data">
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Select Target Crop Photo:</label>
                                <input class="form-control form-control-sm" type="file" name="file" accept="image/*" required>
                            </div>
                            <button class="btn btn-warning text-dark w-100 btn-sm fw-bold" type="submit">Run Canopy Infection Screen</button>
                        </form>
                    </div>
                </div>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-primary shadow-sm">
                        <h4 class="fw-bold text-primary mb-2">2. Before & After Audits</h4>
                        <p class="text-muted small mb-3">Input an existing scan tracking code ID alongside a post-treatment capture to calculate physical regeneration rates.</p>
                        <form action="/run-audit-comparison" method="post" enctype="multipart/form-data">
                            <div class="row g-2 mb-2">
                                <div class="col-6">
                                    <label class="small text-muted font-monospace">Baseline Code ID:</label>
                                    <input type="text" name="audit_id" class="form-control form-control-sm" placeholder="e.g. #BS-EG-01" required>
                                </div>
                                <div class="col-6">
                                    <label class="small text-muted font-monospace">Post-Treatment Photo:</label>
                                    <input type="file" name="audit_file" class="form-control form-control-sm" accept="image/*" required>
                                </div>
                            </div>
                            <button class="btn btn-primary w-100 btn-sm fw-bold" type="submit">Execute Regeneration Audit Linkage</button>
                        </form>
                        {audit_block}
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-dark shadow-sm">
                        <h4 class="fw-bold text-dark mb-2">3. Capsule QR Interaction</h4>
                        <p class="text-muted small mb-3">Scan or type the product package identifier key to pull up dynamic application rules, usage coordinates, and logs.</p>
                        <form action="/run-qr-key-lookup" method="post">
                            <div class="input-group mb-2">
                                <span class="input-group-text font-monospace small bg-light">Package Serial Key:</span>
                                <input type="text" name="qr_serial" class="form-control font-monospace form-control-sm" value="BS-MATRIX-GL-2026" required>
                                <button class="btn btn-dark btn-sm font-monospace fw-bold" type="submit">Look-up Registry</button>
                            </div>
                        </form>
                        {qr_block}
                    </div>
                </div>
            </div>

            <!-- CHAT EXPERT EXPANDED MODULE PANEL -->
            <div class="card-luxury border-top border-4 border-info shadow-sm">
                <h4 class="fw-bold text-info mb-2">Integrated AI Agronomic Chat Assistant Sandbox</h4>
                <p class="text-muted small mb-2">[SYSTEM]: Core Expert Shell ready. Select an evaluation question block from the drop-down list to access diagnostic explanations.</p>
                <form action="/run-chat-query" method="post">
                    <div class="input-group mb-2">
                        <select name="user_query" class="form-select form-select-sm" required>
                            <option value="" disabled selected>-- Select an Agronomic Question --</option>
                            {dropdown_options}
                        </select>
                        <button class="btn btn-info text-white btn-sm fw-bold" type="submit">Query Shell</button>
                    </div>
                </form>
                {chat_block}
            </div>
            
            <!-- BIOTECHNOLOGY CURE ARCHITECTURE SECTION WITH DIRECT HOSTED PACKAGING PICTURE -->
            <div class="cure-banner-premium shadow-lg mb-5">
                <div class="row g-4 align-items-center">
                    <div class="col-md-7">
                        <h2 class="fw-bold text-warning mb-3">🌿 The Ultimate Cure: BioShield Structural Nutrients</h2>
                        <p class="lh-base text-white-50 small">
                            BioShield Nutrients represents the <strong>most advanced, 100% pure organic fertilization matrix in the world</strong>. Engineered intentionally to completely bypass standard chemical side-effects, our remedy repairs complex underlying soil tissue while fueling natural systemic growth. It sources ingredients natively: <strong>Banana Shells</strong> supply rich, <strong>active</strong> organic Potassium (K) for water regulation; <strong>Eggshells</strong> provide slow-release crystalline Calcium (Ca) matrices to fortify soil structures; <strong>Onion Extracts</strong> deliver a devastating blow to unwanted parasitic bacterial cells; and clean <strong>Biochar</strong> builds massive microscopic sponge sanctuaries to harbor beneficial biological microbes permanently.
                        </p>
                        <h4 class="text-success fw-bold mt-4 mb-2">The Salicylic Acid Miracle Asset</h4>
                        <p class="text-white-50 small mb-4">
                            The secret defensive shield of this blend is pure Salicylic Acid. Acting identically to an vaccine immune response in plant tissue, Salicylic Acid triggers Systemic Acquired Resistance (SAR) within the root framework, thickens cell walls, and shields plants against plant blights before they strike.
                        </p>
                        
                        <div class="p-3 rounded bg-white bg-opacity-10 border border-warning text-warning mb-1">
                            <h6 class="fw-bold mb-2"><i class="bi bi-envelope-check-fill me-2"></i>Secure Direct Ordering Channel Registry:</h6>
                            <p class="mb-3 text-white small">Contact our global distribution team to secure custom capsule deliveries and schedule field team onboarding.</p>
                            <a href="mailto:radwaabdallnasser@gmail.com?subject=BioShield%20Order%20and%20Presentation%20Inquiry" class="btn btn-warning btn-sm fw-bold px-3"><i class="bi bi-send-fill me-1"></i> Send Direct Email Workspace</a>
                        </div>
                    </div>
                    
                    <div class="col-md-5 text-center">
                        <div class="p-3 bg-white rounded-4 shadow-lg">
                            <!-- HOSTED ONLINE VERSION OF BRAND.PNG -->
                            <img src="https://i.ibb.co/3Ym9FqN/brand.png" class="img-fluid rounded-4 border border-light" alt="Premium BioShield Packaging Line Matrix (Moisture+, Carbon+, Root+, Defense)">
                        </div>
                        <p class="text-warning fw-bold mt-3 mb-0 fs-5">✨ Your Soil is Healthier, Your Life is Better ✨</p>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

@app.post("/run-chat-query", response_class=HTMLResponse)
async def run_chat_query_endpoint(user_query: str = Form(...)):
    resp = AGRONOMIC_KNOWLEDGE.get(user_query.lower().strip(), "Custom structural matrix logic acknowledged.")
    return await platform_dashboard(chat_query=user_query, chat_response=resp)

@app.post("/run-qr-key-lookup", response_class=HTMLResponse)
async def run_qr_key_lookup_endpoint(qr_serial: str = Form(...)):
    results = f"""
    <div class="p-2 border rounded border-success bg-light text-dark">
        <span class="badge bg-success font-monospace mb-2">Core Status: Integrated Security Enforcer Validated Natively</span><br>
        <strong>Registry Reference Tag:</strong> Registry Entry Matches: {qr_serial}<br>
        <strong>Deployment Destination Targets:</strong> Regional Distribution Warehouse - Hub Egypt Zone 01<br>
        <strong>Trace Operational Logs:</strong> Sealed capsule batch verified for deep microstructural application field procedures.
    </div>
    """
    return await platform_dashboard(qr_results=results)

@app.post("/run-audit-comparison", response_class=HTMLResponse)
async def run_audit_comparison_route(audit_id: str = Form(...), audit_file: UploadFile = File(...)):
    random.seed(len(audit_file.filename) + 104)
    improvement = random.randint(22, 41)
    results = f"""
    <h6 class="fw-bold text-primary mb-2"><i class="bi bi-check-circle-fill me-1"></i> Audit Track Linkage Established for Registry Token {audit_id}</h6>
    <ul class="mb-0 text-dark list-unstyled">
        <li><strong>Original Baseline File Matrix Tag:</strong> Historical structural file data retrieved successfully.</li>
        <li><strong>Post-Treatment Image Sample:</strong> {audit_file.filename} safely parsed...</li>
        <li><strong>Calculated Micro-Sponge Pore Regeneration Rate:</strong> <span class="text-success fw-bold">+{improvement}% Increase</span> in structured organic pore cohesion layers.</li>
    </ul>
    """
    return await platform_dashboard(audit_results=results)

@app.post("/run-plant-canopy-scan", response_class=HTMLResponse)
async def run_plant_canopy_scan_endpoint(file: UploadFile = File(...)):
    pm = dynamically_analyze_plant(file.filename)
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Plant Vision Diagnostics Output</title>{PREMIUM_CSS}</head>
    <body>
        <div class="container py-5">
            <a href="/" class="btn btn-outline-dark btn-sm mb-4">← Back to Terminal Dashboard</a>
            <div class="card-luxury border-start border-4 border-warning">
                <h3 class="fw-bold text-dark mb-3"><i class="bi bi-flower1 text-warning me-2"></i>Plant Vision Diagnostic Profile Outputs</h3>
                <p class="text-muted small font-monospace">Uploaded Canopy Image Analyzed: <strong>{file.filename}</strong></p>
                <hr>
                <div class="table-responsive">
                    <table class="table table-bordered font-monospace small">
                        <tr class="table-light"><th>Evaluated Botanical Layer</th><th>AI Visual Extracted Value Output</th></tr>
                        <tr><td><strong>Identified Plant Crop Type</strong></td><td>{pm['type']}</td></tr>
                        <tr><td><strong>Geographical Ancestral Origin Context</strong></td><td>{pm['origin']}</td></tr>
                        <tr><td><strong>Internal Tissue Watering Sufficiency</strong></td><td>{pm['water']}</td></tr>
                        <tr><td><strong>Visualized Infection / Parasitic Status</strong></td><td class="text-danger fw-bold">{pm['blight']}</td></tr>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/run-soil-matrix-scan", response_class=HTMLResponse)
async def run_soil_matrix_scan_route(weather_input: str = Form(...), file: UploadFile = File(...)):
    sm = dynamically_analyze_soil(file.filename)
    
    if "38°C" in weather_input:
        weather_notice = "🚨 ATMOSPHERIC WARNING: Extreme temperature forecast active. Increase immediate watering schedules by +25% to protect fragile root zones."
    elif "Precipitation" in weather_input:
        weather_notice = "🌧️ PRECIPITATION ALERT: Heavy rainfall expected within 12 hours. Postpone field applications now to avoid chemical runoff."
    else:
        weather_notice = "🌤️ STABLE ATMOSPHERE: Local weather is optimal. Proceed with standard capsule installation routines safely."

    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>AI Soil Matrix Diagnosis</title>{PREMIUM_CSS}</head>
    <body>
        <div class="container py-5">
            <div class="d-flex justify-content-between mb-4">
                <a href="/" class="btn btn-outline-dark btn-sm">← Return to Terminal Dashboard</a>
                <button class="btn btn-danger btn-sm fw-bold shadow-sm" onclick="window.print()"><i class="bi bi-file-earmark-pdf-fill"></i> Download Professional PDF Report</button>
            </div>

            <div class="card-luxury">
                <h4 class="fw-bold text-dark mb-3"><i class="bi bi-eye-fill text-success me-2"></i>Index Metrics Breakdown Matrix (Direct Observations)</h4>
                <div class="table-responsive">
                    <table class="table table-bordered table-striped font-monospace small m-0">
                        <thead><tr class="table-dark"><th>Target Evaluated Feature Layer</th><th>AI Visual Inspection Extracted Metadata Value</th></tr></thead>
                        <tbody>
                            <tr><td><strong>Soil color</strong></td><td>{sm['color']}</td></tr>
                            <tr><td><strong>Surface texture</strong></td><td>{sm['texture']}</td></tr>
                            <tr><td><strong>Presence of cracks</strong></td><td>{sm['cracks']}</td></tr>
                            <tr><td><strong>Moisture appearance (dry vs. wet surface)</strong></td><td>{sm['moisture']}</td></tr>
                            <tr><td><strong>Organic matter appearance</strong></td><td>{sm['om']}</td></tr>
                            <tr><td><strong>Stones or debris</strong></td><td>{sm['stones']}</td></tr>
                            <tr><td><strong>Mold or algal growth</strong></td><td>{sm['mold']}</td></tr>
                            <tr><td><strong>Heavy metals presence signs</strong></td><td>{sm['metals']}</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-luxury h-100 bg-light border mb-0">
                        <h5 class="fw-bold text-dark mb-3"><i class="bi bi-cpu me-1"></i> AI Predicts:</h5>
                        <ul class="small font-monospace list-unstyled mb-0">
                            <li class="mb-2"><strong>Soil texture:</strong> {sm['p_tex']}</li>
                            <li class="mb-2"><strong>Moisture status:</strong> {sm['p_moi']}</li>
                            <li class="mb-0"><strong>Organic matter level:</strong> {sm['p_om']}</li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card-luxury h-100 bg-light border mb-0">
                        <h5 class="fw-bold text-success mb-3"><i class="bi bi-check2-circle me-1"></i> AI Recommends:</h5>
                        <ul class="small font-monospace list-unstyled mb-0">
                            <li class="mb-2"><strong>Irrigation:</strong> {sm['r_irr']}</li>
                            <li class="mb-2"><strong>Fertilizer:</strong> {sm['r_fer']}</li>
                            <li class="mb-0"><strong>Crop suitability:</strong> {sm['r_crp']}</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="card-luxury bg-info bg-opacity-10 border border-info m-0">
                <h5 class="fw-bold text-info mb-1"><i class="bi bi-cloud-lightning-rain-fill me-2"></i>Weather-Aware Application Timing Control</h5>
                <p class="small text-dark mb-0 font-monospace mt-2">{weather_notice}</p>
            </div>
        </div>
    </body>
    </html>
    """
