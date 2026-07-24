from flask import Flask

from config import Config

from routes.dashboard import dashboard_bp
from routes.forecast import forecast_bp
from routes.products import products_bp
from routes.reports import reports_bp


app = Flask(__name__)

app.config.from_object(Config)


# -------------------------
# Register Blueprints
# -------------------------

app.register_blueprint(dashboard_bp)

app.register_blueprint(forecast_bp)

app.register_blueprint(products_bp)

app.register_blueprint(reports_bp)


# -------------------------
# Run Application
# -------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)