import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# LOAD MODEL
# ----------------------------
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
le = pickle.load(open("model/label_encoder.pkl", "rb"))

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Student Predictor", layout="wide")

st.title("🎓 Student Success Predictor")
st.markdown("### AI-based prediction of student outcome")

# ----------------------------
# UI LAYOUT
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📘 Academic Info")
    age = st.slider("Age", 15, 60, 20)

    sem1_grade = st.slider("1st Sem Grade", 0.0, 20.0, 12.0)
    sem2_grade = st.slider("2nd Sem Grade", 0.0, 20.0, 12.0)

    sem1_approved = st.slider("1st Sem Approved Subjects", 0, 10, 5)
    sem2_approved = st.slider("2nd Sem Approved Subjects", 0, 10, 5)

with col2:
    st.subheader("💰 Financial & Status")

    tuition = st.selectbox("Tuition Fees Paid?", ["Yes", "No"])
    debtor = st.selectbox("Debtor?", ["No", "Yes"])
    scholarship = st.selectbox("Scholarship?", ["No", "Yes"])

    gender = st.selectbox("Gender", ["Male", "Female"])

# Convert inputs
tuition = 1 if tuition == "Yes" else 0
debtor = 1 if debtor == "Yes" else 0
scholarship = 1 if scholarship == "Yes" else 0
gender = 1 if gender == "Male" else 0

# ----------------------------
# PREDICT
# ----------------------------
if st.button("🚀 Predict Outcome"):

    # Dummy/default values for unused columns
    input_data = np.array([[ 
        1, 8, 1, 10, 1, 1, 1, 10, 10, 5, 5, 0, 0,
        debtor, tuition, gender, scholarship, age, 0,

        0, 6, 6, sem1_approved, sem1_grade, 0,
        0, 6, 6, sem2_approved, sem2_grade, 0,

        10.0, 2.0, 1.0
    ]])

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict
    pred = model.predict(input_scaled)
    result = le.inverse_transform(pred)

    probs = model.predict_proba(input_scaled)[0]

    # ----------------------------
    # RESULT DISPLAY
    # ----------------------------
    st.markdown("---")

    if result[0] == "Graduate":
        st.success("🎉 Student likely to GRADUATE")
    elif result[0] == "Dropout":
        st.error("⚠️ Student at risk of DROPOUT")
    else:
        st.warning("📘 Student will remain ENROLLED")

    # ----------------------------
    # CHART
    # ----------------------------
    st.subheader("📊 Prediction Probability")

    prob_df = pd.DataFrame({
        "Outcome": ["Dropout", "Enrolled", "Graduate"],
        "Probability": probs * 100
    })

    fig, ax = plt.subplots()
    ax.bar(prob_df["Outcome"], prob_df["Probability"])
    ax.set_ylabel("Probability (%)")

    st.pyplot(fig)

    # ----------------------------
    # INSIGHT BOX
    # ----------------------------
    st.info(f"""
    🔍 Key Insights:
    - Higher grades → Higher chance of graduation  
    - Debtor → Higher dropout risk  
    - Tuition unpaid → High risk  
    - Scholarship → Positive impact  
    """)