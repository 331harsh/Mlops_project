import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import numpy as np

def load_data(path):
    # Load CSV and treat common missing placeholders
    df = pd.read_csv(path, na_values=["N/A", "NA", "", " ", "n/a"])
    return df

def _clean_basic(df):
    df = df.copy()
    # drop id if present
    if 'id' in df.columns:
        df = df.drop(columns=['id'])
    # strip whitespace and normalize categorical values
    for c in df.select_dtypes(include=['object']).columns:
        df[c] = df[c].astype(str).str.strip()
        df.loc[df[c].str.lower().isin(['nan', 'none', 'na', 'n/a']), c] = np.nan
    return df

def preprocess(df):
    """
    Returns X, y, preprocessor for pipeline.
    """
    df = _clean_basic(df)

    if 'stroke' not in df.columns:
        raise ValueError("Dataset must contain 'stroke' column")

    # Ensure numeric coercion
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['hypertension'] = pd.to_numeric(df['hypertension'], errors='coerce').fillna(0).astype(int)
    df['heart_disease'] = pd.to_numeric(df['heart_disease'], errors='coerce').fillna(0).astype(int)
    df['avg_glucose_level'] = pd.to_numeric(df['avg_glucose_level'], errors='coerce')
    df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')

    y = df['stroke'].astype(int)
    X = df.drop(columns=['stroke'])

    cat_cols = X.select_dtypes(include=['object']).columns.tolist()
    num_cols = X.select_dtypes(include=['number']).columns.tolist()

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols),
    ])

    return X, y, preprocessor

def train_test_split_df(X, y, test_size=0.2, random_state=42):
    stratify = y if len(y.unique()) > 1 and len(y) >= 4 else None
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=stratify)
