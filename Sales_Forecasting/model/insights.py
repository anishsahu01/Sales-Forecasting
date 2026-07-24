import pandas as pd


def generate_insights(df, forecast_summary):
    """
    Generate AI-powered business insights for the dashboard.
    """

    insights = {}

    # ===========================
    # Total Sales
    # ===========================

    insights["total_sales"] = round(df["Sales"].sum(), 2)

    # ===========================
    # Total Orders
    # ===========================

    insights["total_orders"] = len(df)

    # ===========================
    # Total Customers
    # ===========================

    if "Customer ID" in df.columns:
        insights["total_customers"] = df["Customer ID"].nunique()
    else:
        insights["total_customers"] = 0

    # ===========================
    # Best Category
    # ===========================

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["best_category"] = category_sales.index[0]
    insights["best_category_sales"] = round(category_sales.iloc[0], 2)

    # ===========================
    # Best Region
    # ===========================

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["best_region"] = region_sales.index[0]
    insights["best_region_sales"] = round(region_sales.iloc[0], 2)

    # ===========================
    # Best State
    # ===========================

    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["best_state"] = state_sales.index[0]

    # ===========================
    # Top Product
    # ===========================

    product_sales = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["top_product"] = product_sales.index[0]

    # ===========================
    # Average Order Value
    # ===========================

    insights["average_order_value"] = round(
        df["Sales"].mean(), 2
    )

    # ===========================
    # Highest Sales Month
    # ===========================

    month_sales = (
        df.groupby("Month Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    insights["best_month"] = month_sales.index[0]

    # ===========================
    # Shipping Days
    # ===========================

    insights["average_shipping_days"] = round(
        df["Shipping Days"].mean(), 1
    )

    # ===========================
    # Forecast
    # ===========================

    insights["forecast_sales"] = forecast_summary[
        "next_month_prediction"
    ]

    # ===========================
    # Recommendation
    # ===========================

    insights["recommendation"] = (
        f"Increase inventory for "
        f"{insights['best_category']} products in "
        f"{insights['best_region']} region. "
        f"Demand is expected to remain strong."
    )

    return insights