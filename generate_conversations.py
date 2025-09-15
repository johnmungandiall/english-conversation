import os

# List of 1000 unique topics
topics = [
    "Hobbies", "Travel", "Sports", "Music", "Movies", "Books", "Technology", "Health", "Education", "Career",
    "Family", "Friends", "Weather", "Food", "Drinks", "Shopping", "Games", "Art", "Nature", "Animals",
    "Cooking", "Gardening", "Photography", "Dancing", "Singing", "Painting", "Writing", "Reading", "Swimming", "Running",
    "Cycling", "Hiking", "Camping", "Fishing", "Hunting", "Chess", "Poker", "Video Games", "Board Games", "Card Games",
    "Puzzles", "Magic", "Comedy", "Drama", "Romance", "Science Fiction", "Fantasy", "Horror", "Thriller", "Mystery",
    "History", "Geography", "Mathematics", "Physics", "Chemistry", "Biology", "Astronomy", "Geology", "Psychology", "Sociology",
    "Philosophy", "Religion", "Politics", "Economics", "Business", "Marketing", "Sales", "Finance", "Accounting", "Law",
    "Medicine", "Engineering", "Architecture", "Design", "Fashion", "Beauty", "Fitness", "Yoga", "Meditation", "Mindfulness",
    "Spirituality", "Volunteering", "Charity", "Environment", "Climate Change", "Recycling", "Sustainability", "Renewable Energy",
    "Electric Vehicles", "Space Exploration", "Artificial Intelligence", "Robotics", "Blockchain", "Cryptocurrency", "Social Media", "Internet",
    "Cybersecurity", "Programming", "Data Science", "Machine Learning",
    "Favorite Hobbies", "Travel Destinations", "Sports Teams", "Music Genres", "Movie Genres", "Book Genres", "Tech Gadgets", "Healthy Eating",
    "Online Education", "Job Interviews", "Family Vacations", "Best Friends", "Weather Forecasting", "Street Food", "Coffee Shops", "Online Shopping",
    "Mobile Games", "Street Art", "Wildlife Conservation", "Pet Care", "Baking", "Indoor Plants", "Digital Photography", "Ballet Dancing",
    "Karaoke Singing", "Oil Painting", "Creative Writing", "Audiobooks", "Beach Swimming", "Marathon Running", "Mountain Biking", "Forest Hiking",
    "RV Camping", "Fly Fishing", "Deer Hunting", "Online Chess", "Texas Hold'em Poker", "RPG Video Games", "Strategy Board Games", "Solitaire Card Games",
    "Crossword Puzzles", "Card Magic", "Stand-up Comedy", "Shakespeare Drama", "Romantic Novels", "Sci-Fi Movies", "Fantasy Books", "Horror Stories",
    "Crime Thrillers", "Detective Mysteries", "Ancient History", "World Geography", "Algebra Mathematics", "Quantum Physics", "Organic Chemistry",
    "Marine Biology", "Black Hole Astronomy", "Volcanic Geology", "Clinical Psychology", "Urban Sociology", "Eastern Philosophy", "World Religions",
    "Political Debates", "Global Economics", "Startup Business", "Digital Marketing", "Retail Sales", "Investment Finance", "Tax Accounting",
    "Criminal Law", "Pediatric Medicine", "Civil Engineering", "Modern Architecture", "Graphic Design", "High Fashion", "Skincare Beauty",
    "Crossfit Fitness", "Hot Yoga", "Guided Meditation", "Positive Mindfulness", "Spiritual Retreats", "Community Volunteering", "Animal Charity",
    "Ocean Environment", "Global Warming", "Plastic Recycling", "Green Sustainability", "Solar Energy", "Hydrogen Vehicles", "Mars Exploration",
    "Neural Networks", "Industrial Robotics", "Bitcoin Blockchain", "NFT Cryptocurrency", "Instagram Social Media", "5G Internet", "Hacking Cybersecurity",
    "Web Programming", "Big Data Science", "Deep Learning",
    "Weekend Hobbies", "International Travel", "Olympic Sports", "Classical Music", "Action Movies", "Mystery Books", "Smart Technology", "Mental Health",
    "Higher Education", "Career Changes", "Nuclear Family", "Childhood Friends", "Tropical Weather", "Italian Food", "Craft Beer", "Black Friday Shopping",
    "Arcade Games", "Abstract Art", "National Parks", "Endangered Animals", "Vegan Cooking", "Rose Gardening", "Portrait Photography", "Hip Hop Dancing",
    "Opera Singing", "Watercolor Painting", "Poetry Writing", "E-books", "Pool Swimming", "Trail Running", "BMX Cycling", "Rock Climbing",
    "Glamping Camping", "Bass Fishing", "Duck Hunting", "Speed Chess", "Blackjack Poker", "MOBA Video Games", "Euro Board Games", "Bridge Card Games",
    "Sudoku Puzzles", "Illusion Magic", "Sketch Comedy", "Musical Drama", "Historical Romance", "Cyberpunk Fiction", "Epic Fantasy", "Zombie Horror",
    "Spy Thrillers", "Whodunit Mysteries", "Medieval History", "Physical Geography", "Geometry Mathematics", "Thermodynamics Physics", "Biochemistry",
    "Genetics Biology", "Exoplanet Astronomy", "Earthquake Geology", "Forensic Psychology", "Criminology Sociology", "Existential Philosophy",
    "Comparative Religion", "Election Politics", "Macroeconomics", "E-commerce Business", "Content Marketing", "B2B Sales", "Real Estate Finance",
    "Auditing Accounting", "Constitutional Law", "Surgery Medicine", "Software Engineering", "Sustainable Architecture", "UX Design", "Street Fashion",
    "Cosmetic Beauty", "Bodybuilding Fitness", "Vinyasa Yoga", "Transcendental Meditation", "Spiritual Awakening", "Disaster Volunteering",
    "Wildlife Charity", "Forest Environment", "Carbon Footprint", "Composting Recycling", "Eco Sustainability", "Wind Energy", "Autonomous Vehicles",
    "Lunar Exploration", "Computer Vision", "Service Robotics", "Ethereum Blockchain", "DeFi Cryptocurrency", "TikTok Social Media", "IoT Internet",
    "Ethical Hacking", "Mobile Programming", "Predictive Analytics", "Reinforcement Learning",
    "Creative Hobbies", "Adventure Travel", "Extreme Sports", "Jazz Music", "Horror Movies", "Biography Books", "Wearable Technology", "Holistic Health",
    "Distance Education", "Freelance Career", "Blended Family", "Online Friends", "Arctic Weather", "Mexican Food", "Wine Tasting", "Luxury Shopping",
    "Puzzle Games", "Sculpture Art", "Desert Nature", "Farm Animals", "Grilling Cooking", "Vegetable Gardening", "Aerial Photography", "Tango Dancing",
    "Gospel Singing", "Acrylic Painting", "Screenwriting", "Graphic Novels", "Open Water Swimming", "Ultra Running", "Downhill Cycling", "Ice Climbing",
    "Backpacking Camping", "Sport Fishing", "Turkey Hunting", "Bullet Chess", "Casino Poker", "Battle Royale Games", "Wargame Board Games",
    "Magic Card Games", "Jigsaw Puzzles", "Stage Magic", "Dark Comedy", "Tragedy Drama", "Gothic Romance", "Space Opera Fiction", "Urban Fantasy",
    "Psychological Horror", "Legal Thrillers", "Cozy Mysteries", "Renaissance History", "Human Geography", "Calculus Mathematics", "Nuclear Physics",
    "Analytical Chemistry", "Evolutionary Biology", "Cosmic Astronomy", "Plate Tectonics Geology", "Cognitive Psychology", "Social Sociology",
    "Moral Philosophy", "Abrahamic Religions", "Foreign Politics", "Development Economics", "Corporate Business", "SEO Marketing", "Direct Sales",
    "Cryptocurrency Finance", "Forensic Accounting", "International Law", "Cardiology Medicine", "Mechanical Engineering", "Bauhaus Architecture",
    "Product Design", "Couture Fashion", "Organic Beauty", "Marathon Fitness", "Ashtanga Yoga", "Mindfulness Meditation", "Spiritual Journeys",
    "Humanitarian Volunteering", "Cancer Charity", "Urban Environment", "Deforestation", "E-waste Recycling", "Circular Sustainability",
    "Geothermal Energy", "Flying Cars", "Asteroid Mining", "Quantum Computing", "Autonomous Robotics", "Smart Contracts", "Stablecoin Cryptocurrency",
    "LinkedIn Social Media", "Quantum Internet", "Data Privacy", "Game Programming", "Natural Language Processing", "Computer Vision AI",
    "DIY Hobbies", "Luxury Travel", "Water Sports", "Rock Music", "Comedy Movies", "Self-Help Books", "AI Technology", "Preventive Health",
    "Vocational Education", "Entrepreneur Career", "Single Parent Family", "Pen Pal Friends", "Monsoon Weather", "Chinese Food", "Tea Culture",
    "Vintage Shopping", "Strategy Games", "Digital Art", "Mountain Nature", "Exotic Animals", "Slow Cooking", "Hydroponic Gardening",
    "Macro Photography", "Salsa Dancing", "Pop Singing", "Charcoal Drawing", "Journalism Writing", "Podcasts", "Synchronized Swimming",
    "Obstacle Running", "Freestyle Cycling", "Cave Exploration", "Survival Camping", "Ice Fishing", "Pheasant Hunting", "Correspondence Chess",
    "Video Poker", "MMORPG Games", "Abstract Board Games", "Tarot Card Games", "Logic Puzzles", "Mentalism Magic", "Satire Comedy",
    "Modern Drama", "Paranormal Romance", "Military Sci-Fi", "High Fantasy", "Body Horror", "Techno Thrillers", "Noir Mysteries",
    "Colonial History", "Economic Geography", "Statistics Mathematics", "Particle Physics", "Physical Chemistry", "Microbiology Biology",
    "Stellar Astronomy", "Mineral Geology", "Behavioral Psychology", "Rural Sociology", "Political Philosophy", "Eastern Religions",
    "Domestic Politics", "Behavioral Economics", "Small Business", "Influencer Marketing", "Telemarketing Sales", "Venture Finance",
    "Management Accounting", "Environmental Law", "Neurology Medicine", "Electrical Engineering", "Gothic Architecture", "Interior Design",
    "Athleisure Fashion", "Natural Beauty", "Powerlifting Fitness", "Bikram Yoga", "Vipassana Meditation", "Spiritual Practices",
    "Refugee Volunteering", "Education Charity", "Polar Environment", "Air Pollution", "Metal Recycling", "Social Sustainability",
    "Tidal Energy", "Hyperloop Vehicles", "Space Tourism", "Machine Learning AI", "Collaborative Robotics", "Decentralized Finance",
    "Altcoin Cryptocurrency", "YouTube Social Media", "Satellite Internet", "Network Security", "Embedded Programming", "Data Mining",
    "Supervised Learning",
    "Artistic Hobbies", "Cultural Travel", "Winter Sports", "Electronic Music", "Documentary Movies", "Fiction Books", "IoT Technology",
    "Wellness Health", "Adult Education", "Corporate Career", "Foster Family", "Virtual Friends", "Desert Weather", "French Food", "Cocktail Bars",
    "Antique Shopping", "Simulation Games", "Performance Art", "Coastal Nature", "Aquatic Animals", "Fusion Cooking", "Urban Gardening",
    "Drone Photography", "Ballroom Dancing", "Country Singing", "Pastel Painting", "Technical Writing", "Webcomics", "Diving Swimming",
    "Ski Running", "Moto Cycling", "Mountain Climbing", "Tent Camping", "Fly Fishing", "Quail Hunting", "Blind Chess", "Online Poker",
    "Sandbox Games", "Thematic Board Games", "Collectible Card Games", "Math Puzzles", "Close-up Magic", "Romantic Comedy", "Absurdist Drama",
    "Time Travel Romance", "Hard Sci-Fi", "Dark Fantasy", "Splatter Horror", "Political Thrillers", "Locked Room Mysteries",
    "Industrial Revolution History", "Cultural Geography", "Discrete Mathematics", "Relativity Physics", "Inorganic Chemistry",
    "Botany Biology", "Radio Astronomy", "Sedimentary Geology", "Developmental Psychology", "Demographic Sociology", "Ethics Philosophy",
    "Indigenous Religions", "Global Politics", "Labor Economics", "Retail Business", "Email Marketing", "Inside Sales", "Banking Finance",
    "Cost Accounting", "Property Law", "Dermatology Medicine", "Chemical Engineering", "Brutalist Architecture", "Fashion Design",
    "Vintage Fashion", "Wellness Beauty", "Calisthenics Fitness", "Yin Yoga", "Loving-Kindness Meditation", "Spiritual Beliefs",
    "Environmental Volunteering", "Health Charity", "Arctic Environment", "Water Pollution", "Paper Recycling", "Economic Sustainability",
    "Fusion Energy", "Drone Vehicles", "Orbital Exploration", "Natural Language AI", "Humanoid Robotics", "Tokenization Blockchain",
    "Meme Cryptocurrency", "Twitter Social Media", "Fiber Internet", "Cloud Security", "Frontend Programming", "Data Visualization",
    "Unsupervised Learning",
    "Crafts Hobbies", "Backpacking Travel", "Motor Sports", "Hip Hop Music", "Animated Movies", "Poetry Books", "VR Technology",
    "Alternative Health", "Special Education", "Tech Career", "Adoptive Family", "Gaming Friends", "Tundra Weather", "Indian Food",
    "Brewpub Bars", "Thrift Shopping", "Racing Games", "Installation Art", "Island Nature", "Reptile Animals", "Molecular Cooking",
    "Container Gardening", "Time-lapse Photography", "Flamenco Dancing", "Blues Singing", "Ink Painting", "Copywriting", "Fan Fiction",
    "Scuba Diving", "Nordic Skiing", "Enduro Cycling", "Rock Climbing", "Car Camping", "Deep Sea Fishing", "Elk Hunting", "Rapid Chess",
    "Tournament Poker", "RTS Games", "Party Board Games", "Trading Card Games", "Word Puzzles", "Escape Magic", "Slapstick Comedy",
    "Epic Drama", "Enemies to Lovers Romance", "Post-Apocalyptic Sci-Fi", "Mythic Fantasy", "Cosmic Horror", "Espionage Thrillers",
    "Historical Mysteries", "Victorian Era History", "Political Geography", "Number Theory Mathematics", "Astrophysics", "Polymer Chemistry",
    "Ecology Biology", "Observational Astronomy", "Igneous Geology", "Social Psychology", "Urban Sociology", "Aesthetics Philosophy",
    "New Age Religions", "International Politics", "Environmental Economics", "Manufacturing Business", "Social Media Marketing",
    "Field Sales", "Insurance Finance", "Financial Accounting", "Tort Law", "Oncology Medicine", "Aerospace Engineering", "Art Deco Architecture",
    "Industrial Design", "Haute Couture", "Therapeutic Beauty", "Functional Fitness", "Restorative Yoga", "Mantra Meditation",
    "Spiritual Retreats", "Community Service Volunteering", "Arts Charity", "Desert Environment", "Soil Pollution", "Glass Recycling",
    "Cultural Sustainability", "Nuclear Energy", "Self-Driving Cars", "Satellite Exploration", "Expert Systems AI", "Surgical Robotics",
    "Layer 2 Blockchain", "Privacy Cryptocurrency", "Reddit Social Media", "Wireless Internet", "Application Security", "Backend Programming",
    "Machine Translation", "Generative AI",
    "Collecting Hobbies", "Road Trip Travel", "Combat Sports", "Reggae Music", "Superhero Movies", "Classic Books", "Quantum Technology",
    "Integrative Health", "Language Education", "Startup Career", "Military Family", "School Friends", "Savanna Weather", "Japanese Food",
    "Speakeasy Bars", "Designer Shopping", "Fighting Games", "Land Art", "River Nature", "Insect Animals", "Experimental Cooking",
    "Vertical Gardening", "Wildlife Photography", "Irish Dancing", "Folk Singing", "Spray Painting", "Blog Writing", "Vlogs", "Snorkeling",
    "Cross-Country Skiing", "Gravel Cycling", "Bouldering", "Yurt Camping", "Saltwater Fishing", "Moose Hunting", "Chess Variants",
    "Poker Tournaments", "Survival Games", "Dexterity Board Games", "Deck Building Games", "Riddle Puzzles", "Street Magic", "Black Comedy",
    "Tragic Drama", "Forbidden Romance", "Alternate History Sci-Fi", "Sword and Sorcery Fantasy", "Lovecraftian Horror", "Conspiracy Thrillers",
    "Golden Age Mysteries", "Ancient Civilizations History", "Regional Geography", "Applied Mathematics", "Condensed Matter Physics",
    "Environmental Chemistry", "Immunology Biology", "Galactic Astronomy", "Structural Geology", "Personality Psychology", "Cultural Sociology",
    "Metaphysics Philosophy", "Mystic Religions", "Local Politics", "Agricultural Economics", "Service Business", "Affiliate Marketing",
    "Consultative Sales", "Mortgage Finance", "Tax Accounting", "Contract Law", "Psychiatry Medicine", "Biomedical Engineering",
    "Postmodern Architecture", "Automotive Design", "Ready-to-Wear Fashion", "Anti-Aging Beauty", "High-Intensity Fitness", "Kundalini Yoga",
    "Zen Meditation", "Spiritual Enlightenment", "Youth Volunteering", "Science Charity", "Grassland Environment", "Noise Pollution",
    "Textile Recycling", "Biodiversity Sustainability", "Biomass Energy", "Electric Bikes", "Underwater Exploration", "Speech Recognition AI",
    "Agricultural Robotics", "Cross-Chain Blockchain", "Central Bank Cryptocurrency", "Facebook Social Media", "Broadband Internet",
    "Endpoint Security", "Full-Stack Programming", "Business Intelligence", "Conversational AI",
    "Model Hobbies", "Cruise Travel", "Team Sports", "Pop Music", "Romance Movies", "Adventure Books", "Nanotechnology", "Public Health",
    "STEM Education", "Gig Economy Career", "Extended Family", "Long-Distance Friends", "Rainforest Weather", "Thai Food", "Juice Bars",
    "Outlet Shopping", "Platform Games", "Video Art", "Canyon Nature", "Bird Animals", "Gourmet Cooking", "Rooftop Gardening",
    "Street Photography", "Waltz Dancing", "Soul Singing", "Mosaic Art", "Content Writing", "Podcasting", "Free Diving", "Alpine Skiing",
    "Touring Cycling", "Sport Climbing", "Cabin Camping", "Lake Fishing", "Bear Hunting", "Chess Openings", "Poker Blinds", "Shooter Games",
    "Trick-Taking Board Games", "Living Card Games", "Brain Teasers", "Comedy Magic", "Parody Comedy", "Melodrama", "Slow Burn Romance",
    "Dystopian Sci-Fi", "Grimdark Fantasy", "Survival Horror", "Action Thrillers", "Puzzle Mysteries", "World War History",
    "Urban Geography", "Pure Mathematics", "High Energy Physics", "Medicinal Chemistry", "Neuroscience Biology", "Solar System Astronomy",
    "Hydrology Geology", "Educational Psychology", "Sociology of Education", "Logic Philosophy", "Shamanic Religions", "State Politics",
    "International Economics", "Hospitality Business", "Video Marketing", "Solution Sales", "Wealth Management Finance", "GAAP Accounting",
    "Corporate Law", "Radiology Medicine", "Environmental Engineering", "Minimalist Architecture", "Jewelry Design", "Casual Fashion",
    "Spa Beauty", "Cardio Fitness", "Hatha Yoga", "Breathwork Meditation", "Spiritual Growth", "Elderly Volunteering", "Literacy Charity",
    "Wetland Environment", "Light Pollution", "Battery Recycling", "Community Sustainability", "Hydroelectric Energy", "Maglev Trains",
    "Deep Sea Exploration", "Computer Graphics AI", "Domestic Robotics", "Proof of Stake Blockchain", "Digital Currency", "Snapchat Social Media",
    "Mesh Internet", "Zero Trust Security", "DevOps Programming", "Data Warehousing", "Recommendation Systems",
    "Building Hobbies", "Safari Travel", "Individual Sports", "Country Music", "Thriller Movies", "Non-Fiction Books", "Biotechnology",
    "Occupational Health", "Liberal Arts Education", "Remote Career", "Step Family", "Social Friends", "Volcanic Weather", "Korean Food",
    "Wine Bars", "Department Store Shopping", "Adventure Games", "Body Art", "Valley Nature", "Mammal Animals", "Farm-to-Table Cooking",
    "Herb Gardening", "Event Photography", "Swing Dancing", "R&B Singing", "Graffiti Art", "SEO Writing", "Streaming", "Kayaking", "Snowboarding",
    "Road Cycling", "Traditional Climbing", "Primitive Camping", "River Fishing", "Boar Hunting", "Chess Endgames", "Poker Tells",
    "Platformer Games", "Auction Board Games", "Customizable Card Games", "Lateral Thinking Puzzles", "Illusion Magic", "Wit Comedy",
    "Soap Opera Drama", "Fake Dating Romance", "Steampunk Sci-Fi", "Low Fantasy", "Gothic Horror", "Military Thrillers", "Whodunit Mysteries",
    "Cold War History", "Economic Geography", "Computational Mathematics", "Plasma Physics", "Forensic Chemistry", "Cell Biology",
    "Interstellar Astronomy", "Glacial Geology", "Positive Psychology", "Sociology of Religion", "Philosophy of Mind", "Pagan Religions",
    "Federal Politics", "Monetary Economics", "Food Service Business", "Podcast Marketing", "Account Management Sales", "Pension Finance",
    "International Accounting", "Intellectual Property Law", "Anesthesiology Medicine", "Petroleum Engineering", "Colonial Architecture",
    "Textile Design", "Sportswear Fashion", "Mineral Beauty", "Strength Training Fitness", "Iyengar Yoga", "Visualization Meditation",
    "Spiritual Healing", "Animal Volunteering", "Disability Charity", "Coral Reef Environment", "Thermal Pollution", "Electronic Recycling",
    "Urban Sustainability", "Ocean Energy", "Bullet Trains", "Suborbital Exploration", "Image Recognition AI", "Entertainment Robotics",
    "Sidechains Blockchain", "CBDC Cryptocurrency", "Pinterest Social Media", "Li-Fi Internet", "Cyber Threat Intelligence",
    "AI Programming", "Data Engineering", "Autonomous Systems",
    "Restoration Hobbies", "Eco Travel", "Equestrian Sports", "Blues Music", "Mystery Movies", "Historical Books", "5G Technology",
    "Reproductive Health", "Early Childhood Education", "Consulting Career", "Grandparent Family", "Work Friends", "Mountain Weather",
    "Vietnamese Food", "Coffee Bars", "Mall Shopping", "Role-Playing Games", "Mixed Media Art", "Lake Nature", "Amphibian Animals",
    "Sous Vide Cooking", "Bonsai Gardening", "Fashion Photography", "Latin Dancing", "Jazz Singing", "Sand Art", "Grant Writing",
    "YouTube Channels", "Canoeing", "Ice Skating", "Track Cycling", "Ice Climbing", "Treehouse Camping", "Trout Fishing", "Lion Hunting",
    "Chess Tactics", "Poker Odds", "Fighting Games", "Negotiation Board Games", "Strategy Card Games", "Cryptic Puzzles", "Hypnotism Magic",
    "Improvisational Comedy", "Farce Drama", "Second Chance Romance", "Time Loop Sci-Fi", "Fairy Tale Fantasy", "Psychological Horror",
    "Heist Thrillers", "Courtroom Mysteries", "Revolutionary History", "Climatic Geography", "Algebraic Geometry", "String Theory Physics",
    "Quantum Chemistry", "Synthetic Biology", "Neutron Star Astronomy", "Oceanic Geology", "Abnormal Psychology", "Sociology of Gender",
    "Philosophy of Language", "Animist Religions", "Parliamentary Politics", "Trade Economics", "Logistics Business", "Guerrilla Marketing",
    "Channel Sales", "Derivatives Finance", "Sustainability Accounting", "Human Rights Law", "Pathology Medicine", "Mining Engineering",
    "Victorian Architecture", "Ceramic Design", "Lingerie Fashion", "Ayurvedic Beauty", "Endurance Fitness", "Anusara Yoga", "Contemplative Meditation",
    "Spiritual Guidance", "Homeless Volunteering", "Hunger Charity", "Mangrove Environment", "Chemical Pollution", "Automotive Recycling",
    "Energy Sustainability", "Pumped Storage", "Personal Aircraft", "Planetary Exploration", "Voice AI", "Warehouse Robotics",
    "Directed Acyclic Graph Blockchain", "Utility Cryptocurrency", "Tumblr Social Media", "Quantum Internet", "Blockchain Security",
    "Quantum Programming", "Data Analytics", "Swarm Intelligence",
    "Painting Hobbies", "Historical Travel", "Martial Arts", "Folk Music", "Western Movies", "Philosophy Books", "AR Technology",
    "Sexual Health", "Special Needs Education", "Law Career", "Same-Sex Family", "Book Club Friends", "Coastal Weather", "Greek Food",
    "Beer Bars", "Boutique Shopping", "MMO Games", "Conceptual Art", "Forest Nature", "Fish Animals", "Fermentation Cooking",
    "Orchid Gardening", "Product Photography", "Square Dancing", "Rock Singing", "Calligraphy Art", "PR Writing", "Livestreaming",
    "Rafting", "Figure Skating", "BMX Cycling", "Aid Climbing", "Hammock Camping", "Catfish Fishing", "Wolf Hunting", "Chess Strategy",
    "Poker Psychology", "Action Games", "Worker Placement Board Games", "Engine Building Games", "Paradox Puzzles", "Ventriloquism Magic",
    "Stand-Up Comedy", "One-Act Drama", "Love Triangle Romance", "Parallel Universe Sci-Fi", "Heroic Fantasy", "Supernatural Horror",
    "Suspense Thrillers", "Amateur Sleuth Mysteries", "Enlightenment History", "Population Geography", "Topology Mathematics",
    "Optics Physics", "Catalysis Chemistry", "Virology Biology", "Pulsar Astronomy", "Desert Geology", "Motivational Psychology",
    "Sociology of Deviance", "Philosophy of Science", "Fundamentalist Religions", "Presidential Politics", "Fiscal Economics",
    "Construction Business", "Native Advertising", "Enterprise Sales", "Forex Finance", "Environmental Accounting", "Family Law",
    "Endocrinology Medicine", "Nuclear Engineering", "Renaissance Architecture", "Glass Design", "Shoe Fashion", "Holistic Beauty",
    "Flexibility Fitness", "Jivamukti Yoga", "Metta Meditation", "Spiritual Discipline", "Prison Volunteering", "Peace Charity",
    "Tundra Environment", "Radiation Pollution", "Construction Recycling", "Waste Sustainability", "Compressed Air Energy",
    "Delivery Drones", "Exoplanet Exploration", "Emotion AI", "Medical Robotics", "Hashgraph Blockchain", "Fan Token Cryptocurrency",
    "Discord Social Media", "6G Internet", "Homomorphic Encryption", "Blockchain Programming", "Data Science Platforms",
    "Cognitive Computing"
]

