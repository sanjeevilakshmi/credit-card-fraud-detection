import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
import xgboost as xgb

# Load dataset
file_path = "CC_Datasets.csv"  # Replace with your file path
dataset = pd.read_csv(file_path)

# Data preprocessing
# Convert transaction date to datetime and extract features
dataset['trans_date_trans_time'] = pd.to_datetime(dataset['trans_date_trans_time'])
dataset['hour'] = dataset['trans_date_trans_time'].dt.hour
dataset['day'] = dataset['trans_date_trans_time'].dt.day
dataset['month'] = dataset['trans_date_trans_time'].dt.month

def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on the Earth."""
    R = 6371  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

# Calculate distance between customer and merchant locations
dataset['distance'] = haversine(
    dataset['lat'], dataset['long'], dataset['merch_lat'], dataset['merch_long']
)

# Drop irrelevant columns
columns_to_drop = ['slno', 'first', 'last', 'street', 'trans_date_trans_time', 
                   'trans_num', 'cc_num', 'zip', 'lat', 'long', 'merch_lat', 'merch_long']
dataset.drop(columns=columns_to_drop, inplace=True)

# Encode all categorical variables
for column in dataset.columns:
    if dataset[column].dtype == 'object':
        le = LabelEncoder()
        dataset[column] = le.fit_transform(dataset[column])

# Separate features and target
X = dataset.drop(columns=['is_fraud'])
y = dataset['is_fraud']

# Handle class imbalance using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_resampled)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_resampled, test_size=0.2, random_state=42)

# Hyperparameter tuning for XGBoost
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7, 10],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0]
}

xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=3, n_jobs=-1, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Evaluate the model
y_pred = best_model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the best model
import joblib
joblib.dump(best_model, "fraud_detection_xgb_best_model.pkl")

# To load the model later
# model = joblib.load("fraud_detection_xgb_best_model.pkl")
