# src/cleaning.py

import pandas as pd
from pathlib import Path

def load_dataset(filename, data_dir=Path.cwd().parent / "data"):
    """Load CSV from the /data folder using a provided filename."""
    path = data_dir / filename
    return pd.read_csv(path, encoding="latin-1")  # handles special chars

def drop_unnamed_columns(df):
    """Remove columns like 'Unnamed: 0' often added by Excel or index export."""
    return df.loc[:, ~df.columns.str.contains('^Unnamed')]

def clean_column_names(df):
    """Standardize column names: strip spaces, lowercase, replace symbols."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace(r'[^\w\s]', '', regex=True)
    )
    return df

def drop_empty_rows_and_columns(df):
    """Drop fully empty rows and columns."""
    return df.dropna(axis=0, how='all').dropna(axis=1, how='all')

def get_missing_value_summary(df):
    """Return missing value count per column, sorted descending."""
    return df.isnull().sum().sort_values(ascending=False)

def convert_to_datetime(df, column_name):
    """Convert a column to datetime; invalid formats become NaT."""
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df


def prepare_dataset(df):
    """Runs all core cleaning steps on the dataset."""
    df = drop_unnamed_columns(df)
    df = drop_empty_rows_and_columns(df)
    df = clean_column_names(df)
    return df

def get_df_info(df):
    """Return basic info and shape of dataframe."""
    buffer = []
    df.info(buf=buffer)
    return "\n".join(buffer), df.shape

def drop_columns(df, columns):
    """Drop a list of columns from the dataframe."""
    return df.drop(columns=columns, errors='ignore')

def fill_missing(df, strategy="mean", value=None):
    """Fill missing values based on strategy: mean, median, mode, or custom."""
    df_filled = df.copy()
    for col in df_filled.columns:
        if df_filled[col].isnull().any():
            if strategy == "mean":
                df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
            elif strategy == "median":
                df_filled[col] = df_filled[col].fillna(df_filled[col].median())
            elif strategy == "mode":
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode().iloc[0])
            elif strategy == "custom" and value is not None:
                df_filled[col] = df_filled[col].fillna(value)
    return df_filled

from sklearn.preprocessing import StandardScaler, MinMaxScaler

def apply_normalization(df, method="standard", columns=None):
    """Apply normalization or standardization to specified columns."""
    df_transformed = df.copy()
    if columns is None:
        columns = df_transformed.select_dtypes(include=['number']).columns.tolist()

    scaler = StandardScaler() if method == "standard" else MinMaxScaler()
    df_transformed[columns] = scaler.fit_transform(df_transformed[columns])
    return df_transformed

def encode_categorical(df, strategy="onehot", columns=None):
    """Encode categorical columns using one-hot or label encoding."""
    df_encoded = df.copy()
    if columns is None:
        columns = df_encoded.select_dtypes(include=['object', 'category']).columns.tolist()

    if strategy == "onehot":
        return pd.get_dummies(df_encoded, columns=columns)

    elif strategy == "label":
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in columns:
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        return df_encoded

    else:
        raise ValueError("Encoding strategy must be 'onehot' or 'label'")


def get_correlation_matrix(df, method="pearson"):
    """Return a correlation matrix (Pearson by default)."""
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.corr(method=method)

import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(corr_matrix):
    """Plot a heatmap from a correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


