# context.py

# src/context.py

from cleaning import get_missing_value_summary

def generate_context_summary(df):
    """Creates a readable summary of a dataframe's shape, columns, and missing data."""
    n_rows, n_cols = df.shape
    col_names = df.columns.tolist()
    missing = get_missing_value_summary(df).to_dict()

    missing_report = (
        "There are no missing values in this dataset."
        if all(v == 0 for v in missing.values())
        else "Missing values by column:\n" + "\n".join([f"- {k}: {v}" for k, v in missing.items() if v > 0])
    )

    return f"""
📊 This dataset has **{n_rows} rows** and **{n_cols} columns**.

🔢 Columns:
{', '.join(col_names)}

🕳️ Missing Data Summary:
{missing_report}
""".strip()
