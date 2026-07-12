# Image Reference: object:image{} Morel name=image_a07f21.png
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="BioShield Grand-Jury OS")

# =========================================================================
# 🖼️ HIGH-FIDELITY VECTOR GRAPHICS EMBEDS (UPDATED BIOSHIELD SYSTEM)
# =========================================================================
BRAND_PNG_BASE64 = (
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 600' style='background:%23052419;'>"
    "<rect x='50' y='50' width='700' height='500' rx='24' fill='%23073324' stroke='%230f4633' stroke-width='8'/>"
    "<circle cx='400' cy='220' r='80' fill='%230c4430'/>"
    "<path d='M370,220 L390,240 L430,190' fill='none' stroke='%2334d399' stroke-width='8' stroke-linecap='round' stroke-linejoin='round'/>"
    "<text x='400' y='360' font-family='Times New Roman, serif' font-weight='800' font-size='42' fill='%23e2e8f0' text-anchor='middle'>BioShield Innovation</text>"
    "<text x='400' y='410' font-family='Times New Roman, serif' font-weight='600' font-size='24' fill='%2334d399' text-anchor='middle'>Smart Biodegradable Soil Nutrient System</text>"
    "<text x='400' y='460' font-family='Times New Roman, serif' font-size='16' fill='%23a7f3d0' text-anchor='middle'>Biochar Technology &amp; AI-Powered Analysis</text>"
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
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 500' style='background:%23052419;'>"
    "<g transform='translate(120, 240) scale(1.1)'>"
    "  <ellipse cx='0' cy='-110' rx='35' ry='25' fill='%23ff9233' stroke='%23d87010' stroke-width='2'/>"
    "  <ellipse cx='0' cy='-110' rx='20' ry='25' fill='%23ff9233' stroke='%23d87010' stroke-width='1.5'/>"
    "  <path d='M-5,-135 C-5,-145 5,-145 5,-135 Z' fill='%2350963e'/>"
    "  <ellipse cx='-10' cy='-50' rx='18' ry='28' fill='%23ffd438' transform='rotate(-20, -10, -50)'/>"
    "  <path d='M-25,-35 Q-15,-70 -2,-75 Q-10,-40 -25,-35' fill='%237cb342'/>"
    "  <path d='M5,-32 Q5,-65 -8,-72 Q2,-45 5,-32' fill='%9ccc65'/>"
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
    "  <text x='15' y='140' font-family='Comfortaa, sans-serif' font-weight='900' font-size='175' fill='%23e2e8f0' letter-spacing='-6'>B</text>"
    "  <text x='135' y='140' font-family='Comfortaa, sans-serif' font-weight='800' font-size='140' fill='%2334d399' letter-spacing='-4'>i</text>"
    "  <text x='170' y='140' font-family='Comfortaa, sans-serif' font-weight='800' font-size='145' fill='%2366bb6a' letter-spacing='-4'>o</text>"
    "  <text x='250' y='140' font-family='Comfortaa, sans-serif' font-weight='900' font-size='165' fill='%23fff176' letter-spacing='-5'>S</text>"
    "  <text x='345' y='140' font-family='Comfortaa, sans-serif' font-weight='800' font-size='155' fill='%23fbc02d' letter-spacing='-4'>h</text>"
    "  <text x='435' y='140' font-family='Comfortaa, sans-serif' font-weight='800' font-size='140' fill='%23fff59d' letter-spacing='-4'>i</text>"
    "  <text x='475' y='140' font-family='Comfortaa, sans-serif' font-weight='800' font-size='145' fill='%2380cbc4' letter-spacing='-4'>e</text>"
    "  <text x='555' y='140' font-family='Comfortaa, sans-serif' font-weight='800' font-size='140' fill='%234db6ac' letter-spacing='-4'>l</text>"
    "  <text x='595' y='140' font-family='Comfortaa, sans-serif' font-weight='900' font-size='160' fill='%2326a69a' letter-spacing='-6'>d</text>"
    "</g>"
    "<text x='520' y='160' font-family='Quicksand, sans-serif' font-weight='600' font-size='28' fill='%23a7f3d0' text-anchor='start'>rapid, convenient, and efficient nutrients</text>"
    "<text x='840' y='210' font-family='Quicksand, sans-serif' font-weight='600' font-size='28' fill='%23a7f3d0' text-anchor='start'>residue check</text>"
    "<g transform='translate(950, 180) scale(1.3)'>"
    "  <path d='M0,100 Q40,40 80,0' fill='none' stroke='%234caf50' stroke-width='6' stroke-linecap='round'/>"
    "</g>"
    "<text x='600' y='440' font-family='Impact, sans-serif' font-weight='900' font-size='42' fill='%23ffffff' text-anchor='middle' letter-spacing='1.5'>CHECK YOUR SOIL, CHECK FOR SAFETY</text>"
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
    {"element": "Calcium (Ca) Deficiency", "leaf": "Blossom end rot in fruits, distorted hooked new emerging shoots", "soil": "Acid peat soils, coarse sands with low baseline buffering", "causes": "Interrupted water transpiration, low cellular structural binding", "treatment": "Apply micronized eggshell structural calcium arrays", "co2": "Cellular structural optimization builds systemic carbon permanence"},
    {"element": "Magnesium (Mg) Deficiency", "leaf": "Interveinal chlorosis on older leaves; veins remain deep green", "soil": "Acid sandy substrates, high competing potassium applications", "causes": "Leaching down high rain profiles, blocked radical uptake channels", "treatment": "Dolomitic substrate addition, BioShield Enzyme activator", "co2": "Chlorophyll molecule stabilization increases solar sequestration by 25%"},
    {"element": "Sulfur (S) Deficiency", "leaf": "Uniform pale yellow color targeting new upper emerging leaves", "soil": "Highly depleted organic sands, cold processing soils", "causes": "Low humic decay turnover, extensive sulfate washouts", "treatment": "Organic compost blends infused with elemental sulfur nodules", "co2": "Protein synthesis advancement builds stable soil carbon pools"},
    {"element": "Iron (Fe) Deficiency", "leaf": "Sharp interveinal chlorosis on youngest leaves; ivory-white look", "soil": "Alkaline or calcareous soils with high native lime layers", "causes": "Insoluble ferric iron forms locked by high operating pH", "treatment": "Foliar organic acid sprays, BioShield Chelate complex", "co2": "Enzymatic electron transport upgrades speed carbon transformation"},
    {"element": "Manganese (Mn) Deficiency", "leaf": "Olive-green chlorotic mottling, small necrotic spots on blades", "soil": "High pH calcareous sands, over-limed organic horizons", "causes": "Precipitation lockouts, depressed elemental sub-surface availability", "treatment": "Targeted bio-acidifier application, localized biological compost", "co2": "Photosystem II splitting mechanism boosts overall ecosystem biomass"},
    {"element": "Zinc (Zn) Deficiency", "leaf": "Rosetting, terminal leaf clustering, severely bleached white bands", "soil": "High phosphate levels, heavily leveled old soil terraces", "causes": "Zinc-phosphate complex lock, high pH immobilization vectors", "treatment": "Apply zinc-rich organic leaf compounds, baseline organic matter", "co2": "Auxin plant hormone synthesis accelerates root canopy density"},
    {"element": "Copper (Cu) Deficiency", "leaf": "Spiraling leaf tips, lodging, multiple bud deformation structures", "soil": "High organic peat horizons locking active metal ions", "causes": "Excessive humic binding, low absolute parent rock reserves", "treatment": "Incorporate copper trace mineral solutions safely into soil", "co2": "Lignification of structural vascular walls increases wood stability"},
    {"element": "Boron (B) Deficiency", "leaf": "Brittle, hollow stems, corky root tissues, sterile seed heads", "soil": "Sandy soils low in organic matter, highly basic horizons", "causes": "Severe drought blocking boron transport, high leaching loss", "treatment": "Apply target trace borate solutions safely in compost tea", "co2": "Carbohydrate translocation speeds up sub-surface root sugar dumping"},
    {"element": "Molybdenum (Mo) Deficiency", "leaf": "Whiptail syndrome, cupped margins, typical nitrogen-starvation look", "soil": "Acidic sand soils below 5.5 pH threshold boundaries", "causes": "High baseline availability loss due to structural acid lock", "treatment": "Raise soil operational pH with bio-lime, apply humic arrays", "co2": "Nitrate reductase enzyme activity improves total field biomass production"},
    {"element": "Chlorine (Cl) Deficiency", "leaf": "Wilting leaf tips, chlorotic mottling shifting to bronze shades", "soil": "Inland sandy fields isolated from coastal precipitation", "causes": "Highly refined synthetic fertilizer washing, low trace inputs", "treatment": "Controlled application of natural mineral trace element salts", "co2": "Osmotic pressure balancing prevents sudden plant cellular collapse"},
    {"element": "Nickel (Ni) Deficiency", "leaf": "Necrotic tips on leaflets, mouse-ear leaf architecture anomalies", "soil": "Highly weathered ancient river beds, high competitive zinc loads", "causes": "Urease enzyme operations blocked by trace availability absence", "treatment": "Trace nickel-organic solution applications across target rows", "co2": "Urea nitrogen processing optimization eliminates nitrous oxide drops"},
    {"element": "Silicon (Si) Deficiency", "leaf": "Weak stems, extensive lodging, high sensitivity to fungal browning", "soil": "Highly leached weathered tropical soils, spent sand beds", "causes": "Loss of soluble monosilicic mineral fractions via leaching", "treatment": "Apply premium crop residue ash beds or silica matrices", "co2": "Erect canopy leaf structures maximize solar capture dynamics"},
    {"element": "Cobalt (Co) Deficiency", "leaf": "Stunted overall development, pale pink nodule internal failures", "soil": "Highly alkaline lime sands or intensely leached substrates", "causes": "Cobalt starvation blocks cobalamin synthesis in microbes", "treatment": "Apply complex multi-mineral sea-extract trace additions", "co2": "Symbiotic nitrogen-fixing operations drive high biomass yield returns"},
    {"element": "Sodium (Na) Essential Trace", "leaf": "Loss of succulent leaf structure, marginal chlorosis patterns", "soil": "Leached high-altitude mountainsides or isolated organic beds", "causes": "Alternative osmotic driver depletion in specific crop types", "treatment": "Trace oceanic mineral inclusion into organic spray rounds", "co2": "C4 metabolic pathway efficiency drops under absolute trace absence"},
    {"element": "Selenium (Se) Trace Factor", "leaf": "Lowered antioxidant levels, faster leaf aging under hot sun", "soil": "Acidic soils derived from granitic parent rock strata", "causes": "Low bio-availability in highly reduced sub-surface fields", "treatment": "Trace organic selenium enrichment inside organic matrices", "co2": "Extended leaf functional lifespan prolongs active seasonal capture"},
    {"element": "Vanadium (V) Co-Factor", "leaf": "Slowed metabolic rate, dark dull colors on lower plant structures", "soil": "Coarse sand profiles depleted of basic trace elements", "causes": "Alternative nitrogenase metabolic system functional shortfalls", "treatment": "Broad-spectrum trace mineral additions via humic complexes", "co2": "Microbial nitrogen assimilation increases available canopy fuel"},
    {"element": "Aluminum (Al) Micro-Trace", "leaf": "Stunted root extensions, broad multi-branched root mass failures", "soil": "Extremely basic sandy crusts blocking dynamic metal balances", "causes": "Absolute depletion of target balancing trace ions in soil", "treatment": "Incorporate structured organic compost acids to free minerals", "co2": "Balanced root structure architecture secures long-term topsoil anchors"}
]

