from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import pandas as pd
import requests

REMOTEOK_API_URL = "https://remoteok.com/api"


def _clean_html(text: Any) -> str:
    return str(text or "").replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")


def fetch_remoteok_jobs(keyword: str = "data", limit: int = 100) -> pd.DataFrame:
    """Fetch remote job postings from RemoteOK's public JSON feed."""
    headers = {
        "User-Agent": "SkillScope Job Market Analytics Portfolio Project"
    }

    response = requests.get(REMOTEOK_API_URL, headers=headers, timeout=30)
    response.raise_for_status()

    payload = response.json()
    jobs = payload[1:] if isinstance(payload, list) and payload else []
    rows = []

    keyword_lower = keyword.lower().strip()

    for job in jobs:
        title = str(job.get("position", ""))
        company = str(job.get("company", ""))
        description = _clean_html(job.get("description", ""))
        tags = " ".join(job.get("tags", []) or [])
        search_text = f"{title} {company} {description} {tags}".lower()

        if keyword_lower and keyword_lower not in search_text:
            continue

        salary_min = job.get("salary_min") or ""
        salary_max = job.get("salary_max") or ""
        salary = f"{salary_min} - {salary_max}" if salary_min or salary_max else ""

        rows.append({
            "job_title": title,
            "company": company,
            "location": job.get("location") or "Remote",
            "salary": salary,
            "job_description": description,
            "date_posted": job.get("date") or datetime.now(timezone.utc).date().isoformat(),
            "job_url": job.get("url") or "",
            "source": "RemoteOK"
        })

        if len(rows) >= limit:
            break

    return pd.DataFrame(rows)
