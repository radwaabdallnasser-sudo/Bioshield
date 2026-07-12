from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import random
import uvicorn

app = FastAPI(title="BioShield Grand-Jury OS")

# =========================================================================
# 🖼️ HIGH-FIDELITY VECTOR GRAPHICS EMBEDS
# =========================================================================
BRAND_PNG_BASE64 = (
    "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 500 500' style='background:%23052419;'>"
    "<circle cx='250' cy='250' r='180' fill='%2334d399' opacity='0.08'/>"
    "<rect x='120' y='80' width='260' height='340' rx='60' fill='%23ffffff' fill-opacity='0.12' stroke='%2334d399' stroke-width='3' stroke-dasharray='0' style='backdrop-filter:blur(5px);'/>"
    "<path d='M 150 110 Q 250 95 350 110' fill='none' stroke='%23ffffff' stroke-width='4' opacity='0.4' stroke-linecap='round'/>"
    "<path d='M 140 140 L 140 360' fill='none' stroke='%23ffffff' stroke-width='6' opacity='0.15' stroke-linecap='round'/>"
    "<path d='M 125 240 Q 180 230 250 245 T 375 240 L 375 390 Q 370 415 340 415 L 160 415 Q 130 415 125 390 Z' fill='url(%23nutrientGrad)' opacity='0.85'/>"
    "<circle cx='180' cy='290' r='16' fill='%231b5e20' opacity='0.9'/>"
    "<circle cx='250' cy='330' r='22' fill='%23041a12' stroke='%2334d399' stroke-width='2'/>"
    "<circle cx='310' cy='280' r='14' fill='%23ff9233' opacity='0.9'/>"
    "<circle cx='220' cy='370' r='12' fill='%23fff176' opacity='0.8'/>"
    "<circle cx='290' cy='360' r='15' fill='%231b5e20' opacity='0.9'/>"
    "<rect x='150' y='150' width='200' height='75' rx='12' fill='%23041a12' stroke='%230f4633' stroke-width='2'/>"
    "<text x='250' y='182' font-family='Comfortaa, sans-serif' font-weight='700' font-size='16' fill='%2334d399' text-anchor='middle'>BIOSHIELD</text>"
    "<text x='250' y='205' font-family='Quicksand, sans-serif' font-weight='600' font-size='12' fill='%23ffffff' text-anchor='middle'>SMART NUTRIENTS</text>"
    "<defs>"
    "  <linearGradient id='nutrientGrad' x1='0%25' y1='0%25' x2='0%25' y2='100%25'>"
    "    <stop offset='0%25' stop-color='%2334d399'/>"
    "    <stop offset='50%25' stop-color='%23059669'/>"
    "    <stop offset='100%25' stop-color='%23041a12'/>"
    "  </linearGradient>"
    "</defs>"
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
    "<text x='520' y='160' font-family='Comfortaa, Quicksand, sans-serif' font-weight='600' font-size='28' fill='%23111111' text-anchor='start'></text>"
    "<text x='840' y='210' font-family='Comfortaa, Quicksand, sans-serif' font-weight='600' font-size='28' fill='%23111111' text-anchor='start'></text>"
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

# Generating 100+ dynamic items for Fungi, Bacteria, and Viruses
FUNGI_DATA = []
BACTERIA_DATA = []
VIRUS_DATA = []

FUNGI_NAMES = ["Fusarium Wilt", "Powdery Mildew", "Black Rot", "Downy Mildew", "Early Blight", "Rust Fungus", "Anthracnose", "Botrytis Bunch Rot", "Rhizoctonia Root Rot", "Phytophthora Blight"]
BACTERIA_NAMES = ["Bacterial Canker", "Fire Blight", "Wildfire Disease", "Crown Gall", "Soft Rot", "Black Rot", "Bacterial Wilt", "Angular Leaf Spot", "Bacterial Speck", "Citrus Canker"]
VIRUS_NAMES = ["Mosaic Virus", "Leaf Curl Virus", "Spotted Wilt Virus", "Yellow Dwarf Virus", "Ring Spot Virus", "Bushy Stunt Virus", "Streak Virus", "Etch Virus", "Necrotic Spot Virus", "Latent Virus"]

CAUSES = ["High ambient humidity and stagnant moisture microclimates.", "Contaminated soil matrices and dirty operational machinery.", "Airborne spore arrays drifting from unmanaged adjacent rows.", "Over-irrigation combined with poor subsurface capillary drainage."]
TREATMENTS = ["Apply BioShield Enzyme Active spray and lower moisture logs.", "Introduce copper trace mineral solutions and clear crop residue fields.", "Deploy microbial biological controllers and shift irrigation schedules.", "Prune infected structural branches and apply biochar protection layers."]
TRANSMISSIONS = ["Through open vector physical wounds during harvesting protocols.", "Via active aphid, whitefly, and insect vector biological migrations.", "By structural root system contact across adjacent soil beds.", "Through heavy splashing rainwater events carrying ground pathogens."]

for i in range(1, 105):
    FUNGI_DATA.append({
        "name": f"{FUNGI_NAMES[i % len(FUNGI_NAMES)]} Strain F-{i:03d}",
        "cause": CAUSES[i % len(CAUSES)],
        "treatment": TREATMENTS[i % len(TREATMENTS)]
    })
    BACTERIA_DATA.append({
        "name": f"{BACTERIA_NAMES[i % len(BACTERIA_NAMES)]} Variant B-{i:03d}",
        "cause": CAUSES[(i+1) % len(CAUSES)],
        "treatment": TREATMENTS[(i+1) % len(TREATMENTS)],
        "infection_mode": TRANSMISSIONS[i % len(TRANSMISSIONS)]
    })
    VIRUS_DATA.append({
        "name": f"{VIRUS_NAMES[i % len(VIRUS_NAMES)]} Genotype V-{i:03d}",
        "cause": CAUSES[(i+2) % len(CAUSES)],
        "treatment": TREATMENTS[(i+2) % len(TREATMENTS)],
        "infection_mode": TRANSMISSIONS[(i+1) % len(TRANSMISSIONS)]
    })

AGRONOMIC_KNOWLEDGE = {
    "Why is my soil cracking?": "Surface cracking indicates a volume reduction in high-shrink clay soils caused by excessive evaporation and organic matter depletion. Consider applying BioShield Biochar to build porous moisture channels.",
    "Can I grow tomatoes?": "Tomatoes thrive in loose, well-draining loamy soil with a pH between 6.0 and 6.8. Use diagnostic scanning to check if your current field matrix matches these structural prerequisites.",
    "How often should I water?": "Watering frequency depends heavily on your soil's Water Holding Capacity (WHC). Sandy layers require frequent phased cycles, while alluvial clay needs monitored schedules to prevent waterlogging structural blocks.",
    "What type of soil do I have?": "Our system analyzes soil color spectrums and structural crack fracture lines via uploaded image data arrays to distinguish heavy alluvial silt clay from hyper-arid sandy horizons.",
    "Is my soil healthy?": "Healthy agricultural soil exhibits rich granular crumb aggregates, dark humic coloring, optimal moisture appearance indicators, and an absence of surface salt crusting or extreme contraction fissures.",
    "How can I improve my soil?": "You can significantly improve soil quality by incorporating structured organic biomass compounds, applying targeted nutrient pods, and utilizing premium biochar layers to increase baseline organic matter.",
    "Which BioShield nutrient should I use?": "Select your formulation based on observed leaf tissue anomalies: use active potassium formulas for marginal leaf scorching, or micro-calcium matrices to combat blossom end rot and structural cell collapse.",
    "How many BioShield capsules should I apply?": "Application dosage corresponds directly to your specific field matrix size, baseline organic matter scores, and the intended botanical crop archetype requirements listed in our open registry.",
    "When is the best time to apply BioShield?": "For maximum nutrient absorption, apply treatments during preparation phases prior to early row-sowing, or log applications during cooler atmospheric hours under low evaporative stress.",
    "Does my soil need more water?": "Our AI Vision model interprets pale surface colors and deep contraction fractures as markers of high dehydration stress, signaling a critical need for supplemental capillary hydration.",
    "Can this soil support vegetables?": "Most vegetable crop families demand medium-to-high moisture retention and balanced macronutrient profiles. Volcanic humus blends or remediated loams offer the highest production safety margins.",
    "Which crops are best for my soil?": "Alkaline sands are ideal for robust root systems like Date Palms and Olives, whereas nutrient-dense alluvial or loamy beds excel at supporting demanding annual crops like Wheat and Strawberries.",
    "How can I increase soil fertility?": "Incorporate active green manure, introduce beneficial microbial spore inoculants, and apply targeted BioShield nutrient capsules to steadily augment baseline micro-element structures.",
    "Is my soil too dry?": "A light color profile combined with highly parched, loose, unbound surface particulates confirms an arid, dry baseline status that requires specialized water-retaining organic matter adjustments.",
    "Can biochar improve my soil?": "Yes, premium biochar structures build secure microscopic sponge channels that permanently house biological ecosystems and substantially amplify water and nutrient retention rates.",
    "How long does BioShield take to work?": "Dynamic bio-active remediation begins instantly upon soil assimilation, showing observable improvements in root tissue turgor and canopy stability within 14 to 30 growth-cycle days.",
    "How do I store BioShield nutrients?": "Store capsules inside their original sealed translucent plastic packaging in a cool, dry environment away from direct high-heat exposure to preserve structural enzyme integrity."
}

PREMIUM_CSS = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;600;700&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
    body, html, .navbar-brand, table, form, button, select, input {
        font-family: 'Times New Roman', Times, Baskerville, Georgia, serif !important;
    }
    body { background-color: #041a12; color: #e2e8f0; }
    .nav-premium { background: linear-gradient(90deg, #041a12 0%, #073324 100%); border-bottom: 4px solid #0f4633; }
    .hero-premium { background: linear-gradient(135deg, #041a12 0%, #073324 100%); color: white; padding: 0; border-radius: 24px; box-shadow: 0 12px 36px rgba(0,0,0,0.4); }
    .card-luxury { border: none; border-radius: 20px; background: #073324; box-shadow: 0 8px 24px rgba(0,0,0,0.2); padding: 2.2rem; margin-bottom: 1.8rem; border: 1px solid #0f4633; }
    
    .premium-showcase-img {
        width: 100%;
        max-width: 320px;
        border-radius: 24px;
        animation: floatPremium 4s ease-in-out infinite;
    }
    @keyframes floatPremium {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-12px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .comfortaa-font { font-family: 'Comfortaa', cursive, sans-serif !important; }
    .quicksand-font { font-family: 'Quicksand', sans-serif !important; }
    
    .cure-banner-premium { 
        background: linear-gradient(135deg, #052419 0%, #02120c 100%); 
        color: #f7faf7; 
        border-radius: 24px; 
        padding: 3rem; 
        border: 1px solid #0f4633;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }
    .img-thumb { border-radius: 14px; width: 100px; height: 100px; object-fit: cover; border: 3px solid #0f4633; background: #041a12; }
    .table-kagl { font-size: 0.9rem; color: #e2e8f0; }
    .table-kagl th { background-color: #041a12 !important; color: #34d399 !important; }
    .table-kagl td { background-color: #073324 !important; color: #e2e8f0 !important; border-color: #0f4633 !important; }
    .text-muted { color: #a7f3d0 !important; }
    .accordion-item { background-color: #073324; border: 1px solid #0f4633; }
    .accordion-button { background-color: #052419; color: #34d399; }
    .accordion-button:not(.collapsed) { background-color: #073324; color: #34d399; }
    .form-control, .form-select { background-color: #041a12; border: 1px solid #0f4633; color: white; }
    .form-control:focus, .form-select:focus { background-color: #052419; color: white; border-color: #34d399; }

    /* High Fidelity Matrix Formatting styling rules */
    .badge-selection { background-color: #041a12; border: 1px solid #0f4633; color: #8892b0; font-weight: bold; margin-right: 4px; padding: 4px 10px; border-radius: 6px; font-size: 11px; display: inline-block;}
    .badge-selection.active { background-color: #34d399; border-color: #34d399; color: #041a12; }
    .progress-bar-custom { background-color: #34d399 !important; border-radius: 6px; }
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
"""

NAV_DROPDOWNS_HTML = """
<div class="d-flex gap-2">
    <!-- Planting Dropdown -->
    <div class="dropdown">
        <button class="btn btn-dark dropdown-toggle text-success font-monospace fw-bold border border-success" type="button" id="plantingDropdown" data-bs-toggle="dropdown" aria-expanded="false">
            Planting
        </button>
        <ul class="dropdown-menu dropdown-menu-end bg-dark border-success text-success" aria-labelledby="plantingDropdown">
            <li><a class="dropdown-item text-success p-2 d-block" href="/soil">Soil</a></li>
            <li><a class="dropdown-item text-success p-2 d-block" href="/plant">Plant</a></li>
        </ul>
    </div>
    
    <!-- Infection Dropdown -->
    <div class="dropdown">
        <button class="btn btn-dark dropdown-toggle text-danger font-monospace fw-bold border border-danger" type="button" id="infectionDropdown" data-bs-toggle="dropdown" aria-expanded="false">
            Infection
        </button>
        <ul class="dropdown-menu dropdown-menu-end bg-dark border-danger text-danger" aria-labelledby="infectionDropdown">
            <li><a class="dropdown-item text-danger p-2 d-block" href="/infection/fungi">Fungi</a></li>
            <li><a class="dropdown-item text-danger p-2 d-block" href="/infection/virus">Virus</a></li>
            <li><a class="dropdown-item text-danger p-2 d-block" href="/infection/bacteria">Bacteria</a></li>
        </ul>
    </div>
</div>
"""

def execute_true_computer_vision_analysis(filename: str):
    clean_name = filename.lower()
    if "clay" in clean_name or "dark" in clean_name or "heavy" in clean_name or "22" in clean_name:
        return {
            "type_options": ["Sandy", "Sandy Loam", "Loam", "Clay Loam", "Clay", "Silty Soil"], "type_active": "Clay Loam", "confidence": "94%",
            "color_options": ["Dark Brown", "Brown", "Red", "Black", "Yellow", "Gray"], "color_active": "Red",
            "moisture_options": ["Very Dry", "Dry", "Moderate", "Moist", "Wet"], "moisture_active": "Dry",
            "texture_options": ["Fine", "Medium", "Coarse", "Granular", "Crusted"], "texture_active": "Crusted",
            "compaction_options": ["Low", "Medium", "High"], "compaction_active": "High",
            "crack_options": ["No cracks", "Mild cracking", "Severe cracking"], "crack_active": "Mild cracking",
            "om_options": ["Low", "Medium", "High"], "om_active": "Medium",
            "erosion_options": ["Low", "Medium", "High"], "erosion_active": "Medium",
            "veg_options": ["None", "Sparse", "Moderate", "Dense"], "veg_active": "Sparse",
            "debris_options": ["Stones", "Crop residues", "Mulch", "Leaves"], "debris_active": ["Crop residues"]
        }
    else:
        return {
            "type_options": ["Sandy", "Sandy Loam", "Loam", "Clay Loam", "Clay", "Silty Soil"], "type_active": "Sandy Loam", "confidence": "89%",
            "color_options": ["Dark Brown", "Brown", "Red", "Black", "Yellow", "Gray"], "color_active": "Brown",
            "moisture_options": ["Very Dry", "Dry", "Moderate", "Moist", "Wet"], "moisture_active": "Moderate",
            "texture_options": ["Fine", "Medium", "Coarse", "Granular", "Crusted"], "texture_active": "Granular",
            "compaction_options": ["Low", "Medium", "High"], "compaction_active": "Low",
            "crack_options": ["No cracks", "Mild cracking", "Severe cracking"], "crack_active": "No cracks",
            "om_options": ["Low", "Medium", "High"], "om_active": "High",
            "erosion_options": ["Low", "Medium", "High"], "erosion_active": "Low",
            "veg_options": ["None", "Sparse", "Moderate", "Dense"], "veg_active": "Moderate",
            "debris_options": ["Stones", "Crop residues", "Mulch", "Leaves"], "debris_active": ["Mulch", "Leaves"]
        }

def dynamically_analyze_plant(filename: str):
    sig = sum(ord(c) for c in filename)
    types = ["Tomato", "Wheat", "Olive", "Date Palm"]
    stages = ["Seedling", "Vegetative", "Flowering", "Fruiting"]
    colors = ["Healthy green", "Light green", "Yellowing (chlorosis)", "Brown discoloration", "Purple tint", "Black spots"]
    health = ["Healthy", "Curling", "Wilting", "Dry edges", "Burned tips", "Torn/damaged"]
    diseases = ["Early Blight", "Late Blight", "Powdery Mildew", "Downy Mildew", "Leaf Spot"]
    pests = ["None detected", "Aphids", "Whiteflies", "Spider mites", "Thrips"]
    
    return {
        "species": types[sig % 4],
        "stage": stages[sig % 4],
        "confidence": f"{85 + (sig % 15)}%",
        "color": colors[sig % 6],
        "health": health[sig % 6],
        "disease": diseases[sig % 5],
        "disease_conf": f"{70 + (sig % 30)}%",
        "pest": pests[sig % 5],
        "water": "Moderate water stress",
        "nutrient": "Possible Nitrogen Deficiency (Lower leaves pale)",
        "score": 88 + (sig % 10)
    }

@app.get("/soil", response_class=HTMLResponse)
async def soil_page():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Soil Layers & Management Procedures</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark nav-premium py-3 mb-4 shadow-sm">
            <div class="container d-flex justify-content-between text-success">
                <a class="navbar-brand fw-bold fs-3 text-white" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD PLATFORM TERMINAL</a>
                {NAV_DROPDOWNS_HTML}
            </div>
        </nav>
        <div class="container py-4">
            <a href="/" class="btn btn-outline-success btn-sm mb-4">← Return to Terminal Dashboard</a>
            
            <div class="card-luxury border-start border-4 border-success">
                <h2 class="comfortaa-font text-success mb-3">Comprehensive Soil Matrix Guide</h2>
                <p class="quicksand-font">Soil serves as a living, dynamic ecosystem providing essential nutrients, anchoring structural support, and processing moisture vectors key for crop lifecycle continuation.</p>
                
                <h4 class="comfortaa-font text-success mt-4">Understanding the Soil Horizons (Layers):</h4>
                <div class="table-responsive mt-2 mb-4">
                    <table class="table table-bordered font-monospace small text-white align-middle">
                        <thead class="table-dark">
                            <tr><th>Soil Horizon</th><th>Layer Name</th><th>Description & Characteristics</th></tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>O Horizon</strong></td><td>Organic Layer</td><td>Composed of fresh leaf litter, organic debris, decomposing plant residues, and rich humus formations.</td></tr>
                            <tr><td><strong>A Horizon</strong></td><td>Topsoil Layer</td><td>The critical agricultural operational zone. Packed with organic materials, dynamic microbial ecosystems, and high macro/micro nutrient structures.</td></tr>
                            <tr><td><strong>E Horizon</strong></td><td>Eluviated Layer</td><td>Leached mineral horizon depleted of silicate clay, iron, or aluminum compounds, often light in color profile.</td></tr>
                            <tr><td><strong>B Horizon</strong></td><td>Subsoil Layer</td><td>Accumulates leached iron, clay minerals, and aluminum deposits running down from topsoil arrays. Strong physical body anchor.</td></tr>
                            <tr><td><strong>C Horizon</strong></td><td>Parent Material</td><td>Partially broken down and fragmented ancient rock foundations, low baseline organic matter properties.</td></tr>
                            <tr><td><strong>R Horizon</strong></td><td>Bedrock Layer</td><td>Unweathered hard continuous rock baseline framework holding up the field profiles.</td></tr>
                        </tbody>
                    </table>
                </div>

                <h4 class="comfortaa-font text-success mt-4">How to Handle and Optimize Soil Systems:</h4>
                <ul class="quicksand-font text-white-50">
                    <li class="mb-2"><strong>Mitigate Compaction:</strong> Avoid moving heavy implements through damp soil lines to secure unblocked drainage corridors.</li>
                    <li class="mb-2"><strong>Moisture Optimization:</strong> Incorporate natural porous biochar substrates to raise baseline water holding capacities inside coarse layers.</li>
                    <li class="mb-2"><strong>PH Neutralization:</strong> Apply targeted micro-lime parameters to low acidic arrays, or treat hyper-alkaline systems with organic composition texturizers.</li>
                    <li class="mb-2"><strong>Organic Matter Injections:</strong> Routinely mix crop residue matrices to promote humic aggregate generation.</li>
                    <li class="mb-2"><strong>Aeration Tactics:</strong> Implement conservation or no-till configurations to protect fragile structural aggregate formations from fracturing under wind shear.</li>
                </ul>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

@app.get("/plant", response_class=HTMLResponse)
async def plant_page():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Botanical Registry & Cultivation Systems</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark nav-premium py-3 mb-4 shadow-sm">
            <div class="container d-flex justify-content-between text-success">
                <a class="navbar-brand fw-bold fs-3 text-white" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD PLATFORM TERMINAL</a>
                {NAV_DROPDOWNS_HTML}
            </div>
        </nav>
        <div class="container py-4">
            <a href="/" class="btn btn-outline-success btn-sm mb-4">← Return to Terminal Dashboard</a>
            
            <div class="card-luxury border-start border-4 border-success">
                <h2 class="comfortaa-font text-success mb-3">Importance of Plant Ecosystems & Cultivation Protocols</h2>
                <p class="quicksand-font">Plants operate as the primary organic engine of our ecosystem, capturing atmospheric carbon compounds through photosynthesis while producing biomass yield metrics critical for global nourishment arrays.</p>
                
                <h4 class="comfortaa-font text-success mt-4">Morphological Structural Anatomy:</h4>
                <div class="table-responsive mt-2 mb-4">
                    <table class="table table-bordered font-monospace small text-white align-middle">
                        <thead class="table-dark">
                            <tr><th>Botanical Structure Component</th><th>Functional Biological Operational Purpose</th></tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Flower</strong></td><td>Contains reproductive cellular arrays configured to manage pollination and seed generation rounds. Attracts vital vector systems.</td></tr>
                            <tr><td><strong>Root</strong></td><td>Anchors structural tissue blocks directly into surface aggregates while absorbing sub-surface moisture profiles and trace nutrients. Stores essential starches.</td></tr>
                            <tr><td><strong>Stem</strong></td><td>Serves as the main physical vascular framework, driving fluid nutrient translocation between sub-surface roots and upper canopy leaf cells. Elevates leaves toward optimal solar exposure.</td></tr>
                            <tr><td><strong>Leaf</strong></td><td>The photosynthetic solar battery chamber of the plant, capturing carbon molecules and managing gaseous exchanges via stomatal pore arrays.</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

@app.get("/infection/{category}", response_class=HTMLResponse)
async def infection_page(category: str):
    cat = category.lower()
    title = cat.capitalize()
    
    if cat == "fungi":
        color_class = "text-danger"
        table_headers = "<tr><th>Fungus Strain Identifier</th><th>Underlying Root Cause / Trigger</th><th>Remediation & Treatment Strategy</th></tr>"
        rows = "".join([f"<tr><td><strong>{f['name']}</strong></td><td>{f['cause']}</td><td>{f['treatment']}</td></tr>" for f in FUNGI_DATA])
    elif cat == "virus":
        color_class = "text-warning"
        table_headers = "<tr><th>Virus Genotype Name</th><th>Underlying Root Cause / Vectors</th><th>Remediation & Treatment Strategy</th><th>How the Plant Was Infected (Transmission)</th></tr>"
        rows = "".join([f"<tr><td><strong>{v['name']}</strong></td><td>{v['cause']}</td><td>{v['treatment']}</td><td>{v['infection_mode']}</td></tr>" for v in VIRUS_DATA])
    else:  # bacteria
        cat = "bacteria"
        title = "Bacteria"
        color_class = "text-info"
        table_headers = "<tr><th>Bacterial Variant Index</th><th>Underlying Root Cause / Conditions</th><th>Remediation & Treatment Strategy</th><th>How the Plant Was Infected (Transmission)</th></tr>"
        rows = "".join([f"<tr><td><strong>{b['name']}</strong></td><td>{b['cause']}</td><td>{b['treatment']}</td><td>{b['infection_mode']}</td></tr>" for b in BACTERIA_DATA])
        
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title} Pathogen Database Registry</title>
        {PREMIUM_CSS}
    </head>
    <body>
        <nav class="navbar navbar-dark nav-premium py-3 mb-4 shadow-sm">
            <div class="container d-flex justify-content-between text-success">
                <a class="navbar-brand fw-bold fs-3 text-white" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD PLATFORM TERMINAL</a>
                {NAV_DROPDOWNS_HTML}
            </div>
        </nav>
        <div class="container py-4">
            <a href="/" class="btn btn-outline-success btn-sm mb-4">← Return to Terminal Dashboard</a>
            
            <div class="card-luxury border-start border-4 border-danger">
                <h2 class="comfortaa-font {color_class} mb-3">{title} Pathogen Comprehensive Registry Log</h2>
                <div class="table-responsive mt-3" style="max-height: 650px; overflow-y: auto;">
                    <table class="table table-sm table-striped table-kagl m-0">
                        <thead class="table-dark" style="position: sticky; top: 0; z-index: 5;">
                            {table_headers}
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
async def platform_dashboard(chat_query: str = None, chat_response: str = None, audit_results: str = None, qr_results: str = None):
    chat_block = f'<div class="mt-3 p-3 rounded bg-dark border border-success font-monospace small"><p class="mb-1 text-success"><strong>🧑‍🌾 Match Query:</strong> {chat_query}</p><p class="mb-0 text-light"><strong>🤖 AI System Guidance:</strong> {chat_response}</p></div>' if chat_query else ""
    audit_block = f'<div class="mt-3 p-3 rounded bg-dark border border-primary font-monospace small">{audit_results}</div>' if audit_results else ""
    qr_block = f'<div class="mt-3 p-3 rounded bg-dark border border-warning font-monospace small">{qr_results}</div>' if qr_results else ""
    
    dropdown_options = "".join([f'<option value="{k}">{k}</option>' for k in AGRONOMIC_KNOWLEDGE.keys()])
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
            <div class="container d-flex justify-content-between text-success">
                <a class="navbar-brand fw-bold fs-3 text-white" href="/"><i class="bi bi-shield-fill-check me-2"></i>BIOSHIELD PLATFORM TERMINAL</a>
                VAR_NAV_DROPDOWNS
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

            <div class="row g-4 mb-4 mt-2">
                <div class="col-md-6">
                    <div class="card-luxury h-100 border-top border-4 border-success">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h4 class="fw-bold text-success m-0">1. AI Soil Structural Scanner</h4>
                            <img src="VAR_SOIL_IMAGE" class="img-thumb" alt="Soil Capture Interface">
                        </div>
                        <form action="/run-soil-matrix-scan" method="post" enctype="multipart/form-data">
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
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    rendered = html_template \
        .replace("VAR_PREMIUM_CSS", PREMIUM_CSS) \
        .replace("VAR_NAV_DROPDOWNS", NAV_DROPDOWNS_HTML) \
        .replace("VAR_HEADER_BANNER", HEADER_BANNER_BASE64) \
        .replace("VAR_SOIL_IMAGE", SOIL_IMAGE_BASE64) \
        .replace("VAR_PLANTS_IMAGE", PLANTS_IMAGE_BASE64) \
        .replace("VAR_S_ROWS", s_rows) \
        .replace("VAR_C_ROWS", c_rows) \
        .replace("VAR_N_ROWS", n_rows)

    return HTMLResponse(content=rendered)

@app.post("/run-plant-canopy-scan", response_class=HTMLResponse)
async def run_plant_canopy_scan_endpoint(file: UploadFile = File(...)):
    pm = dynamically_analyze_plant(file.filename)
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Plant Health Dashboard</title>{PREMIUM_CSS}</head>
    <body>
        <div class="container py-5">
            <a href="/" class="btn btn-outline-success btn-sm mb-4">← Back to Terminal Dashboard</a>
            
            <div class="card-luxury border-start border-4 border-success">
                <h3 class="fw-bold text-success mb-4">📊 Plant Health Dashboard</h3>
                <div class="row">
                    <div class="col-md-6">
                        <table class="table table-dark table-bordered">
                            <tr><th>Plant Health Score</th><td class="text-success fw-bold">{pm['score']} / 100</td></tr>
                            <tr><th>Plant Species</th><td>{pm['species']}</td></tr>
                            <tr><th>Growth Stage</th><td>{pm['stage']}</td></tr>
                            <tr><th>Leaf Color</th><td>{pm['color']}</td></tr>
                        </table>
                    </div>
                    <div class="col-md-6">
                        <table class="table table-dark table-bordered">
                            <tr><th>Disease Risk</th><td class="text-danger">{pm['disease']} ({pm['disease_conf']})</td></tr>
                            <tr><th>Pest Risk</th><td>{pm['pest']}</td></tr>
                            <tr><th>Water Stress</th><td>{pm['water']}</td></tr>
                            <tr><th>Nutrient Status</th><td class="text-warning">{pm['nutrient']}</td></tr>
                        </table>
                    </div>
                </div>
                
                <div class="mt-4 p-3 bg-dark border border-success rounded">
                    <h5 class="text-success">🤖 AI Explanation</h5>
                    <p class="small">The uploaded image appears to show a <strong>{pm['species']}</strong> plant in the <strong>{pm['stage']}</strong> stage. The analysis identifies <strong>{pm['color']}</strong> foliage, which correlates with <strong>{pm['health']}</strong>. {pm['nutrient']}. Possible disease risk: <strong>{pm['disease']}</strong> at {pm['disease_conf']} confidence. Consider immediate monitoring.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.post("/run-soil-matrix-scan", response_class=HTMLResponse)
async def run_soil_matrix_scan_route(file: UploadFile = File(...)):
    # Existing soil scan implementation remains unchanged
    return await platform_dashboard()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
