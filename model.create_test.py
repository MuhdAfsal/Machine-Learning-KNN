
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
)
from sklearn.pipeline import Pipeline
import joblib
import warnings
warnings.filterwarnings("ignore")

print("✅ All libraries imported successfully!")


# --- CELL 3: Upload & Load Dataset ---
# Run this cell to upload your dataset.csv from your local machine.
from google.colab import files

print("Please upload your dataset.csv file...")
uploaded = files.upload()   # <-- a file picker will appear

df = pd.read_csv("dataset.csv")
print(f"✅ Dataset loaded — {df.shape[0]:,} rows × {df.shape[1]} columns")
df.head()


# --- CELL 4: Explore the Dataset ---
print("=== Dataset Info ===")
print(df.info())

print("\n=== Null Values ===")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\n=== Basic Stats (numeric) ===")
print(df.describe())


# --- CELL 5: Feature Engineering — derive primary position label ---
POSITION_COLS = [
    "Goalkeeper", "Sweeper", "Striker",
    "AttackingMidCentral", "AttackingMidLeft", "AttackingMidRight",
    "DefenderCentral", "DefenderLeft", "DefenderRight",
    "DefensiveMidfielder", "MidfielderCentral", "MidfielderLeft",
    "MidfielderRight", "WingBackLeft", "WingBackRight",
]

# Each position column holds a numeric rating; pick the highest as the label.
df["PrimaryPosition"] = df[POSITION_COLS].idxmax(axis=1)

# Drop players where all position ratings are equal (ambiguous)
df = df[df[POSITION_COLS].nunique(axis=1) > 1].copy()

print("Position distribution:")
print(df["PrimaryPosition"].value_counts())

# Optional: group into broader roles to avoid tiny classes
ROLE_MAP = {
    "Goalkeeper":           "Goalkeeper",
    "Sweeper":              "Defender",
    "DefenderCentral":      "Defender",
    "DefenderLeft":         "Defender",
    "DefenderRight":        "Defender",
    "WingBackLeft":         "Wing Back",
    "WingBackRight":        "Wing Back",
    "DefensiveMidfielder":  "Midfielder",
    "MidfielderCentral":    "Midfielder",
    "MidfielderLeft":       "Midfielder",
    "MidfielderRight":      "Midfielder",
    "AttackingMidCentral":  "Attacking Mid",
    "AttackingMidLeft":     "Attacking Mid",
    "AttackingMidRight":    "Attacking Mid",
    "Striker":              "Striker",
}
df["Role"] = df["PrimaryPosition"].map(ROLE_MAP)

print("\nBroad role distribution:")
print(df["Role"].value_counts())


# --- CELL 6: Prepare Features & Target ---
# Player skill attributes used as features (drop IDs, names, dates, positions)
DROP_COLS = ["UID", "Name", "NationID", "Born", "PositionsDesc", "PrimaryPosition"] + POSITION_COLS

FEATURE_COLS = [c for c in df.select_dtypes(include=[np.number]).columns
                if c not in DROP_COLS]

print(f"Using {len(FEATURE_COLS)} features: {FEATURE_COLS}")

X = df[FEATURE_COLS].fillna(df[FEATURE_COLS].median())
y = df["Role"]

print(f"\nFeature matrix shape : {X.shape}")
print(f"Target shape         : {y.shape}")
print(f"Classes              : {sorted(y.unique())}")


# --- CELL 7: Train / Test Split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print(f"Training samples : {len(X_train):,}")
print(f"Test samples     : {len(X_test):,}")


# --- CELL 8: Build KNN Pipeline (Scaler + KNN) ---
# StandardScaler is critical for KNN — distance-based algorithms
# are sensitive to feature scale.

knn_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn",    KNeighborsClassifier(
        n_neighbors=7,       # k — tune this in Cell 9
        metric="euclidean",  # try "manhattan" or "minkowski" too
        weights="distance",  # nearer neighbours vote more strongly
        n_jobs=-1,           # use all CPU cores
    )),
])

knn_pipeline.fit(X_train, y_train)
print("✅ KNN model trained!")


