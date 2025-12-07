import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(layout="wide")

st.title("⚽ Match Outcome Predictions")

# ======================================================
# Load model components
# ======================================================
clf = joblib.load("rf_model.joblib")
le = joblib.load("label_encoder.joblib")
feature_cols = joblib.load("feature_cols.joblib")

# ======================================================
# Load club averages
# ======================================================
# If you saved it as JSON:
#   with open("club_avgs.json") as f: club_avgs = json.load(f)

# If you saved it as joblib:
club_avgs = joblib.load("club_avgs.joblib")

clubs = list(club_avgs.keys())

# ======================================================
# Prediction function
# ======================================================
def predict_match(home_club, away_club):
    row = {}

    # Home features
    for attr in club_avgs[home_club]:
        col = f"home_{attr}"
        if col in feature_cols:
            row[col] = club_avgs[home_club][attr]

    # Away features
    for attr in club_avgs[away_club]:
        col = f"away_{attr}"
        if col in feature_cols:
            row[col] = club_avgs[away_club][attr]

    # DataFrame with correct feature names (fixes sklearn warning)
    X_input = pd.DataFrame([row], columns=feature_cols)

    # Predict
    probs = clf.predict_proba(X_input)[0]
    labels = le.inverse_transform([0, 1, 2])  # [-1, 0, 1]

    return dict(zip(labels, probs))

# ======================================================
# UI
# ======================================================
col1, col2 = st.columns(2)

with col1:
    home_club = st.selectbox("Home Club", clubs)

with col2:
    away_club = st.selectbox("Away Club", clubs)

# Prediction
if st.button("Predict Outcome", type="primary"):
    if home_club == away_club:
        st.error("Home and Away teams must be different.")
    else:
        probs = predict_match(home_club, away_club)

        st.subheader(f"Prediction: {home_club} vs {away_club}")

        # Probability cards
        c1, c2, c3 = st.columns(3)

        c1.metric("🏠 Home Win", f"{probs[1]*100:.1f}%")
        c2.metric("🤝 Draw", f"{probs[0]*100:.1f}%")
        c3.metric("🚗 Away Win", f"{probs[-1]*100:.1f}%")

        
