# app.py  — RUN THIS FILE WITH:  streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import root_mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title= 'COVID-19 Time Series', page_icon="🦠", layout='centered')
st.title('COVID-19 Time Series')

st.write("This demo loads a local CSV of **daily case counts**, creates a time series, "
         "splits it chronologically (80/20), then compares a **Naïve Baseline** to **ARIMA(1,1,1)**.")

# === CONFIG ===
DATA_PATH = '/Users/Marcy_Student/DA2025_Lectures/Mod6/data/covid.csv'  
DATE_COL  = ['date_of_interest']
TARGET_COL = ['case_count']

# === LOAD CSV (RUN THIS SECTION WITHOUT CHANGES if your columns match) ===
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    st.error(None)
    st.stop()

#lowercase columns and strip white space
df.columns = df.columns.str.lower().str.strip()
date_col = DATE_COL[0].lower()
target_col = TARGET_COL[0].lower()

if date_col not in df.columns or target_col not in df.columns:
    st.error(f"Expected columns `{DATE_COL}` and `{TARGET_COL}` not found. "
             f"Got columns: {df.columns.tolist()}")
    st.stop()

# Parse date and coerce numeric (strip commas like '1,141')
df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df[target_col] = pd.to_numeric(df[target_col].astype(str).str.replace(",", "", regex=False), errors="coerce")
df = df.dropna(subset=[date_col, target_col]).sort_values(date_col)

st.caption(f"Data range: {df[date_col].min().date()} → {df[date_col].max().date()}  |  "
           f"Rows: {len(df):,}")

# === BUILD DAILY SERIES ===
#set date index and make sure it is Daily frequency
s = pd.Series(df[target_col].values, index=df[date_col])
s = s.astype("float64").interpolate("linear")  # fill small gaps

# === SPLIT CHRONOLOGICALLY (80/20)  ===
split_idx = int(len(s) * 0.80)
train = s.iloc[:split_idx]
test  = s.iloc[split_idx:]

st.write(f"**Train:** {train.index.min().date()} → {train.index.max().date()}  |  n = {len(train):,}")
st.write(f"**Test :** {test.index.min().date()} → {test.index.max().date()}   |  n = {len(test):,}")

# === BASELINE (Naïve/Shift)===
baseline_pred = pd.Series(train.iloc[-1], index=test.index)
rmse_baseline = root_mean_squared_error(test, baseline_pred)

# === ARIMA(1,1,1) (RUN THIS SECTION WITHOUT CHANGES) ===
try:
    arima_model = ARIMA(train, order=(1, 1, 1)).fit()
    arima_pred = arima_model.forecast(steps=len(test))
    rmse_arima = root_mean_squared_error(test, arima_pred)
except Exception as e:
    st.error(f"ARIMA failed to fit/forecast: {e}")
    st.stop()

# === METRICS (RUN THIS SECTION WITHOUT CHANGES) ===
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Baseline RMSE", value=f"{rmse_baseline:,.3f}")
with col2:
    st.metric(label="ARIMA(1,1,1) RMSE", value=f"{rmse_arima:,.3f}")

# === PLOTS (RUN THIS SECTION WITHOUT CHANGES) ===
st.subheader("Train / Test / Forecasts")

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(train, label="Train")
ax.plot(test, label="Actual (Test)", color="#ff7f0e")
ax.plot(baseline_pred, label="Baseline Forecast", color="#2ca02c", ls="--")
ax.plot(arima_pred, label="ARIMA(1,1,1) Forecast", color="#1f77b4", ls="--")
ax.set_title("Daily Case Counts: Baseline vs ARIMA")
ax.legend()
st.pyplot(fig)

with st.expander("Peek at head of cleaned data:"):
    st.dataframe(df.head(10))

st.info("**Interpretation tip:** If ARIMA RMSE < Baseline RMSE, the model beats the naive forecast. "
        "If not, revisit stationarity, seasonality (SARIMA), or recent structure changes.")
