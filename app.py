import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------------------------------
# Basic page config
# -------------------------------------------------
st.set_page_config(layout="wide")
st.title("Player Attribute Dashboard")

# -------------------------------------------------
# Load Data
# -------------------------------------------------
df = pd.read_csv("attributes_with_images.csv")

# FIX: Clean column names (important!)
df.columns = df.columns.str.strip()

# -------------------------------------------------
# Attribute Groups
# -------------------------------------------------
technical = [
    'Cor', 'Cro', 'Dri', 'Fin', 'Fir', 'Fre', 'Hea', 'Lon', 'L Th',
    'Pas', 'Pen', 'Tck', 'Tec'
]

mental = [
    'Agg', 'Ant', 'Bra', 'Cmp', 'Cnt', 'Dec', 'Det', 'Fla', 'Ldr',
    'OtB', 'Pos', 'Tea', 'Vis'
]

physical = [
    'Wor', 'Acc', 'Agi', 'Bal', 'Jum', 'Pac', 'Nat', 'Sta', 'Str'
]

all_attributes = technical + mental + physical

# -------------------------------------------------
# Club selection
# -------------------------------------------------
club = st.selectbox("Select Club", df["Club"].unique())

# Filter players belonging to the chosen club
filtered_players = df[df["Club"] == club]["Name"].unique()

# -------------------------------------------------
# Player selection (filtered)
# -------------------------------------------------
player = st.selectbox("Select Player", filtered_players)

# Get selected player's row
player_row = df[(df["Name"] == player) & (df["Club"] == club)].iloc[0]

# Compute averages
# Coerce to numeric and ignore non-numeric gracefully
def safe_mean(series):
    return pd.to_numeric(series, errors="coerce").mean()

tech_avg = safe_mean(player_row[technical])
mental_avg = safe_mean(player_row[mental])
phys_avg = safe_mean(player_row[physical])

# -------------------------------------------------
# Gauge helper
# -------------------------------------------------
def make_gauge(value, title, colors, height=170):
    light, mid, dark = colors
    # guard NaN
    if pd.isna(value):
        value = 0
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title, 'font': {'size': 13, 'color': 'white'}},
            gauge={
                'axis': {'range': [0, 20]},
                'bar': {'color': dark},
                'steps': [
                    {'range': [0, 8], 'color': light},
                    {'range': [8, 14], 'color': mid},
                    {'range': [14, 20], 'color': dark},
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.7,
                    'value': value
                }
            }
        )
    )
    fig.update_layout(
        height=height,
        margin=dict(l=5, r=5, t=25, b=5),
        paper_bgcolor="rgba(0,0,0,0)",  # transparent background
    )
    return fig

green_gradient = ("#b6f5b6", "#5cd65c", "#009900")
blue_gradient  = ("#b3d9ff", "#66a3ff", "#0052cc")
red_gradient   = ("#ffb3b3", "#ff6666", "#cc0000")

# -------------------------------------------------
# Radar chart
# -------------------------------------------------
def make_radar(player_row):
    # coerce numeric, fillna with 0
    vals = pd.to_numeric(player_row[all_attributes], errors="coerce").fillna(0).values.tolist()
    values = vals + [vals[0]]
    labels = all_attributes + [all_attributes[0]]

    fig = go.Figure(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill='toself',
            line=dict(color="#0080ff", width=3)
        )
    )
    fig.update_layout(
        height=600,
        polar=dict(radialaxis=dict(visible=True, range=[0, 20])),
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40),
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig

# -------------------------------------------------
# Dark header + panel CSS (fixed)
# -------------------------------------------------
panel_css = """
<style>
.panel {
    background-color: #ffffff;
    padding: 0px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.07);
    margin-bottom: 20px;
}

.panel-header {
    background-color: #111111;
    color: white;
    padding: 12px 18px;
    border-top-left-radius: 14px;
    border-top-right-radius: 14px;
    font-size: 20px;
    font-weight: 700;
}

.panel-body {
    padding: 18px;
}

/* badge styling */
.badge {
    background: #111 !important;               /* Deep black/grey */
    color: #fff !important;                    /* White text */
    padding: 6px 12px;
    border-radius: 10px;
    font-weight: 600;
    border: 1px solid #444;                    /* Thin outline */
    box-shadow: 0px 1px 3px rgba(0,0,0,0.4);   /* Subtle depth */
    display: inline-block;
    margin: 4px 8px 8px 0;
    font-size: 14px;
}
.badge.yellow {
    background: linear-gradient(90deg,#fef3c7,#fde68a);
    color: #222 !important;
    border-color: #eab308;
}
.badge.violet {
    background: linear-gradient(90deg,#7c3aed,#a78bfa);
    color: #fff !important;
    border-color: #6d28d9;
}
</style>
"""
st.markdown(panel_css, unsafe_allow_html=True)

