
import streamlit as st
import pandas as pd

def display():
    st.title("🧪 EDA & Dataset Summary")

    st.markdown("""
    This project is based on a Crunchbase-like dataset with over **66,000 startups** from around the world.  
    The objective was to understand how certain features relate to the **success or failure** of a startup.
    """)

    st.subheader("🧼 Cleaning & Feature Engineering")

    st.markdown("""
    - Transformed date columns to `datetime` format.
    - Converted strings with dashes (`-`) in numerical columns to `NaN` and cast as float.
    - Removed IDs and irrelevant features.
    - **Winsorization applied to `funding_total_usd`:**  
        The total funding column had **extremely large values** (up to billions of USD), which could skew the model.  
        We applied **winsorization at the 1st and 99th percentiles**, meaning:
        - Any value **below the 1st percentile** was replaced by the 1st percentile value.
        - Any value **above the 99th percentile** was replaced by the 99th percentile value.

        🧠 *Why it matters:*  
        This method preserves the distribution but reduces the impact of **outliers**, which could otherwise:
        - Over-influence the model
        - Cause it to assign too much importance to very rare startup cases
        - Lead to poor generalization on new data
    - Created a binary target `success` (1 = operating, 0 = not operating).
    - Focused on 3 key variables:  
        - `funding_rounds`  
        - `funding_total_usd_winsorized`  
        - `country_code`
    """)

    st.subheader("📊 Visual Exploration Highlights")

    st.markdown("### 💰 Distribution of total funding")
    st.image("distribuciondefunding.png", use_container_width=True)

    st.markdown("### 🧾 Number of funding rounds by status")
    st.image("financiacionporestado.png", use_container_width=True)

    st.markdown("### 📈 Funding evolution over time")
    st.image("fundingeneltiempo.png", use_container_width=True)

    st.markdown("### 🌍 Funding by country (top 10)")
    st.image("fundingporpais.png", use_container_width=True)

    st.markdown("### 🏷️ Funding amount by startup status")
    st.image("fundingtotalporestado.png", use_container_width=True)

    st.markdown("### 📌 Startup counts by status")
    st.image("startupsporestado.png", use_container_width=True)
    st.info("This distribution shows one of the main problems at the time of creating the prediction model")

    st.markdown("---")
    st.info("These visual insights helped guide the model creation and feature selection.")
