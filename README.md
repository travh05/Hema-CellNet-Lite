# Hema-CellNet

A minimal, hematopoietic identity classifier built on public bulk data.

## Overview

- Uses BloodSpot normal hematopoiesis data to train a 17-gene multinomial logistic regression classifier
  (SOD1, GATA2, RUNX1, TAL1, MEIS1, SPI1, MPO, ELANE, KLF1, GATA1, CSF3R, FLT3, NPM1, KIT, DNMT3A, IDH1, IDH2).
- Assigns coarse cell identities: `HSC_like`, `Erythroid`, `Myeloid`, `Bcell`, `T_NK`, `DC`.
- Applies the classifier to GSE85112 hiPSC-derived and cord-blood HSPCs.
- Computes an HSC "network fidelity" score (cosine similarity to the BloodSpot HSC centroid)
  and visualizes both samples in the BloodSpot UMAP manifold.

## Structure

- `notebooks/` – data merging, classifier training, and GSE85112 analysis.
- `src/model.py` – helper functions to score new samples.
- `data/` – small example expression matrices.
- `models/` – saved scaler + classifier.

## Quick start

```bash
git clone https://github.com/<your-username>/hema-cellnet-lite.git
cd hema-cellnet-lite
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
pip install -r requirements.txt
jupyter notebook
