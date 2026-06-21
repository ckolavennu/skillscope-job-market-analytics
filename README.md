# SkillScope: Job Market Analytics Platform

SkillScope is a portfolio project for analyzing job market demand using real job posting data. The project combines Svelte for the public-facing website, Streamlit for the interactive analytics dashboard, and Python for data cleaning, skill extraction, and future scraping/API collection.

## Project Structure

- svelte-site: Main website and landing page
- streamlit-app: Analytics dashboard
- README.md: Project documentation
- .gitignore: Ignore rules for Python, Node, and generated files

## Current MVP

The current version includes a Svelte landing site, a dashboard embed page, a Streamlit analytics dashboard, sample job posting data, skill extraction from job descriptions, and location, company, and skill demand charts.

## Run the Streamlit Dashboard

1. cd streamlit-app
2. pip install -r requirements.txt
3. python -m streamlit run app.py

## Run the Svelte Site

1. cd svelte-site
2. npm install
3. npm run dev

## Deployment Plan

Deploy streamlit-app to Streamlit Community Cloud. Deploy svelte-site to Vercel, Netlify, or GitHub Pages. Add the deployed Streamlit URL inside svelte-site/src/routes/Dashboard.svelte.

## Next Milestones

1. Add safer job data collection using public APIs
2. Add salary cleaning and salary analytics
3. Add resume skill-gap analyzer
4. Deploy both apps publicly
