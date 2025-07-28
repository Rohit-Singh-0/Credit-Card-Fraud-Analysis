# Credit-Card Fraud Analysis & Detection Pipeline

Detecting fraudulent card transactions quickly can save issuers millions of dollars in charge-backs and lost trust.  
This project builds a production-ready pipeline that ingests raw transaction data, trains machine-learning models, and serves real-time fraud probabilities through a FastAPI micro-service.

## 🗂️ Repository Structure
.
├── data/ # Small sample for demo; full 150 MB dataset excluded
├── notebooks/
│ └── Fraud_Analysis_Notebook.ipynb
├── src/
│ └── app/ # FastAPI service & preprocessing utilities
├── models/ # Trained pickle artifacts
├── reports/
│ ├── Fraud_Report.pdf # Executive deck
│ └── tableau/ # Dashboard files
└── requirements.txt


## 1. Dataset
| Property  | Value |
|-----------|-------|
| Rows      | 284,807 |
| Fraud share | 0.17 % |
| Features  | 28 PCA-anonymized variables + `Time`, `Amount` |

## 2. End-to-End Workflow
1. **Exploratory Data Analysis** — understand class imbalance and feature distributions  
2. **Pre-processing** — standardize numeric features, handle imbalance via SMOTE  
3. **Modeling** — Logistic Regression & Random Forest with randomized grid-search  
4. **Evaluation** — ROC-AUC, precision-recall, and cost-based threshold analysis  
5. **Serialization** — persist best model and scaler as pickles  
6. **Deployment** — expose `/predict` endpoint with FastAPI  

![Pipeline](reports/readme_assets/pipeline.png)

## 3. Results

| Model                | ROC-AUC | Recall @ 3 % FPR | Precision (Top 0.5 %) | Train time |
|----------------------|---------|------------------|-----------------------|------------|
| Logistic Regression  | 0.982   | 0.81             | 0.76                  | < 1 s      |
| Random Forest (best) | **0.9993** | **0.88**       | **0.84**             | 28 s       |

**Business impact**  
Flagging only the top 0.5 % of transactions by model score captures 88 % of known fraud, reducing analyst reviews by ~40 % while missing just 12 % of fraudulent cases.

## 4. Quick Start

1. Install dependencies
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

2. Run API locally
uvicorn src.app.main:app --reload

3. Score a single transaction
curl -X POST "http://127.0.0.1:8000/predict"
-H "Content-Type: application/json"
-d '@/path/to/sample_transaction.json'


Example response
{
"fraud_probability": 0.9978,
"is_fraud_flag": 1
}


## 5. Visualization Assets
* **Fraud_Report.pdf** — 16-page slide deck for stakeholders (EDA, KPI tables, cost curve)  
* **Tableau Dashboard** — interactive view of fraud geography, hourly patterns, and model thresholds  

## 6. Project Highlights
* Handles extreme class imbalance with **SMOTE** & threshold tuning  
* **Reproducible:** fixed random seeds, clean notebook ordering, `requirements.txt`  
* **Production-minded:** FastAPI micro-service + pickled models ready for containerization  
* **Storytelling:** executive PDF and Tableau dashboard for non-technical audiences  

## 7. Next Steps
- Integrate an XGBoost model to benchmark additional tree-based performance  
- Batch-score streaming data via AWS Lambda + S3 event triggers  
- Add unit tests (`pytest`) for `utils.py` and API endpoints  
- Implement model-drift monitoring with EvidentlyAI  

## 8. Acknowledgements
Dataset originally released by Dal Pozzolo et al. and hosted on Kaggle (European card transactions, 2013).  
Code authored by **Rohit Singh**.
