"""
Plant Pathology Knowledge Database
Comprehensive metadata, symptoms, causes, and remedy recommendations
for 38 agricultural plant leaf pathology classes across major crops.
"""

DISEASE_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


def normalize_class_name(name: str) -> str:
    """Normalizes class names across naming conventions."""
    clean = name.strip()
    # Normalize common aliases
    mapping = {
        "Corn___Common_rust": "Corn_(maize)___Common_rust_",
        "Corn___Northern_Leaf_Blight": "Corn_(maize)___Northern_Leaf_Blight",
        "Corn___healthy": "Corn_(maize)___healthy",
        "Pepper__bell___Bacterial_spot": "Pepper,_bell___Bacterial_spot",
        "Pepper__bell___healthy": "Pepper,_bell___healthy"
    }
    return mapping.get(clean, clean)


DISEASE_INFO = {
    "Apple___Apple_scab": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Apple Scab",
        "pathogen": "Venturia inaequalis (Fungus)",
        "severity": "Moderate to High",
        "description": "Fungal disease causing olive-green to dark brown circular velvety spots on leaves, leading to premature leaf drop and deformed, cracked fruit.",
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
        "description": "Attacks leaves, cankers, and fruit, producing characteristic circular 'frogeye' lesions with purple margins.",
        "symptoms": [
            "Small purple spots that enlarge with tan centers and dark margins.",
            "Cankers on twigs and branches with peeling bark.",
            "Mummified blackened fruit remaining on the tree."
        ],
        "organic_remedies": [
            "Prune out dead wood, cankers, and mummified fruit during winter dormancy.",
            "Apply copper-based fungicides before bud break."
        ],
        "chemical_control": [
            "Captan or thiophanate-methyl applied from tight cluster through cover sprays.",
            "Flint (trifloxystrobin) or Sovran protective rotation."
        ],
        "prevention": "Sanitize pruning tools between cuts with 70% isopropyl alcohol; burn diseased debris."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Cedar Apple Rust",
        "pathogen": "Gymnosporangium juniperi-virginianae (Fungus)",
        "severity": "Moderate",
        "description": "Requires eastern red cedar and apple trees to complete its lifecycle; causes bright yellow-orange lesions on leaves.",
        "symptoms": [
            "Bright orange-yellow circular spots on upper leaf surfaces.",
            "Raised tube-like fungal aecia structures on leaf undersides in summer.",
            "Defoliation and stunted fruit growth under severe infestation."
        ],
        "organic_remedies": [
            "Remove nearby eastern red cedar trees or prune out cedar galls within 500 meters.",
            "Apply sulfur or neem oil formulations at pink-bud stage."
        ],
        "chemical_control": [
            "Myclobutanil (Immunox) applied every 7-10 days from pink through petal fall.",
            "Mancozeb or Propiconazole systemic treatment."
        ],
        "prevention": "Plant rust-resistant apple varieties such as Redfree, Freedom, or Williams Pride."
    },
    "Apple___healthy": {
        "crop": "Apple (Malus domestica)",
        "disease_name": "Healthy Apple Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Lush, dark-green apple leaf with intact venation, active chlorophyll synthesis, and zero lesions or necrotic decay.",
        "symptoms": ["Smooth, symmetrical leaf blade without spots, chlorosis, or curling."],
        "organic_remedies": ["Maintain balanced organic fertilization and drip irrigation."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Continue standard seasonal monitoring and preventative tree spacing."
    },
    "Blueberry___healthy": {
        "crop": "Blueberry (Vaccinium corymbosum)",
        "disease_name": "Healthy Blueberry Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Vibrant, elliptic green blueberry leaves with optimal acid soil nutrition (pH 4.5-5.5) and no disease spots.",
        "symptoms": ["Uniform green pigmentation, intact waxy cuticle, and vigorous shoot growth."],
        "organic_remedies": ["Mulch with pine needles or acidic bark to maintain soil moisture."],
        "chemical_control": ["No treatment required."],
        "prevention": "Regular soil testing and annual drip irrigation scheduling."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry (Prunus avium / cerasus)",
        "disease_name": "Cherry Powdery Mildew",
        "pathogen": "Podosphaera clandestina (Fungus)",
        "severity": "Moderate",
        "description": "White powdery fungal mycelium covering young leaves and shoots, causing curling and stunted growth.",
        "symptoms": [
            "White talcum-powder-like patches on young foliage.",
            "Leaf upward curling, distortion, and hardening.",
            "Shriveled fruit with poor commercial yield."
        ],
        "organic_remedies": [
            "Spray potassium bicarbonate or neem oil at first sign of white coating.",
            "Prune canopy to improve ventilation and decrease shade humidity."
        ],
        "chemical_control": [
            "Myclobutanil or tebuconazole applied at petal fall.",
            "Sulfur-based fungicides applied before warm summer temperature peaks."
        ],
        "prevention": "Avoid excessive overhead sprinkler irrigation and nitrogen over-fertilization."
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry (Prunus avium / cerasus)",
        "disease_name": "Healthy Cherry Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Intact, serrated green cherry leaves showing uniform vascular development and no fungal patches.",
        "symptoms": ["Crisp green margins with no leaf perforations, yellowing, or powdery coating."],
        "organic_remedies": ["Mulch root zone and maintain regular moisture."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Continue standard orchard monitoring."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Zea mays)",
        "disease_name": "Gray Leaf Spot",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "severity": "High",
        "description": "Rectangular tan-to-gray lesions running parallel to leaf veins, causing extensive photosynthetic disruption.",
        "symptoms": [
            "Narrow rectangular lesions bounded by leaf veins.",
            "Lesions turn grayish-tan with fungal sporulation during humid weather.",
            "Extensive leaf blighting and stalk lodging."
        ],
        "organic_remedies": [
            "Crop rotation with non-host crops (soybean, alfalfa) for 2+ years.",
            "Deep tillage of crop residue to accelerate fungal decomposition."
        ],
        "chemical_control": [
            "Strobilurin (azoxystrobin, pyraclostrobin) or triazole (propiconazole) fungicides.",
            "Apply between V12 and early silking stage when lesions reach third leaf below ear."
        ],
        "prevention": "Plant corn hybrids with high genetic tolerance to Gray Leaf Spot."
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Zea mays)",
        "disease_name": "Common Corn Rust",
        "pathogen": "Puccinia sorghi (Fungus)",
        "severity": "Moderate to High",
        "description": "Cinnamon-brown powdery pustules on both upper and lower leaf surfaces that erupt and release rust spores.",
        "symptoms": [
            "Golden-brown to cinnamon pustules (uredinia) scattered over both leaf sides.",
            "Pustules rupture epidermal tissue, releasing powdery spores.",
            "Severe infections turn leaves yellow, dry, and necrotic."
        ],
        "organic_remedies": [
            "Apply biological biofungicides (Bacillus subtilis strain QST 713).",
            "Spray horticultural neem oil early upon pustule detection."
        ],
        "chemical_control": [
            "Pyraclostrobin (Headline) or Azoxystrobin (Quadris).",
            "Propiconazole (Tilt) applied when 6+ pustules appear per leaf prior to silking."
        ],
        "prevention": "Plant resistant hybrids with Rp gene-mediated rust immunity; seed early in season."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Zea mays)",
        "disease_name": "Northern Corn Leaf Blight",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "severity": "High",
        "description": "Long, cigar-shaped grayish-green to tan lesions that coalesce and cause rapid canopy desiccation.",
        "symptoms": [
            "Elliptical, cigar-shaped lesions 2 to 15 cm long.",
            "Dark grayish fungal spore zones inside mature lesions.",
            "Extensive premature death of foliar tissue."
        ],
        "organic_remedies": [
            "Complete 2-year crop rotation out of corn.",
            "Thorough residue management and autumn tillage."
        ],
        "chemical_control": [
            "Stratego (propiconazole + trifloxystrobin) or Quilt Xcel.",
            "Foliar fungicide application when disease is present on the ear leaf or higher."
        ],
        "prevention": "Utilize corn hybrids possessing Ht resistance genes."
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Zea mays)",
        "disease_name": "Healthy Corn Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Broad, arching vibrant green maize leaf blade with robust midrib and zero pustules or necrotic striping.",
        "symptoms": ["Deep green linear leaf blade with intact parallel veins."],
        "organic_remedies": ["Maintain balanced nitrogen side-dressing and uniform soil moisture."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Follow routine field scouting protocol."
    },
    "Grape___Black_rot": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Grape Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "severity": "High",
        "description": "Devastating vineyard disease causing reddish-brown circular lesions on leaves and shriveled black mummified berries.",
        "symptoms": [
            "Reddish-brown circular spots with dark borders and tiny black fruiting pycnidia.",
            "Elongated black lesions on petioles and shoots.",
            "Grapes turn brown, shrivel into hard black mummies."
        ],
        "organic_remedies": [
            "Prune diseased vines and remove all mummified grape clusters.",
            "Apply copper sulfate or lime-sulfur sprays during early shoot development."
        ],
        "chemical_control": [
            "Mancozeb or Ziram applied from 1-inch shoot growth through bloom.",
            "Myclobutanil (Rally) or Tebuconazole post-infection eradication."
        ],
        "prevention": "Canopy management through shoot thinning and trellising for rapid leaf drying."
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Esca (Black Measles / Grape Dieback)",
        "pathogen": "Phaeoacremonium / Fomitiporia complex",
        "severity": "High",
        "description": "Complex vascular trunk disease causing interveinal tiger-stripe foliar chlorosis and berry dark spotting.",
        "symptoms": [
            "Interveinal chlorosis creating distinctive 'tiger-stripe' leaf patterns.",
            "Sudden summer apoplexy (complete vine wilting and drying within days).",
            "Small dark spots ('measles') on ripening grape berries."
        ],
        "organic_remedies": [
            "Paint fresh winter pruning wounds with bio-protectant Trichoderma formulations.",
            "Trunk renewal by training a healthy sucker from vine base."
        ],
        "chemical_control": [
            "No curative chemical fungicides exist for internal vascular trunk wood rot.",
            "Seal pruning wounds with wound sealants containing tebuconazole or pyraclostrobin."
        ],
        "prevention": "Prune late in the dormant season during dry weather; avoid making large pruning cuts."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Isariopsis Leaf Blight",
        "pathogen": "Pseudocercospora cladosporioides (Fungus)",
        "severity": "Moderate",
        "description": "Late-season foliar disease causing irregular dark reddish-brown spots with prominent dark borders.",
        "symptoms": [
            "Irregular necrotic brown lesions on older lower foliage.",
            "Velvety dark spore mass on lesion undersides in humid conditions.",
            "Premature defoliation reducing winter cane hardiness."
        ],
        "organic_remedies": [
            "Rake and bury fallen leaves during winter vineyard sanitation.",
            "Bordeaux mixture or copper oxychloride post-harvest spray."
        ],
        "chemical_control": [
            "Chlorothalonil or Mancozeb protective applications.",
            "Azoxystrobin rotation sprays."
        ],
        "prevention": "Ensure proper vine spacing and canopy airflow."
    },
    "Grape___healthy": {
        "crop": "Grape (Vitis vinifera)",
        "disease_name": "Healthy Grape Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Broad palmate green grape leaf with clean lobed edges and zero spots or tiger striping.",
        "symptoms": ["Uniform green palmate blade with vigorous tendril growth."],
        "organic_remedies": ["Maintain balanced potassium/magnesium vine nutrition."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Continue seasonal canopy maintenance."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange / Citrus (Citrus sinensis)",
        "disease_name": "Citrus Greening (Huanglongbing / HLB)",
        "pathogen": "Candidatus Liberibacter asiaticus (Bacterium)",
        "severity": "Critical",
        "description": "One of the most destructive citrus diseases worldwide, vectored by the Asian citrus psyllid; causes asymmetric leaf blotchy mottle.",
        "symptoms": [
            "Asymmetrical blotchy mottle chlorosis across the midvein.",
            "Yellow shoots and upright twig dieback.",
            "Small, lopsided fruit that remain green at the bottom and taste bitter."
        ],
        "organic_remedies": [
            "Release parasitoid wasps (Tamarixia radiata) for biological psyllid control.",
            "Apply foliar micronutrient cocktail (zinc, manganese, iron, boron) to prolong tree vigor."
        ],
        "chemical_control": [
            "Target insect vector: apply systemic neonicotinoids (imidacloprid) or spirotetramat.",
            "Oxytetracycline injection protocols where regulatory approvals allow."
        ],
        "prevention": "Plant certified disease-free nursery stock; immediately eradicate and burn infected trees."
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach (Prunus persica)",
        "disease_name": "Peach Bacterial Spot",
        "pathogen": "Xanthomonas arboricola pv. pruni (Bacterium)",
        "severity": "High",
        "description": "Bacterial pathogen causing water-soaked angular leaf spots that drop out ('shot-hole' effect) and cratered fruit.",
        "symptoms": [
            "Small angular purple-brown spots that dry and drop out leaving shot-holes.",
            "Severe yellowing of affected leaves starting at tips.",
            "Deep, oozing cracks and gumming on fruit surfaces."
        ],
        "organic_remedies": [
            "Apply fixed copper sprays during dormant season and bud swell.",
            "Avoid excessive summer pruning that stimulates susceptible succulent growth."
        ],
        "chemical_control": [
            "Oxytetracycline (Mycoshield) applied weekly during cover spray period.",
            "Copper bactericides at very low rates to avoid phytotoxicity."
        ],
        "prevention": "Plant tolerant cultivars (e.g., Candor, Dixired). Avoid sandy, drought-stressed soils."
    },
    "Peach___healthy": {
        "crop": "Peach (Prunus persica)",
        "disease_name": "Healthy Peach Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Slender lanceolate green peach foliage with intact finely serrated edges and zero shot-holes.",
        "symptoms": ["Lustrous lanceolate leaves with uniform green color and no gumming."],
        "organic_remedies": ["Apply composted mulch to conserve root zone moisture."],
        "chemical_control": ["No treatment required."],
        "prevention": "Follow routine fruit tree IPM monitoring."
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper (Capsicum annuum)",
        "disease_name": "Pepper Bacterial Spot",
        "pathogen": "Xanthomonas campestris pv. vesicatoria (Bacterium)",
        "severity": "High",
        "description": "Bacterial disease causing water-soaked lesions that turn dark brown with chlorotic halos, leading to catastrophic defoliation.",
        "symptoms": [
            "Small, irregular water-soaked spots on undersides of leaves.",
            "Spots turn necrotic brown with yellow halo; centers drop out.",
            "Sunscald on exposed fruit following rapid leaf drop."
        ],
        "organic_remedies": [
            "Apply copper octanoate (copper soap) or Bacillus subtilis sprays.",
            "Sterilize seed with hot water (50°C for 25 minutes) before planting."
        ],
        "chemical_control": [
            "Copper hydroxide mixed with Mancozeb (synergistic bactericidal combination).",
            "Actigard (acibenzolar-S-methyl) systemic acquired resistance inducer."
        ],
        "prevention": "Use certified disease-free seeds; avoid overhead irrigation; maintain 3-year crop rotation."
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper (Capsicum annuum)",
        "disease_name": "Healthy Bell Pepper Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Deep glossy green bell pepper leaf with intact smooth margin, strong turgor pressure, and zero necrotic spots.",
        "symptoms": ["Glossy, deep green leaf with clear venation and sturdy petiole."],
        "organic_remedies": ["Side-dress with balanced compost and bone meal."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Maintain regular watering and insect monitoring."
    },
    "Potato___Early_blight": {
        "crop": "Potato (Solanum tuberosum)",
        "disease_name": "Potato Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "severity": "High",
        "description": "Common foliar disease marked by concentric dark brown rings producing characteristic 'target board' lesions.",
        "symptoms": [
            "Circular to angular brown spots with distinctive concentric rings.",
            "Yellowing around older lesions on lower mature foliage.",
            "Premature vine dying and reduced tuber bulk size."
        ],
        "organic_remedies": [
            "Ensure adequate nitrogen fertility to prevent crop stress and senescence.",
            "Apply liquid copper or biofungicides (Bacillus amyloliquefaciens).",
            "Maintain wide plant spacing and drip irrigation."
        ],
        "chemical_control": [
            "Chlorothalonil (Bravo) or Mancozeb applied every 7-10 days.",
            "Azoxystrobin or Boscalid rotation during high humidity periods."
        ],
        "prevention": "Plant certified seed tubers; destroy volunteer potato plants; 3-year rotation away from nightshades."
    },
    "Potato___Late_blight": {
        "crop": "Potato (Solanum tuberosum)",
        "disease_name": "Potato Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Critical",
        "description": "Historical pathogen responsible for the Irish Potato Famine; causes rapid water-soaked black rot of leaves, stems, and tubers.",
        "symptoms": [
            "Water-soaked pale to dark olive-brown patches on leaves and stems.",
            "Delicate white fungal-like downy mold on leaf undersides in high humidity.",
            "Foul odor and total collapse of foliage within days."
        ],
        "organic_remedies": [
            "Copper hydroxide spray applied preventatively before rain events.",
            "Immediately destroy and bury heavily infected vines to halt spore release."
        ],
        "chemical_control": [
            "Mandipropamid (Revus) or Cymoxanil (Curzate) for targeted oomycete control.",
            "Mefenoxam / Metalaxyl systemic applications."
        ],
        "prevention": "Monitor late blight forecasting models; hill potatoes high to protect tubers from spores washed down."
    },
    "Potato___healthy": {
        "crop": "Potato (Solanum tuberosum)",
        "disease_name": "Healthy Potato Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Lush pinnate potato leaves with healthy green leaflets and vigorous vegetative vine development.",
        "symptoms": ["Dark green compound leaves with crisp edges and sturdy stems."],
        "organic_remedies": ["Maintain continuous soil moisture and hill up tuber rows."],
        "chemical_control": ["No treatment required."],
        "prevention": "Continue standard field scouting and weed control."
    },
    "Raspberry___healthy": {
        "crop": "Raspberry (Rubus idaeus)",
        "disease_name": "Healthy Raspberry Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Compound trifoliate raspberry leaf with pale pubescent undersides and rich green upper surface.",
        "symptoms": ["Serrated green leaflets with no chlorotic spotting or cane blight."],
        "organic_remedies": ["Mulch cane rows and trellis primocanes."],
        "chemical_control": ["No treatment required."],
        "prevention": "Prune out spent floricanes after fruiting."
    },
    "Soybean___healthy": {
        "crop": "Soybean (Glycine max)",
        "disease_name": "Healthy Soybean Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Trifoliate ovate soybean leaflets displaying active atmospheric nitrogen fixation and vibrant chlorophyll.",
        "symptoms": ["Uniform green trifoliate leaves without rust, frogeye spots, or mosaic mottling."],
        "organic_remedies": ["Inoculate seed with Bradyrhizobium japonicum."],
        "chemical_control": ["No treatment required."],
        "prevention": "Practice good field drainage and crop rotation."
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash / Cucurbit (Cucurbita pepo)",
        "disease_name": "Squash Powdery Mildew",
        "pathogen": "Podosphaera xanthii (Fungus)",
        "severity": "Moderate to High",
        "description": "Rapidly spreading white talc-like powdery fungal growth covering cucurbit leaf surfaces and petioles.",
        "symptoms": [
            "White powdery spots on both leaf surfaces and stems.",
            "Leaves turn yellow, brown, and become brittle ('paper-like').",
            "Premature leaf drop leading to sunburned squash fruits."
        ],
        "organic_remedies": [
            "Spray dilute milk solution (40% milk, 60% water) weekly in sunlight.",
            "Potassium bicarbonate or neem oil sprays applied at first sign."
        ],
        "chemical_control": [
            "Myclobutanil (Rally) or Quinoxyfen (Quintec).",
            "Triflumizole (Procure) rotation."
        ],
        "prevention": "Choose powdery mildew-resistant squash hybrids; avoid excessive nitrogen fertilizer."
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry (Fragaria × ananassa)",
        "disease_name": "Strawberry Leaf Scorch",
        "pathogen": "Diplocarpon earlianum (Fungus)",
        "severity": "Moderate",
        "description": "Fungal infection causing purple-to-dark brown irregular blotches that coalesce and make the leaf look scorched.",
        "symptoms": [
            "Numerous small, irregular purplish spots on upper leaf surfaces.",
            "Spots enlarge without white centers, turning leaves brown and scorched.",
            "Drying and curling of leaf margins."
        ],
        "organic_remedies": [
            "Remove and compost old infected leaves after post-harvest renovation.",
            "Apply copper-based fungicides early in the spring before flowering."
        ],
        "chemical_control": [
            "Captan or Thiram applied at 10-14 day intervals.",
            "Pyraclostrobin (Cabrio) rotation."
        ],
        "prevention": "Plant in raised beds with good drainage and clean straw mulch."
    },
    "Strawberry___healthy": {
        "crop": "Strawberry (Fragaria × ananassa)",
        "disease_name": "Healthy Strawberry Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Trifoliate dark green strawberry leaf with serrated edges, intact cuticle, and zero scorch lesions.",
        "symptoms": ["Crisp, deeply serrated green leaflets with vigorous crown growth."],
        "organic_remedies": ["Mulch with clean wheat straw and maintain drip lines."],
        "chemical_control": ["No treatment required."],
        "prevention": "Annual renovation and runner thinning."
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Bacterial Spot",
        "pathogen": "Xanthomonas perforans (Bacterium)",
        "severity": "High",
        "description": "Small, dark, water-soaked circular spots on leaves that develop yellow halos, leading to severe defoliation.",
        "symptoms": [
            "Small (less than 3mm) dark brown to black spots with yellow halos.",
            "Leaves turn brown, wither, and drop, exposing green tomatoes to sunscald.",
            "Black scabby raised specks on green fruits."
        ],
        "organic_remedies": [
            "Copper soap (copper octanoate) applied at early transplanting.",
            "Streptomyces lydicus bio-bactericide applications."
        ],
        "chemical_control": [
            "Copper hydroxide tank-mixed with Mancozeb.",
            "Acibenzolar-S-methyl (Actigard) to activate systemic plant defense."
        ],
        "prevention": "Use certified pathogen-free seed; avoid overhead sprinklers; sanitize stakes and cages."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "severity": "High",
        "description": "Classic foliar disease producing dark concentric target rings, surrounded by yellow chlorotic margins.",
        "symptoms": [
            "Concentric ring 'target-board' brown lesions starting on oldest lower foliage.",
            "Progressive yellowing and wilting from bottom of plant upward.",
            "Dark, sunken stem lesions and fruit rot at the calyx end."
        ],
        "organic_remedies": [
            "Prune lower foliage 12 inches off the ground to avoid soil splash.",
            "Apply copper fungicide or Bacillus subtilis every 7-10 days.",
            "Heavy straw or plastic mulch beneath tomato vines."
        ],
        "chemical_control": [
            "Chlorothalonil (Daconil) applied preventatively.",
            "Azoxystrobin (Quadris) or Difenoconazole for systemic protection."
        ],
        "prevention": "3-4 year nightshade crop rotation; stake and trellis plants for maximum airflow."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "severity": "Critical",
        "description": "Fast-moving aggressive blight causing large pale green to dark brown water-soaked blotches and white mycelium.",
        "symptoms": [
            "Large, irregularly shaped water-soaked greasy lesions on leaves and stems.",
            "White fuzzy sporulation on leaf undersides during cool, humid weather.",
            "Rapid collapse of foliage and greasy brown rot on green/ripe fruit."
        ],
        "organic_remedies": [
            "Copper fungicides applied before rainfall periods.",
            "Immediately bag and remove infected vines on dry days to halt airborne spores."
        ],
        "chemical_control": [
            "Mandipropamid (Revus), Cymoxanil (Curzate), or Fluopicolide (Presidio).",
            "Chlorothalonil protective barrier sprays."
        ],
        "prevention": "Plant late-blight resistant tomato varieties (e.g., Mountain Magic, Defiant, Iron Lady)."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Leaf Mold",
        "pathogen": "Passalora fulva (Fungus)",
        "severity": "Moderate to High",
        "description": "Common greenhouse and high-tunnel fungal infection causing pale green/yellow spots on top and olive-brown mold beneath.",
        "symptoms": [
            "Pale yellow spots on upper leaf surface with diffuse margins.",
            "Olive-green to velvety brown mold covering corresponding lower surface.",
            "Leaves curl, wither, and drop, severely reducing fruit set."
        ],
        "organic_remedies": [
            "Lower relative humidity below 85% by opening greenhouse vents and using exhaust fans.",
            "Biofungicides based on Trichoderma harzianum."
        ],
        "chemical_control": [
            "Chlorothalonil, Mancozeb, or Copper sulfate.",
            "Cyazofamid or Difenoconazole rotation."
        ],
        "prevention": "Maintain adequate plant spacing; water early in the day; choose resistant tomato hybrids with Cf genes."
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Septoria Leaf Spot",
        "pathogen": "Septoria lycopersici (Fungus)",
        "severity": "High",
        "description": "Numerous small circular spots with grayish-white centers and dark brown borders, dotted with black pycnidia specks.",
        "symptoms": [
            "Dense 1.5-3mm circular lesions with distinct dark borders and light centers.",
            "Tiny black specks (pycnidia) clearly visible in center of spots.",
            "Progressive bottom-up leaf yellowing and severe defoliation."
        ],
        "organic_remedies": [
            "Strip bottom leaves showing first spots and disinfect hands.",
            "Spray copper hydroxide or potassium bicarbonate.",
            "Thick layer of pine straw mulch to eliminate rain splash transmission."
        ],
        "chemical_control": [
            "Chlorothalonil or Mancozeb applied every 7-10 days from early July.",
            "Quadris Top (azoxystrobin + difenoconazole)."
        ],
        "prevention": "Never work among tomato plants when leaves are wet; practice 3-year crop rotation."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Two-spotted Spider Mite Infestation",
        "pathogen": "Tetranychus urticae (Arachnid Pest)",
        "severity": "High",
        "description": "Microscopic piercing pests that feed on plant sap, causing yellow stippling, bronze foliage, and extensive fine webbing.",
        "symptoms": [
            "Fine yellow/white stippling (speckling) across upper leaf surfaces.",
            "Fine silken webbing on undersides of leaves and growing tips.",
            "Leaves turn bronze, dry out, and drop prematurely."
        ],
        "organic_remedies": [
            "Release predatory mites (Phytoseiulus persimilis or Neoseiulus californicus).",
            "Apply insecticidal soap or horticultural neem oil, thoroughly spraying leaf undersides.",
            "Strong blast of cold water on leaf undersides to dislodge mites."
        ],
        "chemical_control": [
            "Abamectin (Agri-Mek) or Bifenazate (Acramite) targeted miticides.",
            "Avoid broad-spectrum synthetic pyrethroids which kill beneficial predatory mites."
        ],
        "prevention": "Keep plants well-watered (drought stress accelerates mite reproduction); control dust on field roads."
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Target Spot",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "severity": "Moderate to High",
        "description": "Warm-weather fungal disease causing pinpoint brown lesions that expand into circular brown spots with faint concentric rings.",
        "symptoms": [
            "Pinpoint brown spots on leaves that expand to 10-12 mm.",
            "Concentric rings and chlorotic yellow halos surrounding spots.",
            "Sunken target-like circular lesions with dark centers on ripe fruit."
        ],
        "organic_remedies": [
            "Improve air circulation through trellising and sucker pruning.",
            "Apply copper octanoate or Bacillus amyloliquefaciens."
        ],
        "chemical_control": [
            "Chlorothalonil or Mancozeb protective applications.",
            "Boscalid (Endura) or Pyraclostrobin."
        ],
        "prevention": "Remove solanaceous weed hosts (e.g., black nightshade); rotate crops regularly."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Begomovirus (Vectored by Whitefly - Bemisia tabaci)",
        "severity": "Critical",
        "description": "Destructive viral disease transmitted by silverleaf whiteflies, causing extreme upward leaf cupping, chlorosis, and stunted growth.",
        "symptoms": [
            "Pronounced upward curling and cupping of leaflet margins.",
            "Severe interveinal chlorosis (yellowing) on youngest leaves.",
            "Extreme plant stunting and flower abortion resulting in near-total yield loss."
        ],
        "organic_remedies": [
            "Install fine 50-mesh insect netting in greenhouses and tunnels.",
            "Deploy yellow sticky traps to monitor and trap whitefly populations.",
            "Apply insecticidal soap or Beauveria bassiana entomopathogenic fungus."
        ],
        "chemical_control": [
            "Target whitefly vector: Dinotefuran (Venom) or Spiromesifen (Oberon).",
            "Pyriproxyfen (Knack) insect growth regulator."
        ],
        "prevention": "Plant TYLCV-resistant hybrids with Ty genes (e.g., Tycoon, Charger); immediately rogue out infected plants in sealed bags."
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "pathogen": "Tobamovirus (Mechanically Transmitted)",
        "severity": "High",
        "description": "Extremely stable, mechanically transmissible virus causing light and dark green mosaic mottling and leaf distortion.",
        "symptoms": [
            "Mottled light and dark green patterns on leaves.",
            "Distorted, blistered, or narrow strap-like 'shoestring' leaves.",
            "Internal brown browning in fruit walls and uneven ripening."
        ],
        "organic_remedies": [
            "Wash hands and dip tools in 20% non-fat dry milk solution before handling plants.",
            "Prohibit tobacco use near tomatoes (tobacco transmits tobamoviruses)."
        ],
        "chemical_control": [
            "No chemical viricides exist to cure systemic viral plant infections.",
            "Apply milk sprays on seedlings prior to transplanting to reduce mechanical transmission."
        ],
        "prevention": "Use certified virus-free seed; plant resistant cultivars (marked with 'T' or 'ToMV'); rogue out infected plants."
    },
    "Tomato___healthy": {
        "crop": "Tomato (Solanum lycopersicum)",
        "disease_name": "Healthy Tomato Foliage",
        "pathogen": "None (Healthy)",
        "severity": "None",
        "description": "Lush, serrated compound tomato leaf displaying rich dark-green chlorophyll pigmentation, optimal glandular trichomes, and zero necrotic lesions.",
        "symptoms": ["Vibrant green foliage with crisp serrated margins and robust turgidity."],
        "organic_remedies": ["Maintain regular drip irrigation and mulch to sustain soil moisture."],
        "chemical_control": ["No chemical treatment required."],
        "prevention": "Continue standard preventative scouting, trellising, and crop rotation."
    }
}


def get_disease_info(raw_class_name: str) -> dict:
    """
    Retrieves the clinical disease record for a given class identifier.
    Falls back gracefully if an unmapped category is requested.
    """
    clean_name = normalize_class_name(raw_class_name)
    
    if clean_name in DISEASE_INFO:
        return DISEASE_INFO[clean_name]
        
    # Attempt substring or case-insensitive matching
    for k, v in DISEASE_INFO.items():
        if k.lower() == clean_name.lower():
            return v
            
    # Fallback generic record
    crop_guess = clean_name.split("___")[0].replace("_", " ").title() if "___" in clean_name else "Unknown Botanical"
    disease_guess = clean_name.split("___")[1].replace("_", " ").title() if "___" in clean_name else clean_name
    
    return {
        "crop": crop_guess,
        "disease_name": disease_guess,
        "pathogen": "Unspecified Plant Pathogen",
        "severity": "Moderate",
        "description": f"Foliar pathology detection associated with {disease_guess} in {crop_guess} host.",
        "symptoms": ["Foliar discoloration and visible symptomatic lesion spots."],
        "organic_remedies": [
            "Prune infected foliage and dispose of safely.",
            "Ensure adequate ventilation, sunlight, and avoid wetting foliage."
        ],
        "chemical_control": [
            "Consult localized agricultural extension service for registered fungicides/bactericides."
        ],
        "prevention": "Practice good crop hygiene, certified seed selection, and preventative rotation."
    }
