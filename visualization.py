import matplotlib.pyplot as plt

def plot_risk_dashboard(risk_score):

    labels = ["Financial Risk","Legal Risk","Operational Risk"]
    values = [risk_score, risk_score*0.6, risk_score*0.8]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Risk Dashboard")

    return fig