import re

def extract_financials(text):

    revenue_match = re.search(r"revenue.*?(\d+)", text.lower())
    debt_match = re.search(r"debt.*?(\d+)", text.lower())
    profit_match = re.search(r"profit.*?(\d+)", text.lower())

    revenue = int(revenue_match.group(1)) if revenue_match else 0
    debt = int(debt_match.group(1)) if debt_match else 0
    profit = int(profit_match.group(1)) if profit_match else 0

    return {
        "revenue": revenue,
        "debt": debt,
        "profit": profit
    }