# --- CELL 9: Find the Best k (Elbow Method) ---
k_range = range(1, 26, 2)   # odd k values to avoid ties
cv_scores = []

for k in k_range:
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=k, weights="distance", n_jobs=-1)),
    ])
    scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="accuracy", n_jobs=-1)
    cv_scores.append(scores.mean())
    print(f"  k={k:2d} → CV Accuracy: {scores.mean():.4f} ± {scores.std():.4f}")

best_k = list(k_range)[np.argmax(cv_scores)]
print(f"\n🏆 Best k = {best_k} (CV Accuracy = {max(cv_scores):.4f})")

plt.figure(figsize=(8, 4))
plt.plot(list(k_range), cv_scores, marker="o", color="royalblue")
plt.axvline(best_k, color="red", linestyle="--", label=f"Best k={best_k}")
plt.xlabel("Number of Neighbours (k)")
plt.ylabel("Cross-Val Accuracy")
plt.title("KNN — Elbow Curve")
plt.legend()
plt.tight_layout()
plt.savefig("elbow_curve.png", dpi=150)
plt.show()
print("📊 Elbow curve saved as elbow_curve.png")


# --- CELL 10: Retrain with Best k ---
best_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn",    KNeighborsClassifier(
        n_neighbors=best_k,
        metric="euclidean",
        weights="distance",
        n_jobs=-1,
    )),
])
best_pipeline.fit(X_train, y_train)
print(f"✅ Model retrained with k={best_k}")


# --- CELL 11: Evaluate on Test Set ---
y_pred = best_pipeline.predict(X_test)

print(f"Test Accuracy : {accuracy_score(y_test, y_pred):.4f}\n")
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=sorted(y.unique()))
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(y.unique()))
disp.plot(ax=ax, cmap="Blues", colorbar=False)
plt.title("KNN — Confusion Matrix (Test Set)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.show()
print("📊 Confusion matrix saved as confusion_matrix.png")


# --- CELL 12: Save (Serialize) the Model ---
MODEL_PATH = "knn_football_position.pkl"
joblib.dump(best_pipeline, MODEL_PATH)
print(f"✅ Model saved to {MODEL_PATH}")

# Download the model file to your local machine
from google.colab import files
files.download(MODEL_PATH)
files.download("elbow_curve.png")
files.download("confusion_matrix.png")


# --- CELL 13: Load Model & Run Inference (Deployment) ---
# This cell simulates how you would load the saved model later and predict.

loaded_model = joblib.load(MODEL_PATH)

# Example: predict the role of the first 5 test players
sample = X_test.iloc[:5]
predictions = loaded_model.predict(sample)
probabilities = loaded_model.predict_proba(sample)

print("=== Sample Predictions ===")
results = pd.DataFrame({
    "Actual Role"    : y_test.iloc[:5].values,
    "Predicted Role" : predictions,
    "Confidence (%)" : [f"{p.max()*100:.1f}" for p in probabilities],
})
print(results.to_string(index=False))


# --- CELL 14: Predict for a Custom Player ---
# Fill in attribute values for any player you want to classify.

def predict_player_role(attribute_dict: dict) -> str:
    """
    Pass a dict of {feature_name: value} for any subset of features.
    Missing features default to the training-set median.
    """
    median_values = X_train.median().to_dict()
    row = {col: attribute_dict.get(col, median_values[col]) for col in FEATURE_COLS}
    df_row = pd.DataFrame([row])
    role = loaded_model.predict(df_row)[0]
    proba = loaded_model.predict_proba(df_row)[0]
    confidence = proba.max() * 100
    return role, confidence

# Example — a pacey, clinical finisher
custom_player = {
    "Pace": 18, "Acceleration": 17, "Finishing": 17,
    "OffTheBall": 16, "Dribbling": 15, "Heading": 14,
    "Passing": 10, "Tackling": 5, "Handling": 1,
}
role, conf = predict_player_role(custom_player)
print(f"\n🔍 Custom player predicted role : {role}  (confidence: {conf:.1f}%)")


print("\n✅ All done! Your KNN model is trained, evaluated, and ready to use.")