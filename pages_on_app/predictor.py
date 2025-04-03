
import streamlit as st
import pandas as pd
import joblib

def display():
    st.header("🔮 Will your startup succeed?")

    model = joblib.load("startup_success_model.pkl")
    feature_names = joblib.load("startup_features.pkl")

    funding = st.number_input("💰 Total Funding (USD)", min_value=1000, step=1000)
    rounds = st.number_input("🔁 Number of Funding Rounds", min_value=1, step=1)
    country = st.selectbox("🌍 Country", options=["USA", "GBR", "IND", "CAN", "DEU", "FRA", "CHN", "ISR", "SWE", "ESP"])

    if st.button("Predict"):
        input_df = pd.DataFrame({
            "funding_total_usd_winsorized": [funding],
            "funding_rounds": [rounds],
            "country_code": [country]
        })

        prob_success = model.predict_proba(input_df)[0][1]
        prob_fail = model.predict_proba(input_df)[0][0]

        if prob_success >= 0.5:
            st.success(f"✅ Success predicted with {prob_success:.2%} probability")
        else:
            st.error(f"❌ Failure predicted. Success chance: {prob_success:.2%}")

        st.markdown(f"- 🟢 Success: **{prob_success:.2%}**\n- 🔴 Failure: **{prob_fail:.2%}**")
