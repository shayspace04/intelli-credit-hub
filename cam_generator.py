def generate_cam(data, risk_score):

    decision = "Approve"
    limit = "₹10 Cr"
    rate = "11%"

    if risk_score > 70:
        decision = "Reject"
        limit = "N/A"
        rate = "N/A"

    cam = f"""
CREDIT APPRAISAL MEMO

Revenue: {data['revenue']}
Debt: {data['debt']}
Profit: {data['profit']}

Risk Score: {risk_score}

Decision: {decision}
Suggested Limit: {limit}
Interest Rate: {rate}
"""

    return cam