def ask_assistant(context, question):

    question = question.lower()

    if "why" in question or "reason" in question:
        return """
The loan was approved because the company's financial indicators
show moderate risk. The debt-to-revenue ratio is acceptable,
and the company is profitable, which supports repayment capacity.
"""

    elif "risk" in question:
        return """
The main risk factors include financial leverage and operational exposure.
However, the overall risk score remains within an acceptable range.
"""

    elif "summary" in question:
        return context

    else:
        return """
The system evaluated financial metrics including revenue,
debt levels, and profitability to produce a credit risk score
and generate the Credit Appraisal Memo.
"""