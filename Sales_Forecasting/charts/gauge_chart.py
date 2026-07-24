import plotly.graph_objects as go

BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
GREEN = "#22C55E"


def gauge_chart(forecast_summary):
    """
    Forecast Performance Gauge
    """

    value = forecast_summary["average_prediction"]

    maximum = max(
        forecast_summary["highest_prediction"] * 1.2,
        value + 1000
    )

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            number={
                "prefix": "$",
                "font": {
                    "size": 40,
                    "color": TEXT
                }
            },

            title={
                "text": "Average Forecast",
                "font": {
                    "size": 24,
                    "color": TEXT
                }
            },

            gauge={

                "axis": {
                    "range": [0, maximum]
                },

                "bar": {
                    "color": GREEN,
                    "thickness": 0.35
                },

                "bgcolor": CARD,

                "borderwidth": 2,

                "bordercolor": "#374151",

                "steps": [

                    {
                        "range": [0, maximum * 0.40],
                        "color": "#1E293B"
                    },

                    {
                        "range": [maximum * 0.40, maximum * 0.70],
                        "color": "#334155"
                    },

                    {
                        "range": [maximum * 0.70, maximum],
                        "color": "#475569"
                    }

                ],

                "threshold": {

                    "line": {
                        "color": "#F59E0B",
                        "width": 5
                    },

                    "thickness": 0.8,

                    "value": value

                }

            }

        )

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=BACKGROUND,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT,
            family="Poppins"
        ),

        height=420,

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )

    )

    return fig.to_html(full_html=False)