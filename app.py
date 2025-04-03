
import streamlit as st
from pages_on_app import predictor, startup_stages, eda_review, powerbi_dashboard , project_challenges

section = st.sidebar.radio(
    "Navigate to:",
    ["🏠 Project Overview", "📘 Startup Stages", "🧪 EDA & Dataset", "📊 Interactive dashboard", "🔮 Success Prediction", "🚧 Project Challenges"]
)

if section == "🏠 Project Overview":
    st.title("🚀 Startup Success Translator")
    st.markdown("""
    Welcome to the **Startup Success Translator**, a tool for non-financial team members to understand startup dynamics using real data and ML.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🔮 Prediction")
        st.markdown("Estimate startup success from funding & country.")
    with col2:
        st.subheader("📘 Startup Stages")
        st.markdown("Understand the phases of a startup.")
    with col3:
        st.subheader("📊 Data Analysis")
        st.markdown("See how the model was built.")
    st.markdown("---")
    st.info("Use the sidebar to explore the app.")

elif section == "🔮 Success Prediction":
    predictor.display()
elif section == "📘 Startup Stages":
    startup_stages.display()
elif section == "🧪 EDA & Dataset":
    eda_review.display()
elif section == "🚧 Project Challenges":
    project_challenges.display()
elif section == "📊 Interactive dashboard":
    powerbi_dashboard.display()
