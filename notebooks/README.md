# Notebooks Overview — Tasks 2 & 3

This folder contains Jupyter notebooks for **Task 2** (Data Profiling, Cleaning & EDA) and **Task 3** (Cross-Country Comparison).

## 📂 Files

* **`benin_eda.ipynb`**
  Data profiling, outlier detection, cleaning, time-series analysis, and visualizations for the Benin dataset.

* **`togo_eda.ipynb`**
  Data profiling, outlier detection, cleaning, time-series analysis, and visualizations for the Togo dataset.

* **`sierra_leone_eda.ipynb`**
  Data profiling, outlier detection, cleaning, time-series analysis, and visualizations for the Sierra Leone dataset.

* **`compare_countries.ipynb`**
  Aggregates cleaned data from all three countries to compute summary statistics, generate comparative plots, and perform one-way ANOVA tests on key metrics (GHI, DNI, DHI).

## 🚀 How to Run

1. Activate your Python environment with required dependencies.
2. Launch Jupyter Lab/Notebook:

   ```bash
   jupyter lab notebooks/
   ```
3. Open each notebook and execute cells sequentially to reproduce analysis and visualizations.

*All notebooks assume cleaned CSVs (`benin_clean.csv`, `togo_clean.csv`, `sierra_leone_clean.csv`) are available in the `data/` directory.*
