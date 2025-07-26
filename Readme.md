# Credit Card Fraud Analysis

This project performs an in-depth analysis and modeling of credit card transactions to detect fraudulent activity using a dataset from Kaggle.

## 📊 Project Overview

The primary objective is to explore, analyze, and build models to detect fraudulent credit card transactions. The dataset is highly imbalanced and requires advanced preprocessing and model evaluation techniques to ensure robustness.

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

## 📁 Dataset

The dataset was sourced from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud). You must download it manually due to Kaggle's API and usage restrictions.

### Uploading the Dataset

1. Visit the [dataset page](https://www.kaggle.com/mlg-ulb/creditcardfraud).
2. Download `creditcard.csv`.
3. Place it in the root directory of this repository or `data/` folder.
4. Ensure the notebook path to the file is correct:
   ```python
   df = pd.read_csv('creditcard.csv')  # Update if your path differs
## 🧪 How to Run
1. Clone the repository:

```bash
git clone https://github.com/your-username/credit-card-fraud-analysis.git
cd credit-card-fraud-analysis
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Launch Jupyter:

```bash
jupyter notebook
```
4. Open Credit_Card_Fraud_Analysis.ipynb and run all cells.

## ✅ Features
-Data preprocessing and exploration

-Dealing with class imbalance

-Model training and evaluation (Logistic Regression, Random Forest, etc.)

-ROC Curve and confusion matrix visualizations

## 📌 Future Improvements
-Add deep learning models

-Use SMOTE or ADASYN for better balancing

-Deploy as a web app using Flask or Streamlit
