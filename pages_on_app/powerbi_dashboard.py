import streamlit as st

def display():
    st.title("📊 Startup Dashboard in Power BI")

    st.markdown("""
    This Power BI dashboard was built to complement the app with visual insights.
    It allows users to explore startup data across countries, funding amounts, industry and outcomes.
    
    👉 **Interactivity** is enabled — you can filter by country and industry.

    ---
    """)

    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNGQ2OWI2M2YtZmUxZC00YjdlLWE1YWUtYWU1MTA3MTVhOTY1IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"

    st.components.v1.iframe (powerbi_url, width=1400, height=500)
