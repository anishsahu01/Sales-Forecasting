from flask import Blueprint, render_template, current_app

from model.preprocessing import (
    load_data,
    preprocess_data
)

from model.insights import generate_insights
from model.forecasting import (
    make_prediction,
    forecast_summary
)

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports"
)


@reports_bp.route("/")
def reports():

    df = load_data(
        current_app.config["DATASET_PATH"]
    )

    df = preprocess_data(df)

    forecast = make_prediction(df)

    summary = forecast_summary(
    forecast,
    2030
)

    insights = generate_insights(
        df,
        summary
    )

    report = {

        "Total Sales": round(
            df["Sales"].sum(),
            2
        ),

        "Total Orders": len(df),

        "Average Sales": round(
            df["Sales"].mean(),
            2
        ),

        "Highest Sale": round(
            df["Sales"].max(),
            2
        ),

        "Lowest Sale": round(
            df["Sales"].min(),
            2
        ),

        "Forecast Next Month": summary[
            "next_month_prediction"
        ],

        "Best Category": insights[
            "best_category"
        ],

        "Best Region": insights[
            "best_region"
        ],

        "Top Product": insights[
            "top_product"
        ],

        "Average Shipping Days": insights[
            "average_shipping_days"
        ],

        "Recommendation": insights[
            "recommendation"
        ]
    }

    return render_template(
        "reports.html",
        report=report
    )