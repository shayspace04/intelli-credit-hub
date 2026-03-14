def calculate_risk(data):

    revenue = data["revenue"]
    debt = data["debt"]
    profit = data["profit"]

    risk_score = 50

    if revenue > 0:
        debt_ratio = debt / revenue
    else:
        debt_ratio = 1

    if debt_ratio > 0.6:
        risk_score += 30

    if profit < 0:
        risk_score += 20
    else:
        risk_score -= 10

    risk_score = max(0, min(100, risk_score))

    return risk_score