
import streamlit as st

def display():
    st.title("🚧 Project Challenges & Reflections")

    st.markdown("""
    Every data project comes with learning curves and obstacles. This one was no exception.
    Here's a summary of the key challenges I've encountered throughout the development of the Startup Success Translator.
    """)

    st.subheader("🛠️ 1. Changing the project scope mid-course")

    st.markdown("""
    - The original project idea focused on **analyzing project management tools**.
    - I encountered serious **dataset access issues**, with APIs limited or broken, and no reliable open dataset available.
    - As a result, I pivoted to this new idea around **startup success prediction**, starting again from scratch.

    💡 *Lesson:* It's crucial to evaluate dataset availability early when designing a data project.
    """)

    st.subheader("📉 2. Missing data and faulty imputation")

    st.markdown("""
    - In an early step, I replaced missing values in `funding_total_usd` with `-1` to keep the column numeric.
    - This later created **errors during winsorization** and skewed the distribution.
    - I had to backtrack, re-clean the data properly and apply correct outlier treatment.

    💡 *Lesson:* Use `NaN` for missing data and be cautious with placeholder values that can mislead analysis.
    """)

    st.subheader("🔍 3. Dataset limitations for modeling failure")

    st.markdown("""
    - The goal was to **predict whether a startup would fail or succeed**.
    - However, I noticed that the dataset was **heavily imbalanced**, with very few clear "failure" examples.
    - After researching new datasets, none matched the structure and context needed.

    💡 *Lesson:* Dataset quality and balance are key when building classification models. Not all questions are solvable with limited data.
    """)

    st.subheader("🧠 With more time...")

    st.markdown("""
    If the project were to continue, here are things I would love to explore:
    
    - ✅ **Web scraping Crunchbase** or other startup platforms to enrich this dataset with:
        - Current operational status
        - Founding team
        - Industry classification
    - ✅ Applying **class balancing techniques** to better train the model on rare outcomes
    """)
    st.success("Challenges are not obstacles — they're where learning happens! or in spanish: Quien trabaja,se equivoca")
