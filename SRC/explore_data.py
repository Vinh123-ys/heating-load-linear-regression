from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_excel(ROOT / "Data" / "ENB2012_data.xlsx")

print("Kích thước:", df.shape)
print("\nKiểu dữ liệu:")
df.info()
print("\nThống kê mô tả:")
print(df.describe().round(2))
print("\nGiá trị thiếu mỗi cột:")
print(df.isnull().sum())
print("\nCác giá trị của X6 (orientation):")
print(df["X6"].value_counts().sort_index())
print("\nCác giá trị của X8 (glazing distribution):")
print(df["X8"].value_counts().sort_index())
print("\nTương quan với Y1:")
print(df.corr()["Y1"].sort_values(ascending=False).round(3))