import plotly.express as px

BACKGROUND = "#0B1120"
CARD = "#111827"
TEXT = "#FFFFFF"
GRID = "#374151"
BLUE = "#3B82F6"


def product_chart(df):
    """
    Top 10 Products by Sales
    """

    products = (
        df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
        .sort_values("Sales")
    )

    fig = px.bar(
        products,
        x="Sales",
        y="Product Name",
        orientation="h",
        color="Sales",
        color_continuous_scale="Blues"
    )

    fig.update_traces(

        texttemplate="₹%{x:,.0f}",
        textposition="outside",

        hovertemplate=
        "<b>Product</b>: %{y}<br>"
        "<b>Sales</b>: ₹%{x:,.2f}"
        "<extra></extra>"
    )

    fig.update_layout(

        template="plotly_dark",

        title=dict(
            text="Top 10 Products",
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
            title="Sales",
            tickprefix="₹",
            showgrid=True,
            gridcolor=GRID,
            zeroline=False
        ),

        yaxis=dict(
            title="Product",
            showgrid=False,
            automargin=True
        ),

        coloraxis_showscale=False
    )

    return fig.to_html(full_html=False)