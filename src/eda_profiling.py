# src/eda_profiling.py
from pathlib import Path
import pandas as pd
from ydata_profiling import ProfileReport

# Paths
ROOT = Path(__file__).resolve().parents[1]  # project root
DATA_FILE = ROOT / "data" / "ObesityDataSet.csv"   # adjust filename if needed
REPORT_FILE = ROOT / "reports" / "profiling_report.html"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Generate profiling report
profile = ProfileReport(df, title="Obesity Dataset Profiling Report", explorative=True)

# Save report
profile.to_file(REPORT_FILE)
print(f"Profiling report saved to: {REPORT_FILE}")