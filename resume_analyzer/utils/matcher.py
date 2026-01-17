from typing import Set, Dict

def match_skills(resume_skills: Set[str], jd_skills: Set[str]) -> Dict[str, object]:
    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)

    if not jd_skills:
        match_percentage = 0
    else:
        match_percentage = round((len(matched_skills)/len(jd_skills))*100, 2)
    
    return {"matched_skills": matched_skills, "missing_skills": missing_skills, "match_percentage": match_percentage}