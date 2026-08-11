from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]

RESULT_DIR = ROOT_DIR / "results" 
PLOTS_DIR = RESULT_DIR / "plots"
BOXPLOT_DIR = PLOTS_DIR / "boxplots"
HEATMAP_DIR = PLOTS_DIR / "heatmap"
BARPLOT_DIR = PLOTS_DIR / "barplot"

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LOGS_DIR = ROOT_DIR / "logs"