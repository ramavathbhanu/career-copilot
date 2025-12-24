ROLE_SKILLS = {
    "data_analyst": ["python", "sql", "excel", "statistics", "power bi", "tableau"],
    "software_developer": ["python", "java", "dsa", "git"]
}

def analyze_skills(resume_skills, role):
    role = role.lower()
    required = ROLE_SKILLS.get(role, [])

    matched = [s for s in required if s in resume_skills]
    missing = [s for s in required if s not in resume_skills]

    confidence = round((len(matched) / len(required)) * 100, 2) if required else 0

    return matched, missing, confidence
