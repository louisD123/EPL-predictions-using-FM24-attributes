import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("../../data/ATTRIBUTES.csv")

df = load_data()

st.set_page_config(page_title="FM25 Dashboard", layout="wide")

# ---- Attribute groups ----
physical = ['Wor', 'Acc', 'Agi', 'Bal', 'Jum', 'Pac', 'Nat', 'Sta', 'Str']
mental   = ['Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Det', 'Fla', 'Ldr', 'OtB', 'Pos', 'Tea', 'Vis']
technical = ['Cor', 'Cro', 'Dri', 'Fin', 'Fir', 'Fre', 'Hea', 'Lon', 'L Th', 'Pas', 'Pen', 'Tck', 'Tec']
attrs = [c for c in df.columns if c not in ["Club", "Name"]]

# ---- Radar Plot Function ----
def make_radar(values, categories, title):
    colored_labels = []
    for cat in categories:
        if cat in physical:
            colored_labels.append(f"<span style='color:red'>{cat}</span>")
        elif cat in mental:
            colored_labels.append(f"<span style='color:blue'>{cat}</span>")
        elif cat in technical:
            colored_labels.append(f"<span style='color:green'>{cat}</span>")
        else:
            colored_labels.append(cat)

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        line=dict(color="white")
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, showgrid=True, range=[0, 20], gridcolor="gray"),
            angularaxis=dict(
                tickmode="array",
                tickvals=categories,
                ticktext=colored_labels,
                showgrid=True,
                gridcolor="gray"
            )
        ),
        showlegend=False,
        title=title,
        paper_bgcolor="black",
        plot_bgcolor="black",
        font=dict(color="white")
    )
    return fig

# ---- CSS for bordered card ----
st.markdown("""
<style>
.metric-card {
    border: 1px solid #444;
    padding: 15px;
    border-radius: 10px;
    background-color: #1e1e1e;
}
.metric-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---- Sidebar ----
page = st.sidebar.selectbox("Choose a page", ["Browse Clubs/Players", "Predictions"])

# -------------------- PAGE 1 ----------------------
if page == "Browse Clubs/Players":
    st.title("Browse Clubs & Players")

    clubs = sorted(df["Club"].dropna().unique())
    selected_club = st.selectbox("Select Club", clubs)
    club_df = df[df["Club"] == selected_club]

    # ---------- CLUB SECTION ----------
    st.subheader(f"Average Attributes — {selected_club}")

    col_left, col_rad = st.columns([1.2, 4])

    with col_left:
        club_phys = club_df[physical].mean().mean()
        club_ment = club_df[mental].mean().mean()
        club_tech = club_df[technical].mean().mean()

        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-title'>Club Attribute Averages</div>", unsafe_allow_html=True)
        st.metric("Physical", round(club_phys, 2))
        st.metric("Mental", round(club_ment, 2))
        st.metric("Technical", round(club_tech, 2))
        st.markdown("</div>", unsafe_allow_html=True)

    with col_rad:
        club_avg = club_df[attrs].mean()
        fig_club = make_radar(club_avg.values.tolist(), attrs, f"{selected_club} — Average Attributes")
        st.plotly_chart(fig_club, use_container_width=True)

    # ---------- PLAYER SECTION ----------
    players = sorted(club_df['Name'].dropna().unique())

    if len(players) > 0:
        selected_player = st.selectbox("Select Player", options=players)

        st.subheader(f"Attributes — {selected_player}")

        col_left2, col_rad2 = st.columns([1.2, 4])

        player_row = club_df[club_df['Name'] == selected_player].iloc[0]

        with col_left2:
            player_phys = player_row[physical].mean()
            player_ment = player_row[mental].mean()
            player_tech = player_row[technical].mean()

            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.markdown("<div class='metric-title'>Player Attribute Averages</div>", unsafe_allow_html=True)
            st.metric("Physical", round(player_phys, 2))
            st.metric("Mental", round(player_ment, 2))
            st.metric("Technical", round(player_tech, 2))
            st.markdown("</div>", unsafe_allow_html=True)

        with col_rad2:
            player_vals = player_row[attrs].tolist()
            fig_player = make_radar(player_vals, attrs, f"{selected_player} — Attributes")
            st.plotly_chart(fig_player, use_container_width=True)

# -------------------- PAGE 2 ----------------------
else:
    st.title("Predictions")
    st.write("Prediction models will be added soon.")
