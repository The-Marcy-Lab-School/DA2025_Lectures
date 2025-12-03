# app.py
import streamlit as st
import joblib, json, numpy as np, pandas as pd

st.set_page_config(page_title="Penguin Predictor", page_icon="🐧", layout="centered")
st.title("🐧 Penguin Species Predictor")


@st.cache_resource
def load_model():
    return joblib.load("penguin_model.pkl")

@st.cache_data
def load_meta():
    with open("penguin_meta.json", "r") as f:
        return json.load(f)

model = load_model()
meta = load_meta()

st.caption(
    f"Model trained on TRAIN split; evaluated on TEST. "
    f"Reported TEST accuracy: **{meta.get('test_accuracy', 'n/a'):.3f}**"
)

# Sidebar inputs

st.sidebar.header("Input Features")

bl = st.sidebar.slider(
    "Bill Length (mm)",
    float(meta["bill_length_mm"][0]),
    float(meta["bill_length_mm"][1]),
    float(meta["bill_length_default"]),
    step=1.0
)

fl = st.sidebar.slider(
    "Flipper Length (mm)",
    float(meta["flipper_length_mm"][0]),
    float(meta["flipper_length_mm"][1]),
    float(meta["flipper_length_default"]),
    step=1.0
)

species_hint = st.sidebar.selectbox("Show example image for:", meta["classes"], index=0)
go = st.sidebar.button("Predict")

# Output columns


col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Inputs")
    st.dataframe(pd.DataFrame([{
        "bill_length_mm": bl,
        "flipper_length_mm": fl
    }]), use_container_width=True)

with col2:
    st.subheader("Prediction")
    if go:
        X = np.array([[bl, fl]])
        pred = model.predict(X)[0]
        proba = model.predict_proba(X)[0]

        st.success(f"Predicted species: **{pred}**")
        st.caption("Class probabilities:")
        for c, p in zip(model.classes_, proba):
            st.write(f"- {c}: {p:.3f}")
    else:
        st.info("Adjust sliders and click **Predict** in the sidebar.")

st.divider()
st.subheader("Example Species Image")

species_images = {
    "Adelie": "https://i.pinimg.com/736x/5b/90/e3/5b90e3c71d0cbe2a818c2ee333066bf1.jpg",
    "Chinstrap": "https://i.pinimg.com/1200x/c3/10/51/c31051d170563790cbab6430f2d3fe8d.jpg",
    "Gentoo": "https://i.pinimg.com/736x/76/08/46/760846a08dfa64552896c44817ed729f.jpg"
}

# Pick correct image based on selected species
img_url = species_images.get(species_hint, species_images["Gentoo"])

st.image(
    img_url,
    caption=f"Example: {species_hint}",
    width=250
)