# Base conversation template with TOPIC placeholder
base_conversation = [
    ("John", "Hey Giri, what do you think about TOPIC?", "Hey Giri, TOPIC గురించి నీ అభిప్రాయం ఏంటి?"),
    ("Giri", "I think TOPIC is interesting. What about you?", "నేను TOPIC ఇంటరెస్టింగ్ అనుకుంటున్నా. నువ్వు?"),
    ("John", "I like TOPIC too. It's fun.", "నాకు కూడా TOPIC ఇష్టం. ఇది ఫన్."),
    ("Giri", "Do you have any experience with TOPIC?", "నీకు TOPIC తో ఎనీ ఎక్స్పీరియన్స్ ఉందా?"),
    ("John", "Yes, I do. It's amazing.", "అవును, ఉంది. ఇది అమేజింగ్."),
    ("Giri", "We should try TOPIC together sometime.", "మనం TOPIC కలిసి ట్రై చేద్దాం ఎప్పుడైనా."),
    ("John", "Sounds good. When?", "బాగుంది. ఎప్పుడు?"),
    ("Giri", "Maybe this weekend.", "బహుశా ఈ వీకెండ్."),
    ("John", "Perfect. Let's plan it.", "పర్ఫెక్ట్. ప్లాన్ చేద్దాం."),
    ("Giri", "Okay, I'm excited.", "ఓకే, నేను ఎక్సైటెడ్.")
]

