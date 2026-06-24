import pandas as pd

SKILLS = [
    "python", "sql", "excel", "power bi", "tableau", "pandas", "numpy",
    "machine learning", "statistics", "data visualization", "dashboard",
    "etl", "azure", "aws", "google analytics", "looker", "r", "spark"
]


def extract_skills(text):
    text = str(text).lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill.title())

    return found


def create_skill_table(df):
    rows = []

    for _, row in df.iterrows():
        skills = extract_skills(row.get("job_description", ""))

        for skill in skills:
            rows.append({
                "job_title": row.get("job_title", ""),
                "company": row.get("company", ""),
                "location": row.get("location", ""),
                "skill": skill
            })

    return pd.DataFrame(rows)
