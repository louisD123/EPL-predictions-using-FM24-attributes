import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------- Load model and data --------------------
rf_1Xvs2 = joblib.load("rf_1Xvs2_classifier.pkl")
club_pca = pd.read_csv("club_pca.csv")  # must have columns: 'Club', 'PC1', ..., 'PC13'

pc_cols = [f"PC{i}" for i in range(1, 14)]

# -------------------- Streamlit interface --------------------
st.title("Football: Home Avoids Losing Predictor (1X vs 2)")

home_club = st.selectbox("Select Home Club", club_pca['Club'].tolist())
away_club = st.selectbox("Select Away Club", club_pca['Club'].tolist())

# -------------------- Get PCs for selected clubs --------------------
home_pc = club_pca.loc[club_pca['Club']==home_club, pc_cols].values
away_pc = club_pca.loc[club_pca['Club']==away_club, pc_cols].values

if home_pc.size == 0 or away_pc.size == 0:
    st.error("PCs for selected clubs not found!")
else:
    # Compute difference features
    X_input = (home_pc - away_pc).reshape(1, -1)
    
    # Predict probability
    p_home_avoids_losing = rf_1Xvs2.predict_proba(X_input)[0,1]
    
    # Display results
    st.subheader("Probabilities")
    
    col1, col2 = st.columns(2)
    col1.metric("Home wins or draws (1X)", f"{p_home_avoids_losing:.2f}")
    col2.metric("Home loses", f"{1 - p_home_avoids_losing:.2f}")


    st.subheader("Fair odds")


    col1, col2 = st.columns(2)
    col1.metric("Home wins or draws (1X)", f"{1/p_home_avoids_losing:.2f}")
    col2.metric("Home loses", f"{ 1/(1 - p_home_avoids_losing):.2f}")
