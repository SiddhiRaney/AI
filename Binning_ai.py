import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

# Sample data
data = [1, 7, 5, 13, 22, 27, 45]
df = pd.DataFrame({"values": data})

print("Original Data:")
print(df)

# --- 1. Binning with pandas.cut (equal-width bins) ---
df["cut_bins"] = pd.cut(df["values"], bins=3, labels=["Low", "Medium", "High"])

# --- 2. Binning with pandas.qcut (quantile bins) ---
df["qcut_bins"] = pd.qcut(df["values"], q=3, labels=["Small", "Medium", "Large"])

# --- 3. Binning with NumPy (digitize) ---
bins = [10, 20, 30]
df["numpy_bins"] = np.digitize(df["values"], bins)

# --- 4. Binning with scikit-learn (KBinsDiscretizer) ---
X = np.array(data).reshape(-1, 1)
kb = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")
df["sklearn_bins"] = kb.fit_transform(X)

print("\nBinned Data:")
print(df)
