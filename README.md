# 10 Academy Solar Data Discovery Challenge – Week 0

Welcome to the solar data discovery project! This repository contains code and reports for Week 0 of the 10 Academy Solar Challenge. Throughout this project, we profile, clean, and analyze one year of minute-resolution solar and meteorological data from three West African sites: Benin (Malanville), Sierra Leone (Bumbuna), and Togo (Dapaong).

## 📁 Repository Structure

```
solar-challenge-week0/
├── data/                       # Raw and cleaned CSV files (not tracked)
│   ├── benin-malanville.csv
│   ├── togo-dapaong_qc.csv
│   ├── sierraleone-bumbuna.csv
│   ├── benin_clean.csv
│   └── ...
├── notebooks/                  # Exploratory notebooks by country and comparison
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── .github/                    # CI pipeline definitions
│   └── workflows/
│       └── ci.yml
├── .gitignore                  # Ignored files (data/, venv/, etc.)
├── requirements.txt            # Pinned Python dependencies
└── README.md                   # Project overview and documentation
```

## 🔧 Installation
To set up this project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/lhiwi/solar-challenge-week0.git
   cd solar-challenge-week1
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt  inside a virtual environment.
   ```
