def analyze_skill_gap(missing_keywords):
    
    skill_map = {
        "python": "Improve Python fundamentals",
        "fastapi": "Learn FastAPI for backend development",
        "django": "Learn Django framework",
        "react": "Learn React for frontend",
        "node": "Learn Node.js backend development",
        "machine": "Study Machine Learning basics",
        "ai": "Understand AI concepts",
        "sql": "Learn SQL and databases",
        "mongodb": "Learn MongoDB (NoSQL DB)",
        "docker": "Learn Docker for deployment"
    }

    suggestions = []

    for word in missing_keywords:
        for key in skill_map:
            if key in word:
                suggestions.append(skill_map[key])

    return list(set(suggestions))  # remove duplicates