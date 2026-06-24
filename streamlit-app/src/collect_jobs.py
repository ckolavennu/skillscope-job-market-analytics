from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.arbeitnow_scraper import fetch_arbeitnow_jobs
from src.remoteok_scraper import fetch_remoteok_jobs

OUTPUT_PATH = Path("data/raw/job_postings.csv")


def collect_jobs(keyword: str = "data", limit_per_source: int = 100) -> pd.DataFrame:
    frames = []

    collectors = [
        fetch_remoteok_jobs,
        fetch_arbeitnow_jobs,
    ]

    for collector in collectors:
        try:
            df = collector(keyword=keyword, limit=limit_per_source)
            if not df.empty:
                frames.append(df)
                print(f"Collected {len(df)} jobs from {df['source'].iloc[0]}")
            else:
                print(f"No jobs collected from {collector.__name__}")
        except Exception as exc:
            print(f"Skipped {collector.__name__}: {exc}")

    if not frames:
        return pd.DataFrame(columns=[
            "job_title", "company", "location", "salary", "job_description",
            "date_posted", "job_url", "source"
        ])

    combined = pd.concat(frames, ignore_index=True)
    combined = combined.drop_duplicates(subset=["job_title", "company", "job_url"])
    return combined


if __name__ == "__main__":
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    jobs_df = collect_jobs(keyword="data", limit_per_source=100)
    jobs_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved {len(jobs_df)} jobs to {OUTPUT_PATH}")
