import numpy as np
import joblib
import pandas as pd

gene_cols = ["SOD1","GATA2","RUNX1","TAL1","MEIS1","SPI1","MPO","ELANE",
             "KLF1","GATA1","CSF3R","FLT3","NPM1","KIT","DNMT3A","IDH1","IDH2"]

scaler = joblib.load("models/hematology_panel_scaler.joblib")
clf = joblib.load("models/hematology_panel_logreg.joblib")

def score_sample(expr_dict):
    """expr_dict: {gene: expression} with the 17 genes."""
    x = np.array([[expr_dict[g] for g in gene_cols]])
    x_scaled = scaler.transform(x)
    proba = clf.predict_proba(x_scaled)[0]
    pred  = clf.predict(x_scaled)[0]
    return pred, dict(zip(clf.classes_, proba))
