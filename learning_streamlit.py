import streamlit as st
import pandas as pd

# --- Load your data ---
df = pd.read_csv("attributes.csv")

# --- Attribute full-name mapping (keep/update as needed) ---
attr_names = {
    'Cor': 'Corners','Cro':'Crossing','Dri':'Dribbling','Fin':'Finishing',
    'Fir':'First Touch','Fre':'Free Kick Taking','Hea':'Heading','Lon':'Long Shots',
    'L Th':'Long Throws','Pas':'Passing','Pen':'Penalty Taking','Tck':'Tackling',
    'Tec':'Technique','Agg':'Aggression','Ant':'Anticipation','Bra':'Bravery',
    'Cmp':'Composure','Cnt':'Concentration','Dec':'Decisions','Det':'Determination',
    'Fla':'Flair','Ldr':'Leadership','OtB':'Off the Ball','Pos':'Positioning',
    'Tea':'Teamwork','Vis':'Vision','Wor':'Work Rate','Acc':'Acceleration',
    'Agi':'Agility','Bal':'Balance','Jum':'Jumping Reach','Pac':'Pace',
    'Nat':'Natural Fitness','Sta':'Stamina','Str':'Strength'
}

attribute_cols = list(attr_names.keys())

# --- UI controls ---
player = st.selectbox("Choose a player", df["Name"].unique())
n = st.slider("Top/Worst N attributes", min_value=1, max_value=len(attribute_cols), value=10)

# --- Prepare data ---
row = df[df["Name"] == player].iloc[0]
# Ensure numeric values; if strings, try to coerce
vals = row[attribute_cols].astype(float)
sorted_attrs = vals.sort_values(ascending=False)

top_n = sorted_attrs.head(n)
worst_n = sorted_attrs.sort_values(ascending=True).head(n)


# --- HTML + CSS for badges ---
css = """
<style>
.badge-row { display:flex; flex-wrap:wrap; gap:8px; margin:8px 0 16px 0; }
.badge {
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:6px 10px;
  border-radius:999px;
  font-size:14px;
  font-weight:600;
  box-shadow: 0 1px 2px rgba(0,0,0,0.08);
  white-space:nowrap;
}
.badge .emoji { font-size:14px; margin-right:6px; }
.violet { background: linear-gradient(90deg,#7c3aed,#a78bfa); color: white; }
.yellow { background: linear-gradient(90deg,#fbbf24,#fcd34d); color: #3b3b3b; }
.badge small { font-size:12px; opacity:0.85; margin-left:6px; font-weight:500; }
</style>
"""

def badge_html(attr, value, kind="top"):
    """Return an HTML badge with title tooltip. kind in {'top','worst'}"""
    full = attr_names.get(attr, attr)
    value_text = int(value) if float(value).is_integer() else round(float(value), 1)
    if kind == "top":
        cls = "badge violet"
        emoji = "⭐"
    else:
        cls = "badge yellow"
        emoji = "🤮"  # funny puke emoji as requested
    # Title attribute provides the browser tooltip
    return f'<span class="{cls}" title="{full}"><span class="emoji">{emoji}</span><span>{attr}: <small>{value_text}</small></span></span>'

# --- Render ---
st.markdown(css, unsafe_allow_html=True)

st.write(f"### ⭐ Top {n} Attributes for {player}")
top_html = '<div class="badge-row">' + "".join(badge_html(a, v, "top") for a, v in top_n.items()) + "</div>"
st.markdown(top_html, unsafe_allow_html=True)

st.write(f"### 🤮 Worst {n} Attributes for {player}")
worst_html = '<div class="badge-row">' + "".join(badge_html(a, v, "worst") for a, v in worst_n.items()) + "</div>"
st.markdown(worst_html, unsafe_allow_html=True)
