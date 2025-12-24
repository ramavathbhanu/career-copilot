# Load English NLP model

# Predefined skill list (you will expand this later)
SKILLS_DB = [
    "python", "java", "c", "c++", "sql", "html", "css", "javascript",
    "react", "node", "mongodb", "mysql",
    "data structures", "algorithms", "dsa",
    "machine learning", "deep learning", "nlp",
    "git", "github", "linux"
]

def extract_skills(text):
    skills = [
        "python", "java", "c", "c++", "sql", "mysql",
        "javascript", "html", "css", "node"
    ]
    found = []
    text = text.lower()

    for skill in skills:
        if skill in text:
            found.append(skill)

    return list(set(found))

if __name__ == "__main__":
    sample_text = """
    I have experience in Python, SQL, Data Structures and Git.
    I also worked with React and MongoDB.
    """

    skills = extract_skills(sample_text)
    print("Extracted Skills:", skills)
