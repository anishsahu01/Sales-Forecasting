import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go

from config import Config


def prepare_forecast_data(df):
    """
    Prepare data for Prophet.
    """

    forecast_df = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    forecast_df.columns = ["ds", "y"]

    return forecast_df



def train_model(df):
    """
    Train Prophet model.
    """

    prophet_df = prepare_forecast_data(df)

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        changepoint_prior_scale=0.15
    )

    model.fit(prophet_df)

    return model



def make_prediction(df):
    """
    Generate future forecast.
    """

    model = train_model(df)

    future = model.make_future_dataframe(
        periods=Config.FORECAST_PERIOD,
        freq="D"
    )

    forecast = model.predict(future)

    return forecast



def forecast_summary(forecast, year):
    """
    KPI prediction according to selected year.
    """

    forecast["ds"] = pd.to_datetime(
        forecast["ds"]
    )

    yearly_forecast = forecast[
        forecast["ds"].dt.year == year
    ]


    if yearly_forecast.empty:
        return {
            "next_month_prediction": 0,
            "highest_prediction": 0,
            "lowest_prediction": 0,
            "average_prediction": 0
        }


    next_30_days = yearly_forecast.head(30)


    return {

        "next_month_prediction":
            round(next_30_days["yhat"].sum(), 2),

        "highest_prediction":
            round(yearly_forecast["yhat"].max(), 2),

        "lowest_prediction":
            round(yearly_forecast["yhat"].min(), 2),

        "average_prediction":
            round(yearly_forecast["yhat"].mean(), 2)
    }



def yearly_prediction(forecast, year):
    """
    Total predicted sales for selected year.
    """

    forecast["ds"] = pd.to_datetime(
        forecast["ds"]
    )


    yearly_sales = forecast[
        forecast["ds"].dt.year == year
    ]["yhat"].sum()


    return round(yearly_sales, 2)



def forecast_chart(df, year):
    """
    Plotly chart according to selected year.
    """

    prophet_df = prepare_forecast_data(df)

    forecast = make_prediction(df)


    forecast["ds"] = pd.to_datetime(
        forecast["ds"]
    )


    prophet_df["ds"] = pd.to_datetime(
        prophet_df["ds"]
    )


    # Selected year filter

    forecast_year = forecast[
        forecast["ds"].dt.year == year
    ]


    actual_year = prophet_df[
        prophet_df["ds"].dt.year == year
    ]



    fig = go.Figure()



    # Actual Sales Line

    fig.add_trace(
        go.Scatter(

            x=actual_year["ds"],

            y=actual_year["y"],

            mode="lines",

            name="Actual Sales",

            line=dict(
                color="#3B82F6",
                width=3
            ),

            hovertemplate=
            "₹%{y:,.2f}<extra></extra>"
        )
    )



    # Forecast Line

    fig.add_trace(
        go.Scatter(

            x=forecast_year["ds"],

            y=forecast_year["yhat"],

            mode="lines",

            name="Forecast",

            line=dict(
                color="#22C55E",
                width=3
            ),

            hovertemplate=
            "₹%{y:,.2f}<extra></extra>"
        )
    )



    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0B1120",

        plot_bgcolor="#111827",

        font=dict(
            color="white"
        ),

        hovermode="x unified",

        title=f"Sales Forecast {year}",

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend=dict(
            orientation="h",
            y=1.08
        ),

        height=550
    )


    fig.update_yaxes(
        tickprefix="₹"
    )


    return fig.to_html(
        full_html=False
    )