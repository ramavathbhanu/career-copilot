from fastapi import FastAPI, UploadFile, File, Form

from fastapi.middleware.cors import CORSMiddleware
import fitz
import shutil

from skill_extractor import extract_skills
from skill_gap import analyze_skills      # UPDATED
from learning_plan import generate_7_day_plan

app = FastAPI(title="AI Career Copilot")

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text


@app.get("/")
def root():
    return {"message": "AI Career Copilot backend running"}


@app.post("/analyze")
async def analyze_resume(
    role: str = Form(...),
    resume: UploadFile = File(...)
):
    temp_path = f"temp_{resume.filename}"

    # Save uploaded resume
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    # Extract text & skills
    text = extract_text_from_pdf(temp_path)
    resume_skills = extract_skills(text)

    # Skill analysis (NEW)
    matched_skills, missing_skills, confidence = analyze_skills(resume_skills, role)

    # Learning plan
    plan = generate_7_day_plan(missing_skills)

    # AI explanation message
    if confidence >= 70:
        ai_message = "You are well aligned with this role. Focus on refining weak areas."
    elif confidence >= 40:
        ai_message = "You have a good foundation, but need structured upskilling."
    else:
        ai_message = "You need significant skill development for this role."

    return {
        "role": role,
        "resume_skills": resume_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "confidence_score": confidence,
        "ai_message": ai_message,
        "learning_plan": plan
    }
