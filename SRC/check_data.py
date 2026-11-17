from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_excel(ROOT / "Data" / "ENB2012_data.xlsx")
print(df.shape)
print(df.head())