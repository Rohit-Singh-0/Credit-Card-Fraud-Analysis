import streamlit as st
import pandas as pd
import time
import json

st.set_page_config(page_title="Live Fraud Monitor", layout="wide")
st.title("📡 Live Credit Card Fraud Monitoring")

placeholder = st.empty()
fraud_log = "transactions_log.jsonl"


@st.cache_data(ttl=1)
def load_data():
    try:
        with open(fraud_log, "r") as f:
            data = [json.loads(line) for line in f.readlines()]
        return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame()


# Update every few seconds
while True:
    df = load_data()

    if not df.empty:
        st.subheader("Last 10 Transactions")
        st.dataframe(df.tail(10).sort_index(ascending=False), use_container_width=True)

        st.subheader("🔢 Fraud Count")
        col1, col2 = st.columns(2)
        col1.metric("Total Transactions", len(df))
        col2.metric("Frauds Detected", df['fraud_prediction'].sum())

        st.subheader("📊 Risk Category Distribution")
        st.bar_chart(df["risk_category"].value_counts())

        st.subheader("📈 Fraud Over Time")
        frauds = df[df["fraud_prediction"] == 1]
        if not frauds.empty:
            frauds["Time (rounded)"] = frauds["Time"].astype(int) // 100
            st.line_chart(frauds["Time (rounded)"].value_counts().sort_index())

    time.sleep(2)
    placeholder.empty()
