from flask import Blueprint, render_template, current_app, request

from model.preprocessing import (
    load_data,
    preprocess_data
)

from model.forecasting import (
    make_prediction,
    forecast_summary,
    forecast_chart,
    yearly_prediction
)


forecast_bp = Blueprint(
    "forecast",
    __name__,
    url_prefix="/forecast"
)


@forecast_bp.route("/")
def forecast():

    df = load_data(
        current_app.config["DATASET_PATH"]
    )

    df = preprocess_data(df)


    # Generate forecast
    forecast = make_prediction(df)


    # Get selected year from dropdown
    selected_year = request.args.get(
        "year",
        default=2030,
        type=int
    )


    # KPI cards according to selected year
    summary = forecast_summary(
        forecast,
        selected_year
    )


    # Forecast chart
    graph = forecast_chart(
    df,
    selected_year
)


    # AI Future Year Prediction
    future_sales = yearly_prediction(
        forecast,
        selected_year
    )


    return render_template(
        "forecast.html",
        forecast_graph=graph,
        summary=summary,
        future_sales=future_sales,
        selected_year=selected_year
    )