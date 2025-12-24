import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined skill list (you will expand this later)
SKILLS_DB = [
    "python", "java", "c", "c++", "sql", "html", "css", "javascript",
    "react", "node", "mongodb", "mysql",
    "data structures", "algorithms", "dsa",
    "machine learning", "deep learning", "nlp",
    "git", "github", "linux"
]

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)


if __name__ == "__main__":
    sample_text = """
    I have experience in Python, SQL, Data Structures and Git.
    I also worked with React and MongoDB.
    """

    skills = extract_skills(sample_text)
    print("Extracted Skills:", skills)
