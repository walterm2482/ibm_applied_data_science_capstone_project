# IBM Applied Data Science Capstone — SpaceX Falcon 9 Landing Success

Predict whether the Falcon 9 first stage lands successfully using data wrangling, EDA, geospatial viz, and ML model comparison.

---

## Repository structure
- `1_spacex_preprocessing.ipynb` — initial ingestion and cleaning  
- `2_falcon9_launches_data_wrangling.ipynb.ipynb` — feature engineering and tidy data  
- `3_spacex_launches_analysis.ipynb` — EDA and plots  
- `4_spacex_sql_queries.ipynb` — SQL-based exploration  
- `5_orbit_success.ipynb.ipynb` — success rate by orbit  
- `6_launch_site_distance_analysis.ipynb` — distance-based analysis and mapping  
- `7_spacex_dash_app.py` — Dash app for interactive exploration  
- `8_model_selection_comparison.ipynb` — train/validate LR, SVM, DT, KNN  
- `Presentation.pdf` — slide deck with methods and results

> File list based on the repository at the time of writing. :contentReference[oaicite:0]{index=0}

---

## Results (short)
- Best cross-validated score: **Decision Tree = 0.8750**.  
- Test accuracy for compared models in this run: **0.833**.  
- Confusion matrices included for DT, SVM, and KNN in notebooks and slides.

> These summaries reflect the provided notebooks and slide deck. :contentReference[oaicite:1]{index=1}

---

## Data sources
- **SpaceX API** — rockets, launches, and metadata.  
- **Wikipedia** snapshot for Falcon 9/Heavy launch tables (for scraping).  
- Some notebooks read from the API + HTML tables; no raw proprietary datasets are committed.

> Public sources referenced in the project materials; see slides for links. :contentReference[oaicite:2]{index=2}

---

## Quickstart

### 1) Prerequisites
- Python **3.10+**
- Git
- A modern browser for Jupyter and the Dash app

### 2) Setup a virtual environment
```bash
git clone https://github.com/walterm2482/ibm_applied_data_science_capstone_project.git
cd ibm_applied_data_science_capstone_project

python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
