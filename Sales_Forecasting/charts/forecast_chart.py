import plotly.graph_objects as go
from prophet import Prophet

BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
BLUE = "#3B82F6"
GREEN = "#22C55E"


def forecast_chart(df):

    forecast_df = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    forecast_df.columns = ["ds", "y"]

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(forecast_df)

    future = model.make_future_dataframe(
        periods=365
    )

    forecast = model.predict(future)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=forecast_df["ds"],
            y=forecast_df["y"],
            mode="lines",
            name="Actual Sales",
            line=dict(
                color=BLUE,
                width=4
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat"],
            mode="lines",
            name="Forecast",
            line=dict(
                color=GREEN,
                width=4,
                dash="dash"
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat_upper"],
            line=dict(width=0),
            showlegend=False
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast["ds"],
            y=forecast["yhat_lower"],
            fill="tonexty",
            fillcolor="rgba(34,197,94,0.15)",
            line=dict(width=0),
            showlegend=False
        )
    )

    fig.update_layout(

        template="plotly_dark",

        title=dict(
            text="Sales Forecast (365 Days)",
            x=0.03,
            font=dict(
                size=24,
                color=TEXT
            )
        ),

        paper_bgcolor=BACKGROUND,
        plot_bgcolor=CARD,

        font=dict(
            color=TEXT,
            family="Poppins"
        ),

        hovermode="x unified",

        height=550,

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        ),

        legend=dict(
            orientation="h",
            y=1.08
        ),

        xaxis=dict(
            title="Date",
            showgrid=False
        ),

        yaxis=dict(
            title="Sales",
            showgrid=True,
            gridcolor="#374151"
        )
    )

    return fig.to_html(full_html=False)