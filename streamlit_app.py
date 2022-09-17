"""
Streamlit app - NLLB-200 translation demo for lyrics.
"""

import pandas as pd
import streamlit as st
from pathlib import Path

st.title("Eco Rating Comparator for Smartphones")

st.markdown("## What is this demo? 🤔")
st.markdown("> __*Make the most sustainable choices. Compare smartphones by Eco Rating scores with this demo app!*__")

st.markdown("""

This Streamlit demo lets you check how sustainable smartphones are and how they compare with each other easily.

You can compare around 30 smartphones.

### About the data

1. All smartphone information and Global Eco Rating scores come from the Orange website. 
2. Sub-scores are approximates. They were pre-computed automatically by converting the progress bars on the Eco Rating pictures into the corresponding numeric sub-scores.
"""
            )


# ---------- Utils

def generate_color(s1, s2):
    if s1 > s2:
        return "green", "red",
    elif s1 < s2:
        return "red", "green",
    return "black", "black",


def generate_formatting(index_model_1, index_model_2):
    # init comparator
    comp = dict()

    # fetch scores for given criteria and get right colors
    for criteria, title in sub_criterias.items():
        s1 = df[criteria][index_model_1]
        s2 = df[criteria][index_model_2]
        c1, c2 = generate_color(s1, s2)
        comp[criteria] = {
            "color_model_1": c1,
            "color_model_2": c2,
            "score_model_1": s1,
            "score_model_2": s2,
            "title": title,
        }
    return comp


def format_score_html(score: str, color: str, size: int = 30):
    return f'<center><span style="color:{color}; font-size: {size}px;">{score}</span></center>'

# ---------- Selection

st.markdown("## Compare your smartphone's Eco Rating with other devices ♻️")

# ====== load data from file ======
path_data = "data/ecoratings_final_v1.csv"
df = pd.read_csv(path_data, encoding='utf-8', delimiter=",", header=0, index_col=None)
df["model_formatted"] = df["brand"] + " " + df["model"]

# select models to compare
model_choices = df["model_formatted"].values.tolist()

select_model_1 = st.selectbox(
    'Select smartphone n°1',
    model_choices,
    index=4,
)
select_model_2 = st.selectbox(
    'Select smartphone n°2',
    model_choices,
    index=13
)
index_model_1 = model_choices.index(select_model_1)
index_model_2 = model_choices.index(select_model_2)
select_img_url_1 = df["url_image_product"][index_model_1]
select_img_url_2 = df["url_image_product"][index_model_2]
select_img_er_1 = df["url_image_ecorating"][index_model_1]
select_img_er_2 = df["url_image_ecorating"][index_model_2]

# compare scores
sub_criterias = {
    "ecorating_index": "General Score",
    "durability": "Durability",
    "reparability": "Reparability",
    "recyclability": "Recyclability",
    "climate": "Climate efficiency",
    "resources": "Resource efficiency",
}

comparator = generate_formatting(index_model_1=index_model_1, index_model_2=index_model_2)

# ---------- Phone picture
col1_img, col2_img = st.columns([1, 1])
with col1_img:
    # phone
    st.markdown(f"### {select_model_1} ")
    st.image(select_img_url_1)

with col2_img:
    # phone
    st.markdown(f"### {select_model_2} ")
    st.image(select_img_url_2)

# ---------- Summary
st.markdown(f"### <br><center>Eco Rating Summary</center>", unsafe_allow_html=True)
col1_brief, col2_brief = st.columns([1, 1])
with col1_brief:
    st.image(select_img_er_1)
with col2_brief:
    st.image(select_img_er_2)

# ---------- General scores
st.markdown(f"### <center>General Scores</center>", unsafe_allow_html=True)
col1_score, col2_score = st.columns([1, 1])
gs1 = comparator["ecorating_index"]["score_model_1"]
gs2 = comparator["ecorating_index"]["score_model_2"]
gsc1 = comparator["ecorating_index"]["color_model_1"]
gsc2 = comparator["ecorating_index"]["color_model_2"]
with col1_score:
    st.markdown(format_score_html(score=gs1, color=gsc1), unsafe_allow_html=True)
with col2_score:
    st.markdown(format_score_html(score=gs2, color=gsc2), unsafe_allow_html=True)

# ---------- sub-scores
st.markdown(f"### <br><center>Scores by Criteria</center>", unsafe_allow_html=True)
st.markdown(
    f'##### <center><span style="color:grey"><i>Generated from the above Eco Rating Summary pictures</i></span></center>',
    unsafe_allow_html=True)
for col, fm in comparator.items():
    if col != "ecorating_index":
        # st.markdown(f"##### <center>{fm['title']}</center>", unsafe_allow_html=True)
        col1_score, col2_score, col3_score = st.columns([1, 1, 1])
        with col1_score:
            st.markdown(format_score_html(score=fm["score_model_1"], color=fm["color_model_1"], size=25),
                        unsafe_allow_html=True)
        with col2_score:
            st.markdown(format_score_html(score=fm["title"], color="black", size=25), unsafe_allow_html=True)
        with col3_score:
            st.markdown(format_score_html(score=fm["score_model_2"], color=fm["color_model_2"], size=25),
                        unsafe_allow_html=True)

# ---------- More info
st.markdown(
    f"""### <br><center>More Info</center>
<center>Learn about the Eco Rating methodology on   ➡️  <a href="https://www.ecoratingdevices.com/">ecoratingdevices.com</a></center>.
"""

    , unsafe_allow_html=True

)
col1_info, col2_info, col3_info = st.columns([1, 1, 1])
pdp1 = df["url_pdp"][index_model_1]
pdp2 = df["url_pdp"][index_model_2]
rid1 = df["reparability_index_doc"][index_model_1]
rid2 = df["reparability_index_doc"][index_model_2]

with col1_info:
    st.markdown(
        f'<center><a href="{pdp1}">{select_model_1} Page</a><br><a href="{rid1}">{select_model_1} Sheet</a></center>',
        unsafe_allow_html=True)
with col2_info:
    st.markdown(f'<center><b>Product page</b></center>', unsafe_allow_html=True)
    st.markdown(f'<center><b>Reparability index doc</b></center>', unsafe_allow_html=True)
with col3_info:
    st.markdown(
        f'<center><a href="{pdp2}">{select_model_2} Page</a><br><a href="{rid2}">{select_model_2} Sheet</a></center>',
        unsafe_allow_html=True)
