import os

# List of 100 unique topics
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
    "Cybersecurity", "Programming", "Data Science", "Machine Learning"
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

print("Generated 100 conversation HTML files.")