import streamlit as st
import pandas as pd
import json
import os
import time

st.set_page_config(page_title="🧠 Real-Time Fraud Dashboard", layout="wide")
st.title("📡 Real-Time Fraud Detection (Last 10 Transactions)")

LOG_FILE = "transactions_log.jsonl"
MAX_DISPLAY = 10

# Session state to hold live rolling window
if "transactions" not in st.session_state:
    st.session_state.transactions = pd.DataFrame()

# UI Layout
col1, col2 = st.columns([2, 1])
transactions_placeholder = col1.empty()
metrics_placeholder = col2.empty()
risk_chart_placeholder = col2.empty()

# Track last file read position
if "last_line_count" not in st.session_state:
    st.session_state.last_line_count = 0

# Loop to keep checking for new lines
while True:
    if not os.path.exists(LOG_FILE):
        time.sleep(1)
        continue

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    new_lines = lines[st.session_state.last_line_count:]
    st.session_state.last_line_count = len(lines)

    if new_lines:
        new_data = [json.loads(line) for line in new_lines]
        new_df = pd.DataFrame(new_data)

        # Append new and limit to 10 rows
        st.session_state.transactions = pd.concat(
            [st.session_state.transactions, new_df],
            ignore_index=True
        ).tail(MAX_DISPLAY)

        # Update dashboard
        transactions_placeholder.dataframe(
            st.session_state.transactions[["Time", "Amount", "fraud_prediction", "risk_category"]],
            use_container_width=True,
            hide_index=True,
            height=320
        )

        frauds = st.session_state.transactions["fraud_prediction"].sum()
        with metrics_placeholder:
            st.metric("🔢 Frauds in Last 10", value=int(frauds))

        with risk_chart_placeholder:
            st.bar_chart(
                st.session_state.transactions["risk_category"].value_counts(),
                use_container_width=True
            )

    time.sleep(1)
