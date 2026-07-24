import pandas as pd


def load_data(file_path):
    """
    Load CSV dataset.
    """
    df = pd.read_csv(file_path, encoding="latin1")
    return df


def preprocess_data(df):
    """
    Clean and preprocess the dataset.
    """

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # Remove missing dates
    df = df.dropna(subset=["Order Date", "Ship Date"])

    # Fill missing categorical values
    categorical_columns = [
        "Ship Mode",
        "Segment",
        "Country",
        "City",
        "State",
        "Region",
        "Category",
        "Sub-Category",
        "Product Name"
    ]

    for col in categorical_columns:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    # Fill numeric values
    numeric_columns = ["Sales"]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # Feature Engineering
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month Name"] = df["Order Date"].dt.strftime("%b")
    df["Quarter"] = df["Order Date"].dt.quarter
    df["Day"] = df["Order Date"].dt.day

    # Shipping Days
    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    # Sort by date
    df = df.sort_values("Order Date").reset_index(drop=True)

    return df


def get_filter_values(df):
    """
    Return unique values for dashboard filters.
    """

    return {
        "years": sorted(df["Year"].unique().tolist()),
        "regions": sorted(df["Region"].unique().tolist()),
        "states": sorted(df["State"].unique().tolist()),
        "categories": sorted(df["Category"].unique().tolist()),
        "sub_categories": sorted(df["Sub-Category"].unique().tolist()),
        "segments": sorted(df["Segment"].unique().tolist()),
        "ship_modes": sorted(df["Ship Mode"].unique().tolist())
    }


def apply_filters(
    df,
    year=None,
    region=None,
    state=None,
    category=None,
    sub_category=None,
    segment=None,
    ship_mode=None
):
    """
    Apply dashboard filters.
    """

    filtered = df.copy()

    if year:
        filtered = filtered[filtered["Year"] == int(year)]

    if region:
        filtered = filtered[filtered["Region"] == region]

    if state:
        filtered = filtered[filtered["State"] == state]

    if category:
        filtered = filtered[filtered["Category"] == category]

    if sub_category:
        filtered = filtered[
            filtered["Sub-Category"] == sub_category
        ]

    if segment:
        filtered = filtered[
            filtered["Segment"] == segment
        ]

    if ship_mode:
        filtered = filtered[
            filtered["Ship Mode"] == ship_mode
        ]

    return filtered