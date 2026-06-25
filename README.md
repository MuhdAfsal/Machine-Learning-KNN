# ⚽ Football Player Pitch Role Predictor using KNN

An end-to-end Machine Learning pipeline utilizing the **K-Nearest Neighbors (KNN)** algorithm to classify football players into their primary pitch roles based on their physical and technical skill attributes. 

This project explores comprehensive data preprocessing, target feature engineering, dimensionality reduction using **Principal Component Analysis (PCA)**, hyperparameter tuning ($k$-value optimization), and model evaluation with detailed performance reports and interactive custom-player inferences.

---

## 📊 Project Overview & Dataset

The analysis is performed on a massive dataset consisting of **159,541 football players** with **89 initial columns** of data (including personal info, physical metrics, and granular player skill ratings).

### 🔍 Dataset Schema & Feature Engineering
1. **Identifier Exclusion**: Personal or redundant identifier columns such as `UID`, `Name`, `NationID`, and `PositionsDesc` are removed to prevent overfitting and leakage.
2. **Target Label Engineering (`PrimaryPosition`)**: Players have ratings across 15 separate positions. The target column `PrimaryPosition` is engineered dynamically by identifying the position where the player has their **highest rating**:
   * *Position Columns*: `Goalkeeper`, `Sweeper`, `Striker`, `AttackingMidCentral`, `AttackingMidLeft`, `AttackingMidRight`, `DefenderCentral`, `DefenderLeft`, `DefenderRight`, `DefensiveMidfielder`, `MidfielderCentral`, `MidfielderLeft`, `MidfielderRight`, `WingBackLeft`, `WingBackRight`.
3. **Broad Pitched Roles (`ROLE_MAP`)**: To reduce classification complexity and eliminate sparse classes, the 15 positions are mapped into **6 broader role classes**:

   | Original Position | Broad Pitch Role |
   | :--- | :--- |
   | `Goalkeeper` | **Goalkeeper** |
   | `Sweeper`, `DefenderCentral`, `DefenderLeft`, `DefenderRight` | **Defender** |
   | `WingBackLeft`, `WingBackRight` | **Wing Back** |
   | `DefensiveMidfielder`, `MidfielderCentral`, `MidfielderLeft`, `MidfielderRight` | **Midfielder** |
   | `AttackingMidCentral`, `AttackingMidLeft`, `AttackingMidRight` | **Attacking Mid** |
   | `Striker` | **Striker** |

---

## ⚙️ Machine Learning Pipeline

The pipeline follows standard data science best practices implemented in Python:

1. **Handling Missing Values**: Robust imputation where numerical missing values are filled with their column **median** (outlier-resilient) and categorical columns are filled with their **mode**.
2. **Date Extraction**: Converts the text `Born` date column into an integer `BirthYear` feature.
3. **Feature Standardization (`StandardScaler`)**: KNN is a distance-based algorithm (Euclidean distance). Features with larger ranges (e.g., Height) will dominate distance calculations over smaller ranges (e.g., Finisher rating). Features are scaled to have a mean of 0 and variance of 1.
4. **Train-Test Split**: Divided into an **80/20 train-test split**, **stratified** on the target labels to ensure identical class distributions are maintained across splits.
5. **Dimensionality Reduction (PCA)**: Principal Component Analysis is optionally applied to retain **95% of the variance** while significantly shrinking the feature dimensions, which accelerates the KNN inference speed.
6. **Hyperparameter Tuning ($k$-value)**: Executes the **Elbow Method** (testing a range of $k$ values) to plot accuracy vs. $k$, helping select the optimal number of neighbors.

---

## 📈 Model Performance & Evaluation

The final model achieves a **Test Accuracy of 82.63%** across **31,909 test samples**. Below is the detailed classification report:

```text
=== Classification Report ===
               precision    recall  f1-score   support

Attacking Mid       0.65      0.73      0.69      5453
     Defender       0.88      0.93      0.91      9831
   Goalkeeper       1.00      1.00      1.00      3426
   Midfielder       0.76      0.69      0.72      7659
      Striker       0.90      0.85      0.87      5323
    Wing Back       0.00      0.00      0.00       217

     accuracy                           0.83     31909
    macro avg       0.70      0.70      0.70     31909
 weighted avg       0.82      0.83      0.82     31909
```

### 🧠 Performance Insights:
* **Goalkeepers (F1-score: 1.00)**: Classified with perfect precision and recall, as goalkeeper attributes (Handling, Reflexes, etc.) are highly distinct from outfield players.
* **Defenders (F1-score: 0.91)** & **Strikers (F1-score: 0.87)**: Show very high classification accuracy, representing distinct physical/tactical roles.
* **Midfielders vs. Attacking Mids**: Suffer from slight classification overlap (lower precision/recall) due to similar technical skill distributions (Passing, Dribbling, Vision) on the pitch.
* **Wing Backs (F1-score: 0.00)**: Due to severe class imbalance (only 217 samples out of 31.9k in the test set), the model struggles to identify this specific role accurately, often misclassifying them as standard Midfielders or Defenders.

