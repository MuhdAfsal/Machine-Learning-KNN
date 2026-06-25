"""
KNN Classification Preprocessing Pipeline
Dataset: Football Player Attributes (159,541 players, 89 columns)

This script preprocesses the dataset and prepares it for a KNN classifier.
The target variable is the player's PRIMARY POSITION, derived from position
rating columns (Goalkeeper, Striker, DefenderCentral, etc.).

Steps:
  1. Load & inspect data
  2. Drop irrelevant/identifier columns
  3. Engineer the target label (primary position)
  4. Handle missing values
  5. Encode date columns
  6. Feature selection (skill/attribute columns)
  7. Train-test split
  8. Feature scaling (critical for KNN — it is distance-based)
  9. Optional: dimensionality reduction with PCA
 10. Save preprocessed arrays ready for KNN
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 1: Loading data")
print("=" * 60)

df = pd.read_csv("dataset.csv")
print(f"Original shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}\n")

# ─────────────────────────────────────────────
# 2. DROP IRRELEVANT / IDENTIFIER COLUMNS
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 2: Dropping identifier/irrelevant columns")
print("=" * 60)

# These columns are identifiers or free-text — not useful as features
drop_cols = ["UID", "Name", "NationID", "PositionsDesc"]
df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True)
print(f"Dropped: {drop_cols}")
print(f"Shape after drop: {df.shape}\n")

# ─────────────────────────────────────────────
# 3. ENGINEER TARGET LABEL (Primary Position)
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 3: Engineering target label — Primary Position")
print("=" * 60)

# Position columns have a rating (higher = more suited to that role).
# We pick the position with the highest rating as the player's primary role.
position_cols = [
    "Goalkeeper", "Sweeper", "Striker",
    "AttackingMidCentral", "AttackingMidLeft", "AttackingMidRight",
    "DefenderCentral", "DefenderLeft", "DefenderRight",
    "DefensiveMidfielder", "MidfielderCentral", "MidfielderLeft",
    "MidfielderRight", "WingBackLeft", "WingBackRight"
]

df["PrimaryPosition"] = df[position_cols].idxmax(axis=1)
print("Position label distribution:")
print(df["PrimaryPosition"].value_counts())
print()

# Encode the target as integer labels
le = LabelEncoder()
df["PrimaryPosition_encoded"] = le.fit_transform(df["PrimaryPosition"])
print(f"Classes: {list(le.classes_)}")
print(f"Encoded values: {list(range(len(le.classes_)))}\n")

# ─────────────────────────────────────────────
# 4. HANDLE MISSING VALUES
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 4: Handling missing values")
print("=" * 60)

print("Missing values before treatment:")
missing = df.isnull().sum()
print(missing[missing > 0])

# Fill numeric NaNs with column median (robust to outliers)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill remaining object NaNs with mode
object_cols = df.select_dtypes(include=["object"]).columns
for col in object_cols:
    if df[col].isnull().any():
        df[col].fillna(df[col].mode()[0], inplace=True)

print("Missing values after treatment:", df.isnull().sum().sum(), "\n")

# ─────────────────────────────────────────────
# 5. ENCODE DATE / STRING COLUMNS
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 5: Encoding date/string columns")
print("=" * 60)

if "Born" in df.columns:
    # Extract birth year as an integer feature
    df["BirthYear"] = pd.to_datetime(df["Born"], errors="coerce").dt.year
    df["BirthYear"].fillna(df["BirthYear"].median(), inplace=True)
    df.drop(columns=["Born"], inplace=True)
    print("'Born' → 'BirthYear' (integer year extracted)")

print(f"Remaining object columns: {df.select_dtypes('object').columns.tolist()}\n")

# ─────────────────────────────────────────────
# 6. FEATURE SELECTION
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 6: Selecting features")
print("=" * 60)

# Use all numeric columns as features EXCEPT:
# - the raw position rating columns (they define the label — data leakage!)
# - the encoded target itself
exclude_from_features = position_cols + ["PrimaryPosition_encoded"]
exclude_from_features = [c for c in exclude_from_features if c in df.columns]

feature_cols = [
    c for c in df.select_dtypes(include=[np.number]).columns
    if c not in exclude_from_features
]

print(f"Number of features selected: {len(feature_cols)}")
print(f"Features: {feature_cols}\n")

X = df[feature_cols].values
y = df["PrimaryPosition_encoded"].values

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}\n")

# ─────────────────────────────────────────────
# 7. TRAIN-TEST SPLIT
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 7: Train-test split (80/20, stratified)")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y       # preserve class distribution in both splits
)

print(f"Train samples: {X_train.shape[0]}")
print(f"Test  samples: {X_test.shape[0]}\n")

# ─────────────────────────────────────────────
# 8. FEATURE SCALING  ← CRITICAL FOR KNN
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 8: Scaling features (StandardScaler)")
print("=" * 60)

# KNN uses Euclidean distance — unscaled features dominate the distance metric.
# We fit ONLY on training data and transform both train and test.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

print("Scaling complete.")
print(f"Train mean (first 5 features): {X_train_scaled[:, :5].mean(axis=0).round(4)}")
print(f"Train std  (first 5 features): {X_train_scaled[:, :5].std(axis=0).round(4)}\n")

# ─────────────────────────────────────────────
# 9. OPTIONAL: PCA DIMENSIONALITY REDUCTION
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 9: Optional PCA (retaining 95% variance)")
print("=" * 60)

# With 159k samples and many features, PCA speeds up KNN significantly.
# Comment this block out if you want to use all features.
pca = PCA(n_components=0.95, random_state=42)  # keep 95% variance
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca  = pca.transform(X_test_scaled)

print(f"Components before PCA : {X_train_scaled.shape[1]}")
print(f"Components after  PCA : {X_train_pca.shape[1]}")
print(f"Variance retained     : {pca.explained_variance_ratio_.sum():.4f}\n")

# ─────────────────────────────────────────────
# 10. SUMMARY & READY-TO-USE ARRAYS
# ─────────────────────────────────────────────
print("=" * 60)
print("STEP 10: Final preprocessed arrays")
print("=" * 60)

print(f"X_train_scaled  (no PCA) : {X_train_scaled.shape}")
print(f"X_test_scaled   (no PCA) : {X_test_scaled.shape}")
print(f"X_train_pca     (PCA)    : {X_train_pca.shape}")
print(f"X_test_pca      (PCA)    : {X_test_pca.shape}")
print(f"y_train                  : {y_train.shape}")
print(f"y_test                   : {y_test.shape}")
print(f"Classes                  : {list(le.classes_)}\n")

# ─────────────────────────────────────────────
# EXAMPLE: FIT A KNN MODEL RIGHT AWAY
# ─────────────────────────────────────────────
print("=" * 60)
print("BONUS: Quick KNN fit on PCA-reduced data")
print("=" * 60)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# Rule of thumb for k: sqrt(n_train)
k = int(np.sqrt(X_train_pca.shape[0]))
k = k if k % 2 != 0 else k + 1   # ensure k is odd to avoid ties
print(f"Using k = {k}")

knn = KNeighborsClassifier(
    n_neighbors=k,
    metric="euclidean",
    n_jobs=-1           # use all CPU cores
)
knn.fit(X_train_pca, y_train)

y_pred = knn.predict(X_test_pca)

print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ─────────────────────────────────────────────
# SAVE PREPROCESSED DATA (optional)
# ─────────────────────────────────────────────
np.save("X_train_scaled.npy", X_train_scaled)
np.save("X_test_scaled.npy",  X_test_scaled)
np.save("X_train_pca.npy",    X_train_pca)
np.save("X_test_pca.npy",     X_test_pca)
np.save("y_train.npy",        y_train)
np.save("y_test.npy",         y_test)
print("\nPreprocessed arrays saved as .npy files.")
