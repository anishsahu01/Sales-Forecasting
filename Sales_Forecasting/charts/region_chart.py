import plotly.express as px

BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
GRID = "#374151"

COLORS = [
    "#3B82F6",
    "#06B6D4",
    "#22C55E",
    "#F59E0B",
    "#8B5CF6",
    "#EF4444"
]


def region_chart(df):
    """
    Sales by Region
    """

    region = (
        df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=True)
    )

    fig = px.bar(
        region,
        x="Sales",
        y="Region",
        orientation="h",
        color="Sales",
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        texttemplate="₹%{x:,.0f}",
        textposition="outside",

        hovertemplate=
        "<b>Region</b>: %{y}<br>"
        "<b>Sales</b>: ₹%{x:,.2f}"
        "<extra></extra>"
    )

    fig.update_layout(

        template="plotly_dark",

        title=dict(
            text="Sales by Region",
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

        height=480,

        margin=dict(
            l=25,
            r=25,
            t=70,
            b=25
        ),

        xaxis=dict(
            title="Sales",
            tickprefix="₹",
            showgrid=True,
            gridcolor=GRID,
            zeroline=False
        ),

        yaxis=dict(
            title="Region",
            showgrid=False
        ),

        coloraxis_showscale=False
    )

    return fig.to_html(full_html=False)