---

## 🖼️ Included Visualizations

The repository contains 7 pre-generated analytical graphs highlighting different phases of the project:
* **`graph1_class_distribution.png`**: Visualizes the player count for each of the 6 pitch roles, exposing the class imbalance.
* **`graph2_confusion_matrix.png`**: Heatmap showing predictions vs. actual roles, illustrating the overlaps between Midfielders and Attacking Mids.
* **`graph3_classification_report.png`**: Heatmap illustrating the precision, recall, and f1-score metrics for each class.
* **`graph4_pca_scree.png`**: Scree plot showing the explained variance ratio of each principal component, justifying PCA dimensionality reduction.
* **`graph5_pca_scatter.png`**: 2D scatter plot of the first two principal components, showing how the different classes cluster in low-dimensional space.
* **`graph6_accuracy_vs_k.png`**: Validation curve showing how accuracy scales across different $k$ values to find the ideal "elbow".
* **`graph7_correlation_heatmap.png`**: Detailed correlation matrix heatmap representing relationships across physical, mental, and technical skills.

---

## 📂 Repository Structure

```directory
.
├── DATASET.zip                       # Compressed raw dataset (containing player attributes)
├── graph1_class_distribution.png     # Frequency count of players in each target role
├── graph2_confusion_matrix.png       # Prediction breakdown of the model
├── graph3_classification_report.png   # Visually formatted precision, recall, F1 metrics
├── graph4_pca_scree.png              # Explained variance ratio from PCA
├── graph5_pca_scatter.png            # 2D projection of player clusters using PCA
├── graph6_accuracy_vs_k.png          # Hyperparameter tuning validation curve (Elbow Method)
├── graph7_correlation_heatmap.png    # Player attribute feature correlation heatmap
├── knn_preprocess.py                 # Script for automated preprocessing, target creation, scaling, & PCA
├── knn_preprocessing.py              # Identical automated preprocessing utility script
├── model.create_test.py              # Jupyter-style notebook script that loads, trains, tunes, and saves the model
└── model_test_output.js              # Plain-text terminal logs from executing the model script
```

---

## 🚀 Getting Started & Usage

### 1. Prerequisites & Installation
Ensure you have Python 3 installed. Clone this repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/MuhdAfsal/Machine-Learning-KNN.git
cd Machine-Learning-KNN

# Install requirements
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2. Extract Dataset
The raw data is stored in a compressed ZIP file. Unzip it before running the scripts:
```bash
unzip DATASET.zip -d .
```

### 3. Run Preprocessing & Dimensionality Reduction
You can run the preprocessing pipeline which handles data cleansing, target engineering, standard scaling, PCA reduction, and saves ready-to-train NumPy arrays:
```bash
python knn_preprocess.py
```

### 4. Train, Tune, and Save the Model
To execute the full training loop, find the best $k$ hyperparameter, generate evaluation metrics, and export the trained model (`knn_football_position.pkl`):
```bash
python model.create_test.py
```

---

## 🔮 Custom Player Inference (Example)

You can run custom predictions directly in Python using the saved model pipeline. Below is an example of predicting a player's role:

```python
import pandas as pd
import numpy as np
import pickle

# Load the saved model pipeline (Scaler + Classifier)
with open("knn_football_position.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Define custom attributes for a new player
# Missing fields will automatically fallback to the training-set median
custom_player = {
    "Pace": 18, 
    "Acceleration": 17, 
    "Finishing": 17,
    "OffTheBall": 16, 
    "Dribbling": 15, 
    "Heading": 14,
    "Passing": 10, 
    "Tackling": 5, 
    "Handling": 1,
}

# Load training feature columns for schema matching
FEATURE_COLS = [...] # List of selected numeric features used during training

# Align custom player attributes to model schema
median_values = loaded_model.named_steps['scaler'].mean_ # fallback to means/medians
row = {col: custom_player.get(col, 0.0) for col in FEATURE_COLS}
df_row = pd.DataFrame([row])

# Run inference
predicted_role = loaded_model.predict(df_row)[0]
probabilities = loaded_model.predict_proba(df_row)[0]
confidence = np.max(probabilities) * 100

print(f"🔍 Custom Player Predicted Role: {predicted_role} (Confidence: {confidence:.2f}%)")
# Output: 🔍 Custom Player Predicted Role: Striker (Confidence: 100.00%)
```

--
