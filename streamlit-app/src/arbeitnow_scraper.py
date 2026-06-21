from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import pandas as pd
import requests

ARBEITNOW_API_URL = "https://www.arbeitnow.com/api/job-board-api"


def _clean_html(text: Any) -> str:
    return str(text or "").replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")


def fetch_arbeitnow_jobs(keyword: str = "data", limit: int = 100) -> pd.DataFrame:
    """Fetch job postings from Arbeitnow's public job board API."""
    response = requests.get(ARBEITNOW_API_URL, timeout=30)
    response.raise_for_status()

    payload = response.json()
    jobs = payload.get("data", []) if isinstance(payload, dict) else []
    rows = []

    keyword_lower = keyword.lower().strip()

    for job in jobs:
        title = str(job.get("title", ""))
        company = str(job.get("company_name", ""))
        description = _clean_html(job.get("description", ""))
        tags = " ".join(job.get("tags", []) or [])
        search_text = f"{title} {company} {description} {tags}".lower()

        if keyword_lower and keyword_lower not in search_text:
            continue

        location = job.get("location") or "Not specified"
        created_at = job.get("created_at")
        if isinstance(created_at, int):
            date_posted = datetime.fromtimestamp(created_at, timezone.utc).date().isoformat()
        else:
            date_posted = datetime.now(timezone.utc).date().isoformat()

        rows.append({
            "job_title": title,
            "company": company,
            "location": location,
            "salary": "",
            "job_description": description,
            "date_posted": date_posted,
            "job_url": job.get("url") or "",
            "source": "Arbeitnow"
        })

        if len(rows) >= limit:
            break

    return pd.DataFrame(rows)
