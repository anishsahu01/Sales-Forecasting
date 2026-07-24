from datetime import datetime


def format_currency(value):
    """
    Format number as currency.
    """
    return f"${value:,.2f}"


def format_number(value):
    """
    Format integer with commas.
    """
    return f"{int(value):,}"


def format_percentage(value):
    """
    Format percentage.
    """
    return f"{value:.2f}%"


def format_date(date):
    """
    Format date as DD Mon YYYY.
    """
    if isinstance(date, datetime):
        return date.strftime("%d %b %Y")
    return date


def safe_divide(a, b):
    """
    Prevent division by zero.
    """
    return a / b if b != 0 else 0


def calculate_growth(current, previous):
    """
    Calculate percentage growth.
    """
    if previous == 0:
        return 0

    return ((current - previous) / previous) * 100