# ============================
# 3 Panel Layout
# ============================
col_left, col_center, col_right = st.columns([1.4, 2.2, 1.4])

# ============================
# LEFT PANEL: PLAYER INFO
# ============================
with col_left:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown(f"<div class='panel-header'>{player_row['Name']}</div>", unsafe_allow_html=True)

    st.markdown("<div class='panel-body'>", unsafe_allow_html=True)

    # Row 1: Player photo
    #st.markdown(f"{player_row['Name']}")
    if "Photo" in df.columns:
        st.image(player_row["Photo"], width=180)
    else:
        st.write("No photo in CSV")

    st.write("")  

    # Row 2: Club name + badge
    #st.markdown(f"{player_row['Club']}")
    if "ClubBadge" in df.columns:
        st.image(player_row["ClubBadge"], width=180)

    st.markdown("</div></div>", unsafe_allow_html=True)



# ============================
# CENTER PANEL: RADAR
# ============================
with col_center:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-header'>Attribute Radar</div>", unsafe_allow_html=True)
    st.markdown("<div class='panel-body'>", unsafe_allow_html=True)

    st.plotly_chart(make_radar(player_row), use_container_width=True)

    st.markdown("</div></div>", unsafe_allow_html=True)



# ============================
# RIGHT PANEL: GAUGES + TOP/WORST N
# ============================
with col_right:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='panel-header'>Attribute Summary</div>", unsafe_allow_html=True)
    st.markdown("<div class='panel-body'>", unsafe_allow_html=True)

    # Gauges
    g1, g2, g3 = st.columns(3)
    with g1:
        st.plotly_chart(make_gauge(tech_avg, "Tech", green_gradient), use_container_width=True)
    with g2:
        st.plotly_chart(make_gauge(mental_avg, "Mental", blue_gradient), use_container_width=True)
    with g3:
        st.plotly_chart(make_gauge(phys_avg, "Physical", red_gradient), use_container_width=True)

    st.write("---")

    # ===== TOP/WORST N ATTRIBUTES =====

    # Slider
    N = st.slider("Top/Worst N Attributes", 1, len(all_attributes), 10)

    vals = player_row[all_attributes].astype(float)
    sorted_vals = vals.sort_values(ascending=False)

    top_n = sorted_vals.head(N)
    worst_n = sorted_vals.sort_values(ascending=True).head(N)

    # Mapping for tooltips
    attr_names = {
        'Cor':'Corners','Cro':'Crossing','Dri':'Dribbling','Fin':'Finishing',
        'Fir':'First Touch','Fre':'Free Kick Taking','Hea':'Heading','Lon':'Long Shots',
        'L Th':'Long Throws','Pas':'Passing','Pen':'Penalty Taking','Tck':'Tackling',
        'Tec':'Technique','Agg':'Aggression','Ant':'Anticipation','Bra':'Bravery',
        'Cmp':'Composure','Cnt':'Concentration','Dec':'Decisions','Det':'Determination',
        'Fla':'Flair','Ldr':'Leadership','OtB':'Off the Ball','Pos':'Positioning',
        'Tea':'Teamwork','Vis':'Vision','Wor':'Work Rate','Acc':'Acceleration',
        'Agi':'Agility','Bal':'Balance','Jum':'Jumping Reach','Pac':'Pace',
        'Nat':'Natural Fitness','Sta':'Stamina','Str':'Strength'
    }

    # Badge generator
    def badge(attr, val, emoji):
        full = attr_names.get(attr, attr)
        return (
            f"<span class='badge' title='{full}'>"
            f"{emoji} {attr}: {int(val) if float(val).is_integer() else val}"
            f"</span>"
        )

    # TOP N
    st.subheader(f"Top {N} Attributes")
    st.markdown("".join([badge(a, v, "⭐") for a, v in top_n.items()]),
                unsafe_allow_html=True)

    st.write("")

    # WORST N
    st.subheader(f"Worst {N} Attributes")
    st.markdown("".join([badge(a, v, "🤮") for a, v in worst_n.items()]),
                unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
