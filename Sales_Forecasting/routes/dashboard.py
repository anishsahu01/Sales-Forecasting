from flask import Blueprint, render_template, request, current_app

from model.preprocessing import (
    load_data,
    preprocess_data,
    apply_filters,
    get_filter_values
)

from model.forecasting import (
    make_prediction,
    forecast_summary
)

from model.insights import generate_insights

from charts.sales_chart import sales_trend_chart
from charts.category_chart import category_chart
from charts.region_chart import region_chart
from charts.product_chart import product_chart
from charts.heatmap import heatmap_chart


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/", methods=["GET"])
def dashboard():

    # -------------------------
    # Load Dataset
    # -------------------------

    df = load_data(
        current_app.config["DATASET_PATH"]
    )

    df = preprocess_data(df)

    # -------------------------
    # Filters
    # -------------------------

    year = request.args.get("year")
    region = request.args.get("region")
    state = request.args.get("state")
    category = request.args.get("category")
    sub_category = request.args.get("sub_category")
    segment = request.args.get("segment")
    ship_mode = request.args.get("ship_mode")

    filtered_df = apply_filters(
        df,
        year=year,
        region=region,
        state=state,
        category=category,
        sub_category=sub_category,
        segment=segment,
        ship_mode=ship_mode
    )

    # -------------------------
    # Forecast (used for AI Insights)
    # -------------------------

    forecast = make_prediction(filtered_df)

    forecast_data = forecast_summary(
        forecast,
        2030
    )

    # -------------------------
    # AI Insights
    # -------------------------

    insights = generate_insights(
        filtered_df,
        forecast_data
    )

    # -------------------------
    # KPI Cards
    # -------------------------

    total_sales = round(
        filtered_df["Sales"].sum(),
        2
    )

    total_orders = len(filtered_df)

    if "Customer ID" in filtered_df.columns:
        total_customers = filtered_df[
            "Customer ID"
        ].nunique()
    else:
        total_customers = 0

    avg_sales = round(
        filtered_df["Sales"].mean(),
        2
    )

    # -------------------------
    # Charts
    # -------------------------

    sales_graph = sales_trend_chart(
        filtered_df
    )

    category_graph = category_chart(
        filtered_df
    )

    region_graph = region_chart(
        filtered_df
    )

    product_graph = product_chart(
        filtered_df
    )

    heatmap_graph = heatmap_chart(
        filtered_df
    )

    # -------------------------
    # Filter Values
    # -------------------------

    filters = get_filter_values(df)

    # -------------------------
    # Render
    # -------------------------

    return render_template(

        "dashboard.html",

        filters=filters,

        selected_year=year,
        selected_region=region,
        selected_state=state,
        selected_category=category,
        selected_sub_category=sub_category,
        selected_segment=segment,
        selected_ship_mode=ship_mode,

        total_sales=total_sales,
        total_orders=total_orders,
        total_customers=total_customers,
        average_sales=avg_sales,

        insights=insights,

        sales_graph=sales_graph,
        category_graph=category_graph,
        region_graph=region_graph,
        product_graph=product_graph,
        heatmap_graph=heatmap_graph
    )