from typing import Set

def load_skills(file_path: str) -> Set[str]:
    with open(file_path, "r", encoding = "utf-8") as file:
        skills = {line.strip().lower() for line in file if line.strip()}
    return skills

def extract_skills(text: str, skills_db: Set[str]) -> Set[str]:
    extracted = set()
    for skill in skills_db:
        if skill in text:
            extracted.add(skill)
    return extracted