# HTML template
html_template = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>TOPIC Conversation — English & Telugu</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0f1724;
      --accent:#6ee7b7;
      --muted:#94a3b8;
      --highlight: rgba(255,255,255,0.03);
      --header-start:#7c3aed;
      --header-end:#06b6d4;
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
      background: linear-gradient(180deg, #031025 0%, #071226 60%);
      color:#e6eef8;
      padding:20px 5px; /* only 5px left-right */
      display:flex;
      justify-content:center;
    }
    .wrap{
      width:100%;
      max-width:980px;
    }
    header{
      display:flex;
      align-items:center;
      gap:14px;
      margin-bottom:18px;
    }
    .logo{
      width:56px;height:56px;border-radius:10px;
      background:linear-gradient(135deg,var(--header-start),var(--header-end));
      display:flex;align-items:center;justify-content:center;font-weight:700;color:white;
      box-shadow:0 6px 20px rgba(12,18,31,0.6);
      font-size:22px;
    }
    h1{font-size:26px;margin:0}
    p.lead{margin:4px 0 0;color:var(--muted);font-size:18px}

    .card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:12px;padding:18px;box-shadow: 0 10px 30px rgba(2,6,23,0.6);backdrop-filter: blur(6px);
    }

    table{width:100%;border-collapse:collapse;margin-top:12px}
    thead th{
      text-align:left;padding:14px 18px;font-weight:600;font-size:20px;
      background: linear-gradient(90deg,var(--header-start),var(--header-end));
      color:white;border-top-left-radius:8px;border-top-right-radius:8px;position:sticky;top:0;z-index:2
    }
    tbody td{padding:18px 20px;border-bottom:1px solid rgba(255,255,255,0.03);vertical-align:top;font-size:20px}
    tbody tr:nth-child(odd){background:linear-gradient(90deg, rgba(255,255,255,0.01), rgba(255,255,255,0));}
    tbody tr:hover{background:var(--highlight)}

    .role{font-weight:700;color:var(--accent);display:block;margin-bottom:6px;font-size:20px}
    .eng{font-size:20px}
    .tel{font-size:19px;color:var(--muted);margin-top:6px}

    @media (max-width:720px){
      thead{display:none}
      table,tbody,td,tr{display:block;width:100%}
      tbody td{padding:16px;border-bottom:1px solid rgba(255,255,255,0.03)}
      td .role{display:inline-block}
      td .eng{display:block}
      td .tel{display:block}
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">CJ</div>
      <div>
        <h1>TOPIC Conversation</h1>
        <p class="lead">English + Telugu Mix</p>
      </div>
    </header>

    <div class="card">
      <table>
        <thead>
          <tr>
            <th>Speaker</th>
            <th>Conversation</th>
          </tr>
        </thead>
        <tbody>
TBODY
        </tbody>
      </table>
    </div>
  </div>
</body>
</html>"""

def generate_tbody(conversation):
    tbody = ""
    for speaker, eng, tel in conversation:
        tbody += f"""          <tr>
            <td><span class="role">{speaker}</span></td>
            <td>
              <div class="eng">{eng}</div>
              <div class="tel">{tel}</div>
            </td>
          </tr>"""
    return tbody

# Generate files
for topic in topics:
    # Create folder (remove spaces for folder name)
    folder = topic.replace(" ", "")
    os.makedirs(folder, exist_ok=True)

    # Generate conversation by replacing TOPIC
    conversation = [(speaker, eng.replace("TOPIC", topic), tel.replace("TOPIC", topic)) for speaker, eng, tel in base_conversation]

    # Generate tbody
    tbody = generate_tbody(conversation)

    # Generate HTML
    html = html_template.replace("TOPIC", topic).replace("TBODY", tbody)

    # Write file
    filename = f"{topic} Conversation.htm"
    with open(f"{folder}/{filename}", "w", encoding="utf-8") as f:
        f.write(html)

print("Generated 1000 conversation HTML files.")