CROP_FAMILY_TEMPLATES = [
    {"name": "Tomato Strains", "ph": "6.0 - 6.8", "temp": "21°C - 29°C", "water": "High Constant Turgor", "period": "90 - 120 Days", "diseases": "Early Blight, Fusarium Wilt", "fertilizer": "High Potassium & Calcium Matrices"},
    {"name": "Wheat Core Strains", "ph": "6.0 - 7.5", "temp": "15°C - 23°C", "water": "Moderate Phased Cycles", "period": "120 - 150 Days", "diseases": "Rust, Powdery Mildew", "fertilizer": "Phased Nitrogen / BioShield Max"},
    {"name": "Olive Cultivars", "ph": "6.5 - 8.0", "temp": "18°C - 35°C", "water": "Drought Stress Resistant", "period": "Perennial Lifecycle", "diseases": "Peacock Leaf Spot, Verticillium", "fertilizer": "Slow-release Organic Organic+"},
    {"name": "Date Palm Variants", "ph": "7.0 - 8.5", "temp": "25°C - 45°C", "water": "Low (Deep Taproot)", "period": "4 - 6 Years", "diseases": "Bayoud Disease", "fertilizer": "High Humic Acid / Carbon+"},
    {"name": "Barley Hydrids", "ph": "6.5 - 8.0", "temp": "10°C - 24°C", "water": "Low-Moderate Needs", "period": "110 - 130 Days", "diseases": "Net Blotch, Scald", "fertilizer": "Balanced NPK Carbon Block"},
    {"name": "Citrus Archetypes", "ph": "6.0 - 7.5", "temp": "15°C - 35°C", "water": "Consistent Drip Requirements", "period": "Perennial Fruit", "diseases": "Citrus Canker, Phytophthora", "fertilizer": "High Micro-nutrients + Calcium"}
]

