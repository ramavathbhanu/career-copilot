from skill_extractor import extract_skills
from skill_gap import find_skill_gap
from learning_plan import generate_7_day_plan
import fitz # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf = fitz.open(pdf_path)
    for page in pdf:
        text += page.get_text()
    return text


if __name__ == "__main__":
    resume_text = extract_text_from_pdf("sample_resume.pdf")
    resume_skills = extract_skills(resume_text)

    career_role = "data_analyst"  # change role to test
    gaps = find_skill_gap(resume_skills, career_role)

    plan = generate_7_day_plan(gaps)

    print("\nResume Skills:", resume_skills)
    print("\nMissing Skills:", gaps)
    print("\n7-Day Learning Plan:")
    for day, task in plan.items():
        print(day, "→", task)

