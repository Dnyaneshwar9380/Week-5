import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="Amazon Prime Titles Analysis", layout="wide")

st.title("📺 Exploratory Data Analysis of Amazon Prime Titles")

# Upload CSV
uploaded_file = st.file_uploader("Upload Amazon Prime Dataset CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # Basic Info
    st.subheader("Dataset Shape")
    st.write(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")

    # Null Values
    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # Convert Date
    if 'date_added' in data.columns:
        data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
        data['year_added'] = data['date_added'].dt.year

    # Release Year Distribution
    if 'release_year' in data.columns:
        st.subheader("Release Year Distribution")
        fig, ax = plt.subplots()
        sns.histplot(data['release_year'], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

    # Top Countries
    if 'country' in data.columns:
        st.subheader("Top 10 Countries")
        fig, ax = plt.subplots()
        data['country'].value_counts().head(10).plot(kind='bar', ax=ax)
        st.pyplot(fig)

    # Content Type Distribution
    if 'type' in data.columns:
        st.subheader("Movies vs TV Shows")
        fig, ax = plt.subplots()
        data['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)

    # Ratings Distribution
    if 'rating' in data.columns:
        st.subheader("Ratings Distribution")
        fig, ax = plt.subplots(figsize=(10,5))
        data['rating'].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

else:
    st.info("Please upload your CSV file to begin analysis.")