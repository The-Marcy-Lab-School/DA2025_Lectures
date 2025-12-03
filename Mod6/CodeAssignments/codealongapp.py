# app.py
import streamlit as st
import joblib, json, numpy as np, pandas as pd

st.set_page_config(page_title='Penguin Classifier', page_icon="🐧", layout="centered")
st.title('Penguin Classifier')

@st.cache_resource
def load_model():
    return joblib.load("penguin_model.pkl") #use joblin.load 

@st.cache_data
def load_meta():
    return json.load(open("penguin_meta.json")) #use json.load 

model = load_model() #call the function that loads the model
meta = load_meta()

st.caption(f"Model trained on TRAIN split; evaluated on TEST. Reported TEST accuracy: **{meta.get('test_accuracy', 'n/a')}**")

# --- Sidebar inputs ---
st.sidebar.header("Input Features")
bl = st.sidebar.slider(
   'Bill Length (mm)', 
    float(meta['bill_length_mm'][0]),
    float(meta['bill_length_mm'][1]),
    float(meta['bill_length_default']), step=1.0
)
fl = st.sidebar.slider(
    'Flipper Length (mm)',
    float(meta["flipper_length_mm"][0]), float(meta["flipper_length_mm"][1]),
    float(meta["flipper_length_default"]), step=1.0
)

species_hint = st.sidebar.selectbox("Show example image for:", meta["classes"], index=0)
go = st.sidebar.button("Predict")

# --- Two columns for outputs ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Inputs")
    st.dataframe(pd.DataFrame([{
        'bill_length_mm': bl, #name of input columns as a str
        'flipper_length_mm': fl
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
#change the placeholder image if you like 
st.image(
    f"https://placehold.co/600x300?text={species_hint}",
    caption=f"Placeholder image: {species_hint}",
    use_column_width=True
)
