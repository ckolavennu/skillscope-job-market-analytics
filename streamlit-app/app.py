import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from src.skill_extraction import create_skill_table

st.set_page_config(
    page_title="SkillScope Dashboard",
    page_icon="📊",
    layout="wide"
)

DATA_PATH = Path("data/raw/job_postings.csv")
SAMPLE_DATA_PATH = Path("data/raw/job_postings_sample.csv")


@st.cache_data
def load_data():
    path = DATA_PATH if DATA_PATH.exists() else SAMPLE_DATA_PATH
    return pd.read_csv(path)


df = load_data()

st.title("📊 SkillScope Job Market Dashboard")
st.caption("Explore job postings, in-demand skills, hiring locations, and employer demand.")

st.sidebar.header("Filters")

locations = sorted(df["location"].dropna().unique())
selected_locations = st.sidebar.multiselect(
    "Location",
    options=locations,
    default=locations
)

filtered_df = df[df["location"].isin(selected_locations)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Jobs Collected", len(filtered_df))
col2.metric("Companies", filtered_df["company"].nunique())
col3.metric("Locations", filtered_df["location"].nunique())
col4.metric("Sources", filtered_df["source"].nunique())

st.divider()

st.subheader("Top In-Demand Skills")
skill_df = create_skill_table(filtered_df)

if not skill_df.empty:
    skill_count = skill_df["skill"].value_counts().reset_index()
    skill_count.columns = ["Skill", "Count"]

    fig_skills = px.bar(skill_count, x="Skill", y="Count", title="Most Mentioned Skills")
    st.plotly_chart(fig_skills, use_container_width=True)
else:
    st.info("No skills detected yet. Add more job descriptions to improve the analysis.")

left, right = st.columns(2)

with left:
    st.subheader("Jobs by Location")
    location_count = filtered_df["location"].value_counts().reset_index()
    location_count.columns = ["Location", "Jobs"]
    fig_location = px.bar(location_count, x="Location", y="Jobs", title="Jobs by Location")
    st.plotly_chart(fig_location, use_container_width=True)

with right:
    st.subheader("Top Hiring Companies")
    company_count = filtered_df["company"].value_counts().reset_index()
    company_count.columns = ["Company", "Jobs"]
    fig_company = px.bar(company_count, x="Company", y="Jobs", title="Top Hiring Companies")
    st.plotly_chart(fig_company, use_container_width=True)

st.subheader("Job Posting Data")
st.dataframe(filtered_df, use_container_width=True)