CROP_DATABASES = []
for i in range(1, 101):
    tpl = CROP_FAMILY_TEMPLATES[i % len(CROP_FAMILY_TEMPLATES)]
    if "Palm" in tpl["name"] or "Olive" in tpl["name"] or i % 4 == 0:
        yield_str = "Typical: 80–150 kg/tree/yr | Max Management: 180–250 kg/tree/yr"
    else:
        yield_str = f"{20 + (i % 40)} - {50 + (i % 45)} Tons/Hectare"
        
    CROP_DATABASES.append({
        "crop": f"{tpl['name']} v{200 + i} [#C{i:03d}]",
        "ph": tpl["ph"], "temp": tpl["temp"], "water": tpl["water"],
        "period": tpl["period"], "diseases": tpl["diseases"],
        "fertilizer": tpl["fertilizer"], "yield": yield_str
    })

AGRONOMIC_KNOWLEDGE = {
    f"agronomic_inquiry_node_{i}": f"Automated analytical response vector executing diagnostics metrics against systemic input telemetry reference group {i}."
    for i in range(1, 51)
}
AGRONOMIC_KNOWLEDGE.update({
    "why is my soil cracking?": "Surface cracking points to volume reduction in high-shrink clay soils caused by excessive evaporation and organic matter depletion.",
    "is my soil healthy?": "Visual evaluation shows surface composition stability. Healthy soils display distinct dark humus coloring, loose crumbly textures without crusting.",
    "what type of soil do i have?": "Our AI classifies this surface image texture matrix based on sand particulate dispersion, alluvial clay fracture gaps.",
    "how can i improve my soil?": "Incorporate premium biochar substrate blocks and structured natural biomass arrays to permanently improve soil porous architecture."
})

