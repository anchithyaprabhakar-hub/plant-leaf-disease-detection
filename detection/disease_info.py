"""
Plant Pathology Knowledge Database
Comprehensive metadata, symptoms, causes, and remedy recommendations for plant leaf diseases.
"""

DISEASE_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Corn___Common_rust",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___healthy",
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___healthy"
]

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Apple Scab",
        "pathogen": "Venturia inaequalis (Fungus)",
        "severity": "Moderate to High",
        "description": "Fungal disease causing olive-green to dark brown circular velvety spots on leaves, leading to premature leaf drop and deformed fruit.",
        "symptoms": [
            "Olive-green to velvety brown spots on upper leaf surfaces.",
            "Yellowing around lesions and premature defoliation.",
            "Scabby, cracked lesions on developing fruits."
        ],
        "organic_remedies": [
            "Rake and destroy fallen leaves in autumn to eliminate overwintering spores.",
            "Apply wettable sulfur or liquid copper fungicide during early bud break.",
            "Spray baking soda solution (potassium bicarbonate) with horticultural oil."
        ],
        "chemical_control": [
            "Myclobutanil or Captan sprayed during pre-bloom to petal-fall stages.",
            "Mancozeb protective sprays applied at 7-10 day intervals during wet periods."
        ],
        "prevention": "Plant resistant cultivars (e.g., Liberty, Enterprise). Prune trees to maximize sunlight and airflow."
    },
    "Apple___Black_rot": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Black Rot (Frogeye Leaf Spot)",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "severity": "High",
        "description": "Attacks leaves, trunk cankers, and fruit, causing characteristic concentric ring spots ('frogeye' lesions).",
        "symptoms": [
            "Small purple spots that enlarge with tan centers and dark margins (frogeye appearance).",
            "Cankers on twigs and branches with peeling bark.",
            "Mummified blackened fruits clinging to branches."
        ],
        "organic_remedies": [
            "Prune out dead wood and cankered branches at least 6 inches below visible infection.",
            "Apply copper-based bio-fungicides during the dormant period."
        ],
        "chemical_control": [
            "Thiophanate-methyl or Captan sprays during petal fall.",
            "Flint (trifloxystrobin) for comprehensive fungal protection."
        ],
        "prevention": "Remove mummified apples, disinfect pruning shears with 70% alcohol between cuts."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Cedar Apple Rust",
        "pathogen": "Gymnosporangium juniperi-virginianae (Fungus)",
        "severity": "Moderate",
        "description": "Heteroecious rust fungus requiring both apple trees and eastern red cedar/juniper to complete its two-year life cycle.",
        "symptoms": [
            "Bright orange-yellow circular spots on upper leaf surface.",
            "Tube-like fungal structures (aecia) protruding from the underside of leaves.",
            "Premature defoliation in severe outbreaks."
        ],
        "organic_remedies": [
            "Remove eastern red cedar or juniper trees within 1-2 miles if possible.",
            "Apply sulfur or copper soap solutions at pink bud stage."
        ],
        "chemical_control": [
            "Immunox (myclobutanil) applied at pink bud through petal fall.",
            "Mancozeb or Dithane sprays at 7 to 10-day intervals."
        ],
        "prevention": "Choose rust-immune varieties such as Prima, Priscilla, and Freedom."
    },
    "Apple___healthy": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Healthy Foliage",
        "pathogen": "None (Healthy plant)",
        "severity": "None",
        "description": "Vibrant green leaves with crisp margins and normal chlorophyll development, indicating optimal nutritional and photosynthetic health.",
        "symptoms": ["No disease symptoms observed."],
        "organic_remedies": ["Maintain balanced organic compost application."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Continue standard seasonal irrigation, mulching, and pest monitoring."
    },
    "Corn___Common_rust": {
        "crop": "Corn / Maize (Zea mays)",
        "disease_name": "Common Rust",
        "pathogen": "Puccinia sorghi (Fungus)",
        "severity": "Moderate to High",
        "description": "Fungal foliar disease common in moderate temperatures and high humidity, producing powdery cinnamon-brown pustules.",
        "symptoms": [
            "Cinnamon-brown, powdery pustules (uredinia) scattered across both leaf surfaces.",
            "Pustules turn dark brownish-black as plant matures.",
            "Extensive chlorosis and tissue necrosis under severe infection."
        ],
        "organic_remedies": [
            "Apply neem oil or sulfur formulations at the earliest detection.",
            "Promote biodiversity and crop rotation with non-host legumes."
        ],
        "chemical_control": [
            "Azoxystrobin (Quadris) or Pyraclostrobin (Headline) applied before tasseling.",
            "Tebuconazole or Propiconazole for systemic intervention."
        ],
        "prevention": "Plant corn hybrids carrying the Rp resistance gene. Practice early planting to escape late season humidity peaks."
    },
    "Corn___Northern_Leaf_Blight": {
        "crop": "Corn / Maize (Zea mays)",
        "disease_name": "Northern Leaf Blight",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "severity": "High",
        "description": "Serious fungal threat causing elongated grayish-green cigar-shaped necrotic lesions, severely impairing photosynthesis.",
        "symptoms": [
            "Long, elliptical, grayish-green or tan lesions (1 to 6 inches long).",
            "Lesions develop dark fungal sporulation during wet weather.",
            "Leaves turn grayish and wither completely."
        ],
        "organic_remedies": [
            "Deep tillage to bury infected corn residue after harvest.",
            "Application of bio-fungicides like Bacillus subtilis."
        ],
        "chemical_control": [
            "Strobilurin and triazole premix fungicides (e.g., Headline AMP, Trivapro).",
            "Fungicide treatment is critical if lesions appear on the ear leaf before silking."
        ],
        "prevention": "Rotate crops for at least 1-2 years with soybeans or wheat. Plant resistant hybrids."
    },
    "Corn___healthy": {
        "crop": "Corn / Maize (Zea mays)",
        "disease_name": "Healthy Corn Foliage",
        "pathogen": "None",
        "severity": "None",
        "description": "Broad, deep-green, upright leaves displaying robust veining and vigorous growth without lesions or pustules.",
        "symptoms": ["Clean, healthy vegetative tissues."],
        "organic_remedies": ["Apply balanced organic nitrogen fertilizers (e.g., blood meal or compost tea)."],
        "chemical_control": ["None required."],
        "prevention": "Maintain proper plant spacing (30-inch rows) and weed control."
    },
    "Grape___Black_rot": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Grape Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "severity": "Severe",
        "description": "One of the most damaging diseases of warm, humid vineyards, attacking leaves, shoots, and fruit clusters.",
        "symptoms": [
            "Small reddish-brown circular leaf lesions with black dots (pycnidia).",
            "Berries shrivel into hard, black, wrinkled mummies.",
            "Elongated sunken black cankers on young canes."
        ],
        "organic_remedies": [
            "Prune infected canes and remove all dried mummies from vines and vineyard floor.",
            "Spray Bordeaux mixture or copper octanoate."
        ],
        "chemical_control": [
            "Mancozeb, Captan, or Myclobutanil from bud break until veraison.",
            "Difenoconazole applied at critical pre-bloom intervals."
        ],
        "prevention": "Prune grape canopy to ensure direct sunlight reaches cluster zones."
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Esca (Black Measles)",
        "pathogen": "Complex of Phaeomoniella chlamydospora & Fomitiporia mediterranea",
        "severity": "High (Chronic Trunk Disease)",
        "description": "Vascular wood rot disease causing characteristic 'tiger stripe' chlorosis on leaves and spotty berries.",
        "symptoms": [
            "'Tiger-striped' leaves with yellow-red bands and green veins.",
            "Small dark purple/brown specks on berry skins (measles).",
            "Sudden vine collapse (apoplexy) during hot spells."
        ],
        "organic_remedies": [
            "Trunk renewal and surgical removal of necrotic wood.",
            "Trichoderma-based wound protectants applied immediately after pruning."
        ],
        "chemical_control": [
            "Paint fresh pruning wounds with wound sealants containing tebuconazole or pyraclostrobin.",
            "No curative systemic fungicide exists for established wood rot."
        ],
        "prevention": "Delay pruning until late winter when spore releases decline; treat all pruning cuts >1 inch."
    },
    "Grape___healthy": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Healthy Grapevine Leaf",
        "pathogen": "None",
        "severity": "None",
        "description": "Distinctive palmate green leaves with intact lobes, clean margins, and strong vascular integrity.",
        "symptoms": ["Normal healthy foliage."],
        "organic_remedies": ["Apply kelp meal and compost mulch around vine root zones."],
        "chemical_control": ["None required."],
        "prevention": "Routine canopy training and drip irrigation."
    },
    "Pepper__bell___Bacterial_spot": {
        "crop": "Bell Pepper (Capsicum annuum)",
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas campestris pv. vesicatoria (Bacterium)",
        "severity": "High",
        "description": "Bacterial disorder thriving in warm, rainy environments, causing water-soaked lesions that lead to heavy defoliation.",
        "symptoms": [
            "Small, water-soaked, blister-like spots on lower leaf surfaces.",
            "Lesions turn brown with pale centers and dark yellow halos.",
            "Severe drop of leaves and sunscald on unprotected peppers."
        ],
        "organic_remedies": [
            "Apply fixed copper mixed with Bacillus subtilis or bio-bactericides.",
            "Immediately remove and discard infected seedlings."
        ],
        "chemical_control": [
            "Copper hydroxide combined with Mancozeb (enhances copper efficacy).",
            "Actigard (acibenzolar-S-methyl) to activate plant systemic acquired resistance."
        ],
        "prevention": "Use certified disease-free hot-water treated seeds. Avoid overhead sprinkler irrigation."
    },
    "Pepper__bell___healthy": {
        "crop": "Bell Pepper (Capsicum annuum)",
        "disease_name": "Healthy Bell Pepper Foliage",
        "pathogen": "None",
        "severity": "None",
        "description": "Smooth, glossy, elliptical dark-green leaves showing active photosynthesis and vigorous flowering potential.",
        "symptoms": ["No spotting, wilting, or chlorosis."],
        "organic_remedies": ["Apply calcium nitrate or fish emulsion for optimal fruiting."],
        "chemical_control": ["None required."],
        "prevention": "Maintain soil moisture and mulch to prevent splash contamination."
    },
    "Potato___Early_blight": {
        "crop": "Potato (Solanum tuberosum)",
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "severity": "Moderate to High",
        "description": "Fungal infection causing circular brown necrotic spots with characteristic target-board concentric rings on older leaves.",
        "symptoms": [
            "Dark brown to black lesions with concentric rings (target pattern).",
            "Yellow halo surrounding lesions.",
            "Lower, older foliage dies back first and curls upward."
        ],
        "organic_remedies": [
            "Copper octanoate or copper sulfate sprays.",
            "Spray biological fungicide containing Bacillus amyloliquefaciens.",
            "Ensure adequate nitrogen fertility to delay plant senescence."
        ],
        "chemical_control": [
            "Chlorothalonil (Bravo) or Mancozeb preventative sprays.",
            "Azoxystrobin or Boscalid for active disease management."
        ],
        "prevention": "3-4 year crop rotation away from solanaceous plants. Avoid leaf wetness by using drip irrigation."
    },
    "Potato___Late_blight": {
        "crop": "Potato (Solanum tuberosum)",
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Critical (High Emergency)",
        "description": "The notorious water mold responsible for the Irish Potato Famine; causes rapid water-soaked necrosis and devastating crop collapse in cool, moist conditions.",
        "symptoms": [
            "Irregular, pale green to dark water-soaked lesions that rapidly expand.",
            "White fungal-like downy growth on the underside of leaves during humid mornings.",
            "Brown rotting of stems and tuber flesh with foul odor."
        ],
        "organic_remedies": [
            "Strict sanitation: immediately destroy infected vines by bagging or deep burying.",
            "Regular preventive applications of copper hydroxide or Bordeaux mixture."
        ],
        "chemical_control": [
            "Mandipropamid (Revus), Cymoxanil (Curzate), or Fluopicolide.",
            "Apply systemic oomycide mixtures every 5-7 days under high risk weather alerts."
        ],
        "prevention": "Plant certified disease-free seed tubers. Eliminate all volunteer potato tubers and cull piles."
    },
    "Potato___healthy": {
        "crop": "Potato (Solanum tuberosum)",
        "disease_name": "Healthy Potato Leaf",
        "pathogen": "None",
        "severity": "None",
        "description": "Compound pinnate leaves with vibrant deep green leaflets, free of chlorotic rings or water-soaked patches.",
        "symptoms": ["Vigorous foliage with intact leaf tissue."],
        "organic_remedies": ["Side-dress with well-rotted manure or balanced organic N-P-K."],
        "chemical_control": ["None required."],
        "prevention": "Ensure hilling to protect underground tubers from sunlight and blight spores."
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas perforans / euvesicatoria (Bacterium)",
        "severity": "High",
        "description": "Common bacterial disease producing small greasy spots on leaves and scabby raised spots on fruit.",
        "symptoms": [
            "Small (less than 3mm), dark brown, water-soaked circular lesions.",
            "Lesions become angular and paper-thin with yellow margins.",
            "Premature drop of infected leaves, exposing fruit to sunscald."
        ],
        "organic_remedies": [
            "Copper soap (copper octanoate) combined with Serenade (Bacillus subtilis).",
            "Sterilize garden stakes, cages, and tools."
        ],
        "chemical_control": [
            "Fixed copper tank-mixed with Mancozeb (effective against copper-tolerant strains).",
            "Bacteriophage biopesticide sprays (AgriPhage)."
        ],
        "prevention": "Avoid handling plants when wet. Use drip irrigation rather than overhead sprinklers."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Early Blight",
        "pathogen": "Alternaria linariae / solani (Fungus)",
        "severity": "Moderate to High",
        "description": "Prevalent fungal disease initiating on lower, older leaves and producing classic 'bullseye' concentric ring lesions.",
        "symptoms": [
            "Dark brown concentric rings forming a bullseye or target pattern.",
            "Extensive yellowing (chlorosis) around the spots.",
            "Collar rot on stems and dark leathery sunken lesions on fruit stems."
        ],
        "organic_remedies": [
            "Prune off the bottom 12-18 inches of leaves to prevent soil splash.",
            "Apply copper fungicide or potassium bicarbonate weekly during damp weather.",
            "Apply thick straw or plastic mulch beneath plants."
        ],
        "chemical_control": [
            "Chlorothalonil, Mancozeb, or Daconil protective sprays.",
            "Quadris (azoxystrobin) or Luna Tranquility for systemic defense."
        ],
        "prevention": "Implement a 3-year crop rotation. Space plants at least 24-36 inches apart for air movement."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Critical (Crop Killing)",
        "description": "Extremely aggressive water mold capable of destroying entire tomato fields in days during cool, damp weather.",
        "symptoms": [
            "Large, dark brown to greasy greenish-black water-soaked patches on leaves.",
            "Fuzzy white mold on the underside of infected leaves in high humidity.",
            "Dark brown greasy lesions on stems and green fruit."
        ],
        "organic_remedies": [
            "Immediately pull and bag severely infected plants; do NOT compost them.",
            "Preventive copper sprays before weather turns cool and wet."
        ],
        "chemical_control": [
            "Revus (mandipropamid), Tanos (famoxadone + cymoxanil), or Ranman.",
            "Spray schedule intensified to 5 days under continuous rain/fog."
        ],
        "prevention": "Select late-blight-resistant cultivars (e.g., Mountain Magic, Defiant PhR, Plum Regal)."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Leaf Mold",
        "pathogen": "Passalora fulva (Fungus)",
        "severity": "Moderate",
        "description": "Frequent greenhouse and high-tunnel foliar infection developing under sustained relative humidity above 85%.",
        "symptoms": [
            "Pale greenish-yellow chlorotic spots with indistinct margins on upper leaf surfaces.",
            "Dense olive-green to grayish velvety fungal mat on lower leaf surfaces.",
            "Leaves curl, turn brown, and wither prematurely."
        ],
        "organic_remedies": [
            "Aggressive ventilation: run exhaust fans in greenhouse or high-tunnels.",
            "Spray sulfur or copper octanoate on underleaf surfaces."
        ],
        "chemical_control": [
            "Chlorothalonil or fenamidone sprays at first sign of mold.",
            "Triazole fungicides for protective coverage."
        ],
        "prevention": "Keep relative humidity strictly below 85% with fans and heating. Avoid overhead watering."
    },
    "Tomato___healthy": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Healthy Tomato Foliage",
        "pathogen": "None",
        "severity": "None",
        "description": "Vibrant emerald green leaves with serrated margins, active glandular trichomes, and no signs of spots or wilting.",
        "symptoms": ["Normal, disease-free tomato foliage."],
        "organic_remedies": ["Apply balanced compost tea, Epsom salt (magnesium sulfate), and organic mulch."],
        "chemical_control": ["None required."],
        "prevention": "Maintain regular watering to prevent blossom end rot; monitor weekly for pest vectors."
    }
}


def get_disease_info(class_name: str) -> dict:
    """Retrieve detailed disease metadata, or return a generic record if not found."""
    if class_name in DISEASE_INFO:
        return DISEASE_INFO[class_name]
    
    # Generic fallback
    crop_name = class_name.split("___")[0].replace("_", " ") if "___" in class_name else "Plant"
    condition = class_name.split("___")[1].replace("_", " ") if "___" in class_name else class_name
    return {
        "crop": crop_name,
        "disease_name": condition,
        "pathogen": "Suspected Foliar Pathogen",
        "severity": "Moderate",
        "description": f"Detected foliar abnormality on {crop_name} consistent with {condition}.",
        "symptoms": ["Leaf discoloration, spotting, or textural change."],
        "organic_remedies": ["Isolate plant, apply broad-spectrum organic copper fungicide or neem oil."],
        "chemical_control": ["Consult local agricultural extension office for appropriate fungicide/bactericide."],
        "prevention": "Sanitize equipment, ensure adequate spacing, and avoid wetting leaves when watering."
    }
