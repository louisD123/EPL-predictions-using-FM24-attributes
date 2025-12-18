import streamlit as st
import pandas as pd
import numpy as np
import joblib




@st.cache_resource
def load_model():
    return joblib.load("rf_model.pkl")

rf_model = load_model()

@st.cache_data
def load_clubs():
    df = pd.read_csv("club_pca.csv")
    return df.set_index("Club")


club_pca = load_clubs()



st.title("Match Outcome Probabilities (Random Forest)")

st.markdown(
    "Select **Home** and **Away** clubs to get predicted probabilities."
)


clubs = club_pca.index.tolist()

home_club = st.selectbox("Home Club", clubs)
away_club = st.selectbox("Away Club", clubs, index=1)


def make_features(home, away):
    home_pcs = club_pca.loc[home].values
    away_pcs = club_pca.loc[away].values
    diff = home_pcs - away_pcs
    return diff.reshape(1, -1)

X = make_features(home_club, away_club)



probs = rf_model.predict_proba(X)[0]
classes = rf_model.classes_



prob_map = dict(zip(classes, probs))

p_home = prob_map.get(1, 0.0)
p_draw = prob_map.get(0, 0.0)
p_away = prob_map.get(-1, 0.0)




st.subheader("Predicted Probabilities")

col1, col2, col3 = st.columns(3)

col1.metric("Home Win", f"{p_home:.2%}")
col2.metric("Draw", f"{p_draw:.2%}")
col3.metric("Away Win", f"{p_away:.2%}")


st.subheader("Fair odds")

col1, col2, col3 = st.columns(3)

col1.metric("Home Win", f"{1/p_home:.2f}")
col2.metric("Draw", f"{1/p_draw:.2f}")
col3.metric("Away Win", f"{1/p_away:.2f}")



