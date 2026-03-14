import streamlit as st

from document_parser import extract_text
from financial_extractor import extract_financials
from risk_model import calculate_risk
from cam_generator import generate_cam
from visualization import plot_risk_dashboard
from assistant import ask_assistant


st.title("IntelliCredit – AI Credit Decision Engine")

uploaded = st.file_uploader("Upload Company PDF", type="pdf")

if uploaded:

    text = extract_text(uploaded)

    data = extract_financials(text)

    st.subheader("Extracted Financial Data")
    st.write(data)

    risk_score = calculate_risk(data)

    st.subheader("Risk Score")
    st.write(risk_score)

    fig = plot_risk_dashboard(risk_score)
    st.pyplot(fig)

    cam = generate_cam(data, risk_score)

    st.subheader("Credit Appraisal Memo")
    st.text(cam)

    st.subheader("AI Credit Copilot")

    question = st.text_input("Ask about this loan decision")

    if question:
        answer = ask_assistant(cam, question)
        st.write(answer)