import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(layout="wide")
st.title("Player Attribute Dashboard")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
players = pd.read_csv("players.csv")

# -------------------------------------------------
# CONSTANTS
# -------------------------------------------------
GAUGE_HEIGHT = 320
RADAR_HEIGHT = 320

# -------------------------------------------------
# GAUGE HELPER (CLIPPING SAFE)
# -------------------------------------------------
def make_gauge(value, title, colors):
    light, mid, dark = colors
    if pd.isna(value):
        value = 0

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title, 'font': {'size': 13}},
            gauge={
                'axis': {
                    'range': [0, 20],
                    'tickwidth': 1,
                },
                'bar': {'color': dark},
                'steps': [
                    {'range': [0, 8], 'color': light},
                    {'range': [8, 14], 'color': mid},
                    {'range': [14, 20], 'color': dark},
                ],
            }
        )
    )

    fig.update_layout(
        height=GAUGE_HEIGHT,
        margin=dict(l=35, r=35, t=35, b=25),
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig


green_gradient = ("#b6f5b6", "#5cd65c", "#009900")
blue_gradient  = ("#b3d9ff", "#66a3ff", "#0052cc")
red_gradient   = ("#ffb3b3", "#ff6666", "#cc0000")

# -------------------------------------------------
# RADAR HELPER (CLIPPING SAFE)
# -------------------------------------------------
def radar_fig(values, labels, color):
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values + [values[0]],
            theta=labels + [labels[0]],
            fill="toself",
            line=dict(color=color)
        )
    )

    fig.update_layout(
        height=RADAR_HEIGHT,
        polar=dict(
            domain=dict(x=[0, 1], y=[0.07, 0.93]),
            radialaxis=dict(
                range=[0, 20],
                showticklabels=False
            )
        ),
        margin=dict(l=25, r=25, t=25, b=20),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig

# -------------------------------------------------
# SELECTIONS
# -------------------------------------------------
league = st.selectbox("Select League", sorted(players["Based"].dropna().unique()))
league_players = players[players["Based"] == league]

club = st.selectbox("Select Club", sorted(league_players["Club"].dropna().unique()))
club_players = league_players[league_players["Club"] == club]

player_name = st.selectbox("Select Player", sorted(club_players["Name"].unique()))
player = club_players[club_players["Name"] == player_name].iloc[0]

# -------------------------------------------------
# ATTRIBUTE GROUPS
# -------------------------------------------------
technical = ['Cor', 'Cro', 'Dri', 'Fin', 'Fir', 'Fre', 'Hea', 'Lon', 'L Th',
             'Mar', 'Pas', 'Pen', 'Tck', 'Tec']

mental = ['Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Det', 'Fla', 'Ldr',
          'OtB', 'Pos', 'Tea', 'Vis', 'Wor']

physical = ['Acc', 'Agi', 'Bal', 'Jum', 'Nat.1', 'Pac', 'Sta', 'Str']

keeping = ['Aer', 'Cmd', 'Com', 'Ecc', 'Han', 'Kic', '1v1', 'Pun', 'Ref', 'TRO', 'Thr']

all_attributes = technical + mental + physical + keeping

# =================================================
# LAYOUT
# =================================================
left, middle, right = st.columns([1.2, 2.6, 1.2])

# -------------------------------------------------
# LEFT PANEL — GENERAL INFO
# -------------------------------------------------
with left:
    st.subheader(player_name)
    st.markdown(
        f"""
        **Nationality:** {player['Nat']}  
        **Date of Birth:** {player['DoB']}  
        **Height:** {player['Height']}  
        **Weight:** {player['Weight']}  
        **Best Position:** {player['Best Pos']}  
        **Preferred Foot:** {player['Preferred Foot']}
        """
    )

# -------------------------------------------------
# MIDDLE PANEL — GAUGE + RADAR STACK
# -------------------------------------------------
with middle:
    st.markdown("### Attributes")
 


    for label, attrs, colors, col in [
        ("Technical", technical, green_gradient, "green"),
        ("Mental", mental, blue_gradient, "blue"),
        ("Physical", physical, red_gradient, "red"),
    ]:
        st.markdown(
            f"<h4 style='text-align: center; margin-bottom: 0.5rem;'>{label}</h4>",
            unsafe_allow_html=True
        )
        
        g, r = st.columns([1, 3])

        with g:
            st.plotly_chart(
                make_gauge(player[attrs].mean(), label, colors),
                use_container_width=False
            )

        with r:
            st.plotly_chart(
                radar_fig([player[a] for a in attrs], attrs, col),
                use_container_width=True
            )

# -------------------------------------------------
# RIGHT PANEL — TOP / WORST ATTRIBUTES
# -------------------------------------------------
with right:
    st.subheader("Attribute Extremes")

    N = st.slider("Number of attributes", 3, 10, 5)

    attr_series = player[all_attributes].astype(float)

    st.markdown("**Top Attributes**")
    st.dataframe(
        attr_series.sort_values(ascending=False).head(N).to_frame("Value"),
        height=200
    )

    st.markdown("**Weakest Attributes**")
    st.dataframe(
        attr_series.sort_values().head(N).to_frame("Value"),
        height=200
    )