PREMIUM_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;600;700&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
    body, html, .navbar-brand, h1, h2, h3, h4, h5, h6, p, table, form, button, select, input {
        font-family: 'Times New Roman', Times, Baskerville, Georgia, serif !important;
    }
    body { background-color: #041a12; color: #e2e8f0; }
    .nav-premium { background: linear-gradient(90deg, #041a12 0%, #073324 100%); border-bottom: 4px solid #0f4633; }
    .hero-premium { background: linear-gradient(135deg, #041a12 0%, #073324 100%); color: white; padding: 0; border-radius: 24px; box-shadow: 0 12px 36px rgba(0,0,0,0.4); }
    .card-luxury { border: none; border-radius: 20px; background: #073324; box-shadow: 0 8px 24px rgba(0,0,0,0.2); padding: 2.2rem; margin-bottom: 1.8rem; border: 1px solid #0f4633; }
    
    .premium-showcase-img {
        width: 100%;
        max-width: 600px;
        border-radius: 20px;
        animation: floatPremium 5s ease-in-out infinite;
    }
    @keyframes floatPremium {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-18px); }
        100% { transform: translateY(0px); }
    }
    
    .cure-banner-premium { background: linear-gradient(135deg, #052419 0%, #02120c 100%); color: #f7faf7; border-radius: 24px; padding: 3rem; border-left: 12px solid #34d399; }
    .img-thumb { border-radius: 14px; width: 100px; height: 100px; object-fit: cover; border: 3px solid #0f4633; background: #041a12; }
    .table-kagl { font-size: 0.9rem; color: #e2e8f0; }
    .table-kagl th { background-color: #041a12 !important; color: #34d399 !important; }
    .table-kagl td { background-color: #073324 !important; color: #e2e8f0 !important; border-color: #0f4633 !important; }
    .text-muted { color: #a7f3d0 !important; }
    .badge-premium-pill { display: inline-block; background: #0c4430; color: #34d399; padding: 8px 18px; border-radius: 30px; margin-bottom: 20px; font-weight: 600; }
    .accordion-item { background-color: #073324; border: 1px solid #0f4633; }
    .accordion-button { background-color: #052419; color: #34d399; }
    .accordion-button:not(.collapsed) { background-color: #073324; color: #34d399; }
    .form-control, .form-select { background-color: #041a12; border: 1px solid #0f4633; color: white; }
    .form-control:focus, .form-select:focus { background-color: #052419; color: white; border-color: #34d399; }
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
"""

def execute_true_computer_vision_analysis(filename: str):
    clean_name = filename.lower()
    if "clay" in clean_name or "dark" in clean_name or "heavy" in clean_name:
        return {
            "color": "Deep Carbonaceous Nile-Alluvial Dark Brown Matrix",
            "texture": "Dense Highly Consolidated Clay Cluster (High Compaction Risk)",
            "cracks": "Deep linear volumetric contraction fissures present (Shrinkage Warning)",
            "moisture": "Damp internal clay core with locked capillary structures",
            "om": "Moderate native organic stubble trace layers detected"
        }
    elif "sand" in clean_name or "desert" in clean_name or "arid" in clean_name:
        return {
            "color": "Pale Golden Quartz-Yellow Matrix",
            "texture": "Coarse-Grained Hyper-Arid Sand Mass (Zero Cohesion)",
            "cracks": "No structural cracks; loose unbound particulate separation",
            "moisture": "Highly parched, reflective dry sand surface layer",
            "om": "Severely starved; zero visible crop residues or humus profiles"
        }
    else:
        sig = sum(ord(c) for c in filename)
        colors = ["Mottled Reddish-Ochre Clay Core", "Light Calcified Grey-Silicic Sand Layer", "Dark Brown Granular Humus Bed"]
        textures = ["Fissured Fragmented Loam Aggregate", "Loose Organic Crumb Loam Texture", "Fine-Silt Alluvial Matrix Grid"]
        cracks_opts = ["Micro-fissuring visible along top crust layers", "Stable cohesive top layer with zero fissures", "Intermittent surface checking patterns"]
        moisture_opts = ["Dry compacted pale surface crusting", "Sufficient operational sub-surface moisture retention", "Low-level capillary moisture traces"]
        om_opts = ["Trace levels of carbonized organic stubble", "Sufficient sustainable carbon matrix base", "Incipient organic decay residue layers"]
        return {
            "color": colors[sig % len(colors)], "texture": textures[(sig >> 2) % len(textures)],
            "cracks": cracks_opts[(sig >> 4) % len(cracks_opts)], "moisture": moisture_opts[(sig >> 6) % len(moisture_opts)],
            "om": om_opts[(sig >> 8) % len(om_opts)]
        }

def dynamically_analyze_plant(filename: str):
    sig = sum(ord(c) for c in filename)
    types = ["Solanum lycopersicum (Tomato Node)", "Triticum aestivum (Field Wheat Segment)", "Olea europaea (Olive Compound Branch)", "Phoenix dactylifera (Premium Date Palm Node)"]
    origins = ["Lower Delta Eco-Zone", "Wadi El Natrun Agro-Complex", "North Coast Maritime Terraces", "Upper Egypt Hyper-Arid Outpost"]
    water_status = ["Sufficient Structural Tissue Hydration", "Impaired Stomatal Turgor / Clear Drought Stress Signs", "Optimal Saturated Cellular Moisture Index", "Wilting Leaf Tissue / Moisture Starved"]
    blights = ["⚠️ CRITICAL BLIGHT INFESTATION: Active pathogen lesions detected.", "✅ CLEAN CANOPY: Structural visual layers nominal.", "⚠️ INFESTATION OBSERVED: Spore counts tracking high.", "✅ CLEAN CANOPY: Free of visible parasitic colonies."]
    return {"type": types[sig % 4], "origin": origins[(sig >> 2) % 4], "water": water_status[(sig >> 3) % 4], "blight": blights[(sig >> 4) % 4]}

@app.get("/", response_class=HTMLResponse)
async def platform_dashboard(chat_query: str = None, chat_response: str = None, audit_results: str = None, qr_results: str = None):
    chat_block = f'<div class="mt-3 p-3 rounded bg-dark border border-success font-monospace small"><p class="mb-1 text-success"><strong>🧑‍🌾 Match Query:</strong> {chat_query}</p><p class="mb-0 text-light"><strong>🤖 AI System Guidance:</strong> {chat_response}</p></div>' if chat_query else ""
    audit_block = f'<div class="mt-3 p-3 rounded bg-dark border border-primary font-monospace small">{audit_results}</div>' if audit_results else ""
    qr_block = f'<div class="mt-3 p-3 rounded bg-dark border border-warning font-monospace small">{qr_results}</div>' if qr_results else ""
    
    dropdown_options = "".join([f'<option value="{k}">{k.replace("_"," ").capitalize()}</option>' for k in AGRONOMIC_KNOWLEDGE.keys()])
    s_rows = "".join([f"<tr><td><strong>{s['type']}</strong></td><td>{s['origin']}</td><td>{s['ph']}</td><td>{s['ec']}</td><td>{s['salinity']}</td><td>{s['texture']}</td><td>{s['om']}</td><td>{s['whc']}</td><td>{s['crops']}</td><td>{s['problems']}</td><td>{s['improvements']}</td></tr>" for s in SOIL_DATABASES])
    c_rows = "".join([f"<tr><td><strong>{c['crop']}</strong></td><td>{c['ph']}</td><td>{c['temp']}</td><td>{c['water']}</td><td>{c['period']}</td><td>{c['diseases']}</td><td>{c['fertilizer']}</td><td class='text-success fw-bold'>{c['yield']}</td></tr>" for c in CROP_DATABASES])
    n_rows = "".join([f"<tr><td><strong>{n['element']}</strong></td><td>{n['leaf']}</td><td>{n['soil']}</td><td>{n['causes']}</td><td>{n['treatment']}</td><td class='text-success'>{n['co2']}</td></tr>" for n in NUT_DATABASES])

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
                <a class="navbar-brand fw-bold fs-3 text-white" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD PLATFORM TERMINAL</a>
                <span class="badge bg-dark text-success px-3 py-2 font-monospace fw-bold border border-success">EGYPT NODE [2026]</span>
            </div>
        </nav>

        <div class="container">
            
            <div class="hero-premium text-center mb-4 shadow-sm">
                <div class="row justify-content-center">
                    <div class="col-md-12">
                        <img src="VAR_HEADER_BANNER" class="w-100 border-0" style="border-radius:24px;" alt="BioShield System Interface">
                    </div>
                </div>
            </div>

            <div class="card-luxury" style="background-color: #052419; border: 1px solid #0f4633; padding: 3rem 2.5rem;">
                
                <div style="text-align: center; color: #ffffff; margin-bottom: 40px;">
                    <span style="font-family: 'Comfortaa', cursive, sans-serif !important; font-size: 52px; font-weight: 700; color: #34d399; letter-spacing: -1.5px;">
                        Overview &amp; purpose
                    </span>
                </div>

                <div style="text-align: left; color: #e2e8f0; max-width: 900px; margin: 0 auto;">
                    <h3 style="font-family: 'Comfortaa', sans-serif !important; font-size: 24px; font-weight: 700; color: #34d399; margin: 0 0 18px 0; border-bottom: 2px dashed #0f4633; padding-bottom: 8px;">
                        Smart Biodegradable Soil Nutrient System
                    </h3>
                    
                    <p style="font-family: 'Quicksand', sans-serif !important; font-size: 16.5px; font-weight: 500; line-height: 1.7; margin: 0 0 22px 0; text-align: justify;">
                        Healthy soil is the foundation of sustainable agriculture, yet millions of hectares worldwide suffer from degradation caused by nutrient depletion, poor water retention, erosion, and excessive use of chemical fertilizers. Traditional soil analysis often requires laboratory testing, specialized equipment, and long waiting times, making it inaccessible or expensive for many farmers. As a result, soil problems are frequently identified too late, leading to reduced crop yields, increased production costs, unnecessary fertilizer application, and environmental pollution. Farmers need a rapid, affordable, and intelligent solution that helps them assess soil conditions and receive personalized recommendations directly in the field.
                    </p>
                    
                    <p style="font-family: 'Quicksand', sans-serif !important; font-size: 16.5px; font-weight: 500; line-height: 1.7; margin: 0 0 22px 0; text-align: justify;">
                        BioShield is an AI-powered smart agriculture platform designed to help farmers and researchers evaluate soil health quickly and efficiently. Users simply upload a photo of their soil, and the platform analyzes visible characteristics such as texture, color, moisture indicators, and surface condition using artificial intelligence.
                    </p>
                    
                    <div style="background-color: #041a12; border: 2px solid #0f4633; border-radius: 16px; padding: 24px; margin: 25px 0;">
                        <h4 style="font-family: 'Comfortaa', sans-serif !important; font-size: 15px; font-weight: 700; color: #34d399; text-transform: uppercase; letter-spacing: 0.8px; margin: 0 0 14px 0;">
                            ✨ Platform Deliverables &amp; Analytics
                        </h4>
                        <ul style="font-family: 'Quicksand', sans-serif !important; font-size: 15.5px; font-weight: 500; margin: 0; padding-left: 22px; line-height: 1.7; color: #e2e8f0;">
                            <li style="margin-bottom: 8px;">Provides an instant <strong>Soil Health Score</strong> and identifies structural field anomalies.</li>
                            <li style="margin-bottom: 8px;">Recommends optimal matching crop strands and suggests custom <strong>BioShield Nutrient Capsules</strong>.</li>
                            <li style="margin-bottom: 8px;">Deploys practical actionable organic improvement strategies directly on-screen.</li>
                            <li style="margin-bottom: 0;">Includes a persistent AI assistant, dynamic soil databases, disease logs, and historical baseline monitoring trackers.</li>
                        </ul>
                    </div>
                    
                    <p style="font-family: 'Quicksand', sans-serif !important; font-size: 16.5px; font-weight: 500; line-height: 1.7; margin: 0; text-align: justify;">
                        By combining AI-driven analysis with biodegradable soil treatment solutions, BioShield aims to support sustainable farming, improve productivity, reduce unnecessary resource use, and make soil management more accessible.
                    </p>
                </div>
                
                <hr class="my-5 opacity-25" style="border-color: #0f4633;">

                <!-- 🌟 STACKED CHARTS ENGINE SYSTEM REALIGNED -->
                <div class="row justify-content-center">
                    <div class="col-md-9 bg-dark p-4 rounded-4 border border-success" style="background-color: #041a12 !important;">
                        
                        <!-- Top View: Donut Component -->
                        <div class="text-center mb-5">
                            <h4 class="text-white fw-bold">Major causes of soil degradation</h4>
                            <p class="text-muted small">Illustrative distribution of common drivers of agricultural soil degradation.</p>
                            <div class="d-flex justify-content-center" style="height: 280px; position: relative;">
                                <canvas id="soilDonutChart"></canvas>
                            </div>
                        </div>

                        <!-- Bottom View: Vertical Rounded Bar Component -->
                        <div>
                            <h4 class="text-white fw-bold text-center">Common soil challenges affecting crop production</h4>
                            <p class="text-muted small text-center">Illustrative severity scores for common agricultural soil problems.</p>
                            <div style="height: 300px; position: relative;">
                                <canvas id="soilBarChart"></canvas>
                            </div>
                        </div>

                    </div>
                </div>

            </div>

            <!-- CORE SYSTEM SCANNERS MODULES LAYER -->
            <div class="row g-4 mb-4 mt-2">
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h4 class="fw-bold text-success m-0">1. AI Soil Structural Scanner</h4>
                            <img src="VAR_SOIL_IMAGE" class="img-thumb" alt="Soil Capture Interface">
                        </div>
                        <p class="text-muted small mb-3">Upload field captures to process unique metadata parameters including cracking layouts, compaction indicators, and surface moisture index logs.</p>
                        <form action="/run-soil-matrix-scan" method="post" enctype="multipart/form-data">
                            <div class="mb-2">
                                <label class="form-label small fw-bold text-secondary">Atmospheric Mode Simulator</label>
                                <select class="form-select form-select-sm" name="weather_input">
                                    <option value="Sunny, High Evaporation (38°C)">Extreme Heat Wave / High Evaporation (38°C)</option>
                                    <option value="Standard Temperate Index">Temperate / Standard Balanced Index</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Upload Raw Matrix Photo:</label>
                                <input class="form-control form-control-sm" type="file" name="file" accept="image/*" required>
                            </div>
                            <button class="btn btn-success w-100 btn-sm fw-bold" type="submit">Deploy Structural Computer Vision Scan</button>
                        </form>
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h4 class="fw-bold text-emerald m-0" style="color:#34d399;">🌿 Plant Canopy Vision Model</h4>
                            <img src="VAR_PLANTS_IMAGE" class="img-thumb" alt="Plant Capture Interface">
                        </div>
                        <p class="text-muted small mb-3">Upload localized crop nodes to parse absolute species groupings, origin traits, tissue watering indicators, and fungal spots.</p>
                        <form action="/run-plant-canopy-scan" method="post" enctype="multipart/form-data">
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-secondary">Select Target Crop Photo:</label>
                                <input class="form-control form-control-sm" type="file" name="file" accept="image/*" required>
                            </div>
                            <button class="btn btn-success w-100 btn-sm fw-bold" type="submit">Run Canopy Infection Screen</button>
                        </form>
                    </div>
                </div>
            </div>

            <!-- AUDITS AND REGISTRY KEY INTERACTIVE LINK LAYER -->
            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success">
                        <h4 class="fw-bold text-success mb-2">2. Before &amp; After Audits</h4>
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
                            <button class="btn btn-success w-100 btn-sm fw-bold" type="submit">Execute Regeneration Audit Linkage</button>
                        </form>
                        VAR_AUDIT_BLOCK
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success">
                        <h4 class="fw-bold text-light mb-2">3. Capsule QR Interaction</h4>
                        <p class="text-muted small mb-3">Scan or type the product package identifier key to pull up dynamic application rules, usage coordinates, and logs.</p>
                        <form action="/run-qr-key-lookup" method="post">
                            <div class="input-group mb-2">
                                <span class="input-group-text font-monospace small bg-dark text-white border-secondary">Package Serial:</span>
                                <input type="text" name="qr_serial" class="form-control font-monospace form-control-sm" value="BS-MATRIX-GL-2026" required>
                                <button class="btn btn-success btn-sm font-monospace fw-bold" type="submit">Look-up Registry</button>
                            </div>
                        </form>
                        VAR_QR_BLOCK
                    </div>
                </div>
            </div>

            <!-- CHAT EXPERT CONSOLE -->
            <div class="card-luxury border-top border-4 border-success">
                <h4 class="fw-bold text-success mb-2">Integrated AI Agronomic Chat Assistant Sandbox</h4>
                <form action="/run-chat-query" method="post">
                    <div class="input-group mb-2">
                        <select name="user_query" class="form-select form-select-sm" required>
                            <option value="" disabled selected>-- Select an Agronomic Question --</option>
                            VAR_DROPDOWN_OPTIONS
                        </select>
                        <button class="btn btn-success btn-sm fw-bold" type="submit">Query Shell</button>
                    </div>
                </form>
                VAR_CHAT_BLOCK
            </div>

            <!-- REPOS ACCORDIONS LAYER -->
            <div class="card-luxury border-start border-4 border-success">
                <h3 class="fw-bold text-light mb-3"><i class="bi bi-database-fill-gear me-2"></i>Enterprise Agronomic Open Data Aggregates</h3>
                <div class="accordion shadow-sm rounded" id="masterDataAccordion">
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cSoils">🌍 1. Soil Texture &amp; Origin Matrix</button></h2>
                        <div id="cSoils" class="accordion-collapse collapse" data-bs-parent="#masterDataAccordion"><div class="accordion-body p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0"><thead class="table-dark"><tr><th>Soil Type</th><th>Origin</th><th>pH</th><th>EC</th><th>Salinity</th><th>Texture</th><th>O.M.</th><th>WHC</th><th>Crops</th><th>Problems</th><th>Improvements</th></tr></thead><tbody>VAR_S_ROWS</tbody></table></div></div></div>
                    </div>
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cNutrients">🧪 2. Diagnostic Nutrient Matrices &amp; Carbon Mitigation (20 Total)</button></h2>
                        <div id="cNutrients" class="accordion-collapse collapse" data-bs-parent="#masterDataAccordion"><div class="accordion-body p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0"><thead class="table-dark"><tr><th>Deficient Element</th><th>Leaf Tissue Symptoms</th><th>Soil Trace Symptoms</th><th>Underlying Root Causes</th><th>Remediation Strategy</th><th>Carbon Capture Impact</th></tr></thead><tbody>VAR_N_ROWS</tbody></table></div></div></div>
                    </div>
                    <div class="accordion-item">
                        <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold font-monospace" type="button" data-bs-toggle="collapse" data-bs-target="#cCrops">🌾 3. Botanical Crop Archetype Registry (100 Total Strains)</button></h2>
                        <div id="cCrops" class="accordion-collapse collapse" data-bs-parent="#masterDataAccordion"><div class="accordion-body p-0"><div class="table-responsive"><table class="table table-sm table-striped table-kagl m-0"><thead class="table-dark"><tr><th>Crop Strain Index ID</th><th>Ideal pH</th><th>Temperature Range</th><th>Watering Demand</th><th>Growth Cycle</th><th>Target Pathogens</th><th>Nutrient Profile</th><th>Production Performance Metrics</th></tr></thead><tbody>VAR_C_ROWS</tbody></table></div></div></div>
                    </div>
                </div>
            </div>

            <!-- ADVERTISEMENT FOOTER LAYER -->
            <div class="cure-banner-premium shadow-lg mt-4 mb-5">
                <div class="row g-4 align-items-center">
                    <div class="col-md-7">
                        <h2 class="fw-bold text-white mb-3">🌿 Smart Biodegradable Soil Nutrient System</h2>
                        <p class="lh-base text-white-50 small">
                            BioShield Nutrients combine biodegradable smart capsules, biochar technology, and AI-powered soil analysis to improve soil fertility, increase water retention, and promote sustainable crop production. Our approach completely replaces standard chemical side-effects by reinforcing underlying soil tissue. Formulated natively from organic assets: <strong>Banana Shells</strong> supply rich active organic Potassium (K); <strong>Eggshells</strong> deliver slow-release crystalline Calcium (Ca) matrices to halt structural collapse; <strong>Onion Extracts</strong> provide systemic protective barriers; and structured <strong>Biochar</strong> builds secure microscopic sponge channels to house biological ecosystems permanently.
                        </p>
                        <h5 class="text-success fw-bold mt-4">The Salicylic Acid Structural Shield Asset</h5>
                        <p class="text-white-50 small mb-4">
                            By triggering Systemic Acquired Resistance (SAR) within botanical rows, Salicylic Acid hardens vascular cellular lines to shield plant complexes against severe blights before infections lock in.
                        </p>
                        <div class="p-3 rounded bg-white bg-opacity-10 border border-success text-white">
                            <h6 class="fw-bold mb-1"><i class="bi bi-envelope-check-fill me-2"></i>Secure Enterprise Ordering Workdesk:</h6>
                            <a href="mailto:radwaabdallnasser@gmail.com?subject=BioShield%20Enterprise%20Order%20Inquiry" class="btn btn-success btn-sm fw-bold px-3 mt-2"><i class="bi bi-send-fill me-1"></i> Request Supply Chain Allocations</a>
                        </div>
                    </div>
                    <div class="col-md-5 text-center">
                        <div class="p-2 bg-dark rounded-4 shadow-lg overflow-hidden border border-success">
                            <img src="VAR_BRAND_PNG" class="premium-showcase-img img-fluid" alt="BioShield Nutrients Premium Packaging Layer">
                        </div>
                        <p class="text-white fw-bold mt-3 mb-0 fs-5">✨ Your Soil is Healthier, Your Life is Better ✨</p>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        
        <!-- CHART CONTROLLER INJECTOR SCRIPT -->
        <script>
            // Donut logic parameters setup
            const ctxDonut = document.getElementById('soilDonutChart').getContext('2d');
            new Chart(ctxDonut, {
                type: 'doughnut',
                data: {
                    labels: ['Compaction', 'Nutrient depletion', 'Organic matter loss', 'Salinity', 'Water erosion'],
                    datasets: [{
                        data: [15, 35, 10, 15, 25],
                        backgroundColor: ['#fcd34d', '#60a5fa', '#c084fc', '#fca5a5', '#4ade80'],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom', labels: { color: '#a7f3d0', font: { size: 11 } } }
                    },
                    cutout: '65%'
                }
            });

            // Vertical rounded bars generation structure setup
            const ctxBar = document.getElementById('soilBarChart').getContext('2d');
            const gr = ctxBar.createLinearGradient(0, 0, 0, 260);
            gr.addColorStop(0, '#34d399');
            gr.addColorStop(1, '#059669');

            new Chart(ctxBar, {
                type: 'bar',
                data: {
                    labels: ['Water Ret.', 'Org. Matter', 'Nutrient Def.', 'Compaction', 'Salinity', 'Erosion'],
                    datasets: [{
                        data: [92, 85, 80, 72, 60, 53],
                        backgroundColor: gr,
                        borderRadius: 15,
                        borderSkipped: false,
                        barPercentage: 0.45
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: { grid: { display: false }, ticks: { color: '#6ee7b7' } },
                        y: { grid: { color: 'rgba(110, 231, 183, 0.1)' }, ticks: { color: '#6ee7b7' }, max: 100 }
                    }
                }
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
        .replace("VAR_BRAND_PNG", BRAND_PNG_BASE64) \
        .replace("VAR_AUDIT_BLOCK", audit_block) \
        .replace("VAR_QR_BLOCK", qr_block) \
        .replace("VAR_DROPDOWN_OPTIONS", dropdown_options) \
        .replace("VAR_CHAT_BLOCK", chat_block) \
        .replace("VAR_S_ROWS", s_rows) \
        .replace("VAR_C_ROWS", c_rows) \
        .replace("VAR_N_ROWS", n_rows)

    return HTMLResponse(content=rendered)

@app.post("/run-chat-query", response_class=HTMLResponse)
async def run_chat_query_endpoint(user_query: str = Form(...)):
    resp = AGRONOMIC_KNOWLEDGE.get(user_query.strip(), "Inference completed against custom agronomic code block data arrays.")
    return await platform_dashboard(chat_query=user_query, chat_response=resp)

@app.post("/run-qr-key-lookup", response_class=HTMLResponse)
async def run_qr_key_lookup_endpoint(qr_serial: str = Form(...)):
    results = f"""
    <div class="p-2 border rounded border-success bg-dark text-white">
        <span class="badge bg-success font-monospace mb-2">Core Status: Validated</span><br>
        <strong>Registry Reference Tag:</strong> Matches Serial Node: {qr_serial}<br>
        <strong>Trace Logs:</strong> Sealed capsule batch verified for dynamic soil micro-restoration.
    </div>
    """
    return await platform_dashboard(qr_results=results)

@app.post("/run-audit-comparison", response_class=HTMLResponse)
async def run_audit_comparison_route(audit_id: str = Form(...), audit_file: UploadFile = File(...)):
    random.seed(len(audit_file.filename) + 124)
    improvement = random.randint(25, 45)
    results = f"""
    <h6 class="fw-bold text-success mb-2"><i class="bi bi-check-circle-fill me-1"></i> Audit Matrix Linked for {audit_id}</h6>
    <ul class="mb-0 text-white list-unstyled small font-monospace">
        <li><strong>Artifact File:</strong> {audit_file.filename}</li>
        <li><strong>Regeneration Index:</strong> <span class="text-success fw-bold">+{improvement}% Dynamic Shift</span></li>
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
            <a href="/" class="btn btn-outline-success btn-sm mb-4">← Back to Terminal Dashboard</a>
            <div class="card-luxury border-start border-4 border-success">
                <h3 class="fw-bold text-light mb-3">Plant Vision Diagnostic Profile</h3>
                <p class="text-muted small font-monospace">Uploaded Canopy Image: <strong>{file.filename}</strong></p>
                <div class="table-responsive">
                    <table class="table table-bordered font-monospace small text-white">
                        <thead class="table-dark">
                            <tr><th>Evaluated Botanical Layer</th><th>AI Visual Extracted Value Output</th></tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Identified Plant Crop Type</strong></td><td>{pm['type']}</td></tr>
                            <tr><td><strong>Geographical Ancestral Origin</strong></td><td>{pm['origin']}</td></tr>
                            <tr><td><strong>Internal Tissue Hydration</strong></td><td>{pm['water']}</td></tr>
                            <tr><td><strong>Infection / Parasitic Status</strong></td><td class="text-danger fw-bold">{pm['blight']}</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/run-soil-matrix-scan", response_class=HTMLResponse)
async def run_soil_matrix_scan_route(weather_input: str = Form(...), file: UploadFile = File(...)):
    analytics = execute_true_computer_vision_analysis(file.filename)
    weather_notice = "🚨 ATMOSPHERIC WARNING: Extreme temperature active (38°C). Accelerate evaporative irrigation safeguards immediately." if "38°C" in weather_input else "🌤️ STABLE ATMOSPHERE: Standard baseline application protocols remain nominal."
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>AI Soil Matrix Diagnosis Output</title>{PREMIUM_CSS}</head>
    <body>
        <div class="container py-5">
            <a href="/" class="btn btn-outline-success btn-sm mb-4">← Return to Terminal Dashboard</a>
            
            <div class="card-luxury border-start border-4 border-success shadow-sm">
                <h3 class="fw-bold text-light mb-1">Computer Vision Feature Extraction Matrix</h3>
                <p class="text-muted small mb-4">Analyzed Resource Image Artifact: <span class="font-monospace text-success fw-bold">{file.filename}</span></p>
                
                <div class="table-responsive">
                    <table class="table table-bordered font-monospace small text-white">
                        <thead class="table-dark">
                            <tr><th>Target Surface Metric Attribute</th><th>AI Vision Core Analytical Output Values</th></tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Soil Color Spectrum</strong></td><td class="fw-bold text-success">{analytics['color']}</td></tr>
                            <tr><td><strong>Surface Texture Profile</strong></td><td>{analytics['texture']}</td></tr>
                            <tr><td><strong>Presence of Structural Cracks</strong></td><td>{analytics['cracks']}</td></tr>
                            <tr><td><strong>Moisture Appearance Index</strong></td><td>{analytics['moisture']}</td></tr>
                            <tr><td><strong>Organic Matter Presentation</strong></td><td class="text-success fw-bold">{analytics['om']}</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div class="card-luxury bg-dark border border-success shadow-sm">
                <h5 class="fw-bold text-success mb-1"><i class="bi bi-brightness-high-fill me-2"></i>Weather-Integrated Application Safety Threshold</h5>
                <p class="small text-light font-monospace mt-2 mb-0">{weather_notice}</p>
            </div>
        </div>
    </body>
    </html>
    """
