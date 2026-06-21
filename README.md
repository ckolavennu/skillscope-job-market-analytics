# SkillScope: Job Market Analytics Platform

SkillScope is a portfolio project for analyzing job market demand using real job posting data. The project combines Svelte for the public-facing website, Streamlit for the interactive analytics dashboard, and Python for data collection, cleaning, and skill extraction.

## Project Structure

- svelte-site: Main website and landing page
- streamlit-app: Analytics dashboard and Python data pipeline
- README.md: Project documentation
- .gitignore: Ignore rules for Python, Node, and generated files

## Current MVP

The current version includes a Svelte landing site, a dashboard embed page, a Streamlit analytics dashboard, sample job posting data, skill extraction from job descriptions, location analysis, company analysis, and job collection scripts using public job APIs.

## Run the Streamlit Dashboard

1. cd streamlit-app
2. pip install -r requirements.txt
3. python -m streamlit run app.py

## Collect Real Job Data

From inside the streamlit-app folder, run:

1. python -m src.collect_jobs

This creates data/raw/job_postings.csv. The Streamlit dashboard will automatically use that file when it exists. If it does not exist, the dashboard falls back to the sample dataset.

Current sources:

- RemoteOK public job feed
- Arbeitnow public job board API

## Run the Svelte Site

1. cd svelte-site
2. npm install
3. npm run dev

## Deployment Plan

Deploy streamlit-app to Streamlit Community Cloud. Deploy svelte-site to Vercel, Netlify, or GitHub Pages. After the Streamlit app is deployed, replace the placeholder iframe URL in svelte-site/src/App.svelte with the deployed Streamlit URL.

## Next Milestones

1. Add salary cleaning and salary analytics
2. Improve skill extraction dictionary
3. Add resume skill-gap analyzer
4. Deploy both apps publicly
