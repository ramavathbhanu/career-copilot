# career_roles.py

CAREER_SKILLS = {
    "software_developer": [
        "python", "java", "c", "c++", "dsa", "sql", "git"
    ],
    "data_analyst": [
        "python", "sql", "excel", "statistics", "power bi", "tableau"
    ],
    "web_developer": [
        "html", "css", "javascript", "react", "node", "mongodb"
    ],
    "ml_engineer": [
        "python", "machine learning", "deep learning", "numpy", "pandas"
    ]
}

def get_required_skills(role):
    return CAREER_SKILLS.get(role, [])
