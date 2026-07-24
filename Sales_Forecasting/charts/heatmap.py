import pandas as pd
import plotly.express as px

BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
GRID = "#374151"


def heatmap_chart(df):
    """
    Monthly Sales Heatmap
    """

    heatmap = (
        df.groupby(["Year", "Month Name"])["Sales"]
        .sum()
        .reset_index()
    )

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    heatmap["Month Name"] = pd.Categorical(
        heatmap["Month Name"],
        categories=month_order,
        ordered=True
    )

    heatmap = heatmap.sort_values(
        ["Year", "Month Name"]
    )

    pivot = heatmap.pivot(
        index="Year",
        columns="Month Name",
        values="Sales"
    )

    fig = px.imshow(
        pivot,
        text_auto=".0f",
        aspect="auto",
        color_continuous_scale="Blues"
    )

    fig.update_layout(

        template="plotly_dark",

        title=dict(
            text="Monthly Sales Heatmap",
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
            l=20,
            r=20,
            t=70,
            b=20
        ),

        height=500,

        xaxis=dict(
            title="Month",
            showgrid=False
        ),

        yaxis=dict(
            title="Year",
            showgrid=False
        ),

        coloraxis_colorbar=dict(
            title="Sales"
        )
    )

    fig.update_traces(
        hovertemplate=
        "<b>Month:</b> %{x}<br>"
        "<b>Year:</b> %{y}<br>"
        "<b>Sales:</b> $%{z:,.2f}<extra></extra>"
    )

    return fig.to_html(full_html=False)