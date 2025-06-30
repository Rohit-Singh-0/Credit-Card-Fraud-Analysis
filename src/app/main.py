from fastapi import FastAPI
from schema import TransactionInput
import joblib
import numpy as np
import pandas as pd
import json
# Load model and scaler
model = joblib.load("../../models/Random_Forest_Model.pkl")
scaler = joblib.load("../../models/Robust_Scaler.pkl")

app = FastAPI(title="Real-Time Fraud Detection API")

with open("feature_order.json") as f:
    feature_order = json.load(f)

# Risk thresholds
def classify_risk(prob):
    if prob < 0.1:
        return "Low"
    elif prob < 0.3:
        return "Medium"
    elif prob < 0.7:
        return "High"
    else:
        return "Critical"

@app.get("/")
def read_root():
    return {"message": "Fraud Detection API is live."}

@app.post("/predict/")
def predict(transaction: TransactionInput):
    df = pd.DataFrame([transaction.dict()])

    df["Amount_log"] = np.log1p(df["Amount"])
    df["hour"] = df["Time"] // 3600

    # Arrange columns in same order used during training
    # feature_order = [
    #     'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    #     'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    #     'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
    #     'Amount_log', 'hour'
    # ]
    df = df[feature_order]

    X_scaled = scaler.transform(df)
    pred = model.predict(X_scaled)[0]
    prob = model.predict_proba(X_scaled)[0][1]

    return {
        "fraud_probability": round(prob, 4),
        "risk_category": classify_risk(prob),
        "fraud_prediction": int(pred)
    }
