from flask import Blueprint, render_template, current_app

from model.preprocessing import (
    load_data,
    preprocess_data
)

from charts.product_chart import product_chart


products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/")
def products():

    df = load_data(
        current_app.config["DATASET_PATH"]
    )

    df = preprocess_data(df)

    top_products = (
        df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(20)
    )

    graph = product_chart(df)

    return render_template(
        "products.html",
        products=top_products.to_dict(orient="records"),
        product_graph=graph
    )