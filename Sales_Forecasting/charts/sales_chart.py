import plotly.express as px


BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
GRID = "#374151"
BLUE = "#3B82F6"


def sales_trend_chart(df):
    """
    Creates a daily sales trend chart.
    """

    sales = (
        df.groupby("Order Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Order Date")
    )

    fig = px.line(
        sales,
        x="Order Date",
        y="Sales",
        markers=True
    )

    fig.update_traces(
        line=dict(
            color=BLUE,
            width=4,
            shape="spline"
        ),
        marker=dict(
            size=6,
            color=BLUE
        ),
        hovertemplate=
        "<b>Date:</b> %{x}<br>"
        "<b>Sales:</b> $%{y:,.2f}"
        "<extra></extra>"
    )

    fig.update_layout(

        template="plotly_dark",

        title=dict(
            text="Sales Trend",
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

        margin=dict(
            l=25,
            r=25,
            t=70,
            b=25
        ),

        hovermode="x unified",

        height=480,

        xaxis=dict(
            title="Order Date",
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            title="Sales",
            showgrid=True,
            gridcolor=GRID,
            zeroline=False
        ),

        legend=dict(
            orientation="h",
            y=1.08
        )
    )

    return fig.to_html(full_html=False)