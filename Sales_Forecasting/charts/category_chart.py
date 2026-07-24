import plotly.express as px

BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
GRID = "#374151"

COLORS = [
    "#3B82F6",
    "#22C55E",
    "#F59E0B",
    "#8B5CF6",
    "#06B6D4"
]


def category_chart(df):
    """
    Sales by Category
    """

    category = (
        df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig = px.pie(
        category,
        names="Category",
        values="Sales",
        hole=0.65,
        color_discrete_sequence=COLORS
    )

    fig.update_traces(

        textposition="inside",

        textinfo="percent+label",

        pull=[0.03] * len(category),

        hovertemplate=
        "<b>%{label}</b><br>"
        "Sales: $%{value:,.2f}<br>"
        "Percentage: %{percent}<extra></extra>"
    )

    fig.update_layout(

        template="plotly_dark",

        title=dict(
            text="Sales by Category",
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

        showlegend=True,

        legend=dict(
            orientation="h",
            y=-0.15,
            x=0.5,
            xanchor="center"
        )
    )

    return fig.to_html(full_html=False)