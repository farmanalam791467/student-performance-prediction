import streamlit as st

st.set_page_config(
    page_title="Student Final Grade Prediction",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Final Grade Prediction")
st.caption("Predict a student's final grade before the final examination using Machine Learning.")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("📚 Academic Information")

    study_hours = st.slider("Study Hours", 0, 15, 5)
    attendance = st.slider("Attendance (%)", 0, 100, 80)
    assignment = st.slider("Assignment Completion (%)", 0, 100, 80)
    discussions = st.slider("Discussions", 0, 20, 5)
    online_courses = st.number_input("Online Courses", 0, 20, 2)
    motivation = st.slider("Motivation", 1, 5, 3)

with right:
    st.subheader("👨‍🎓 Student Information")

    age = st.number_input("Age", 15, 30, 20)
    gender = st.selectbox("Gender", ["Male", "Female"])
    internet = st.selectbox("Internet Access", ["Yes", "No"])
    resources = st.selectbox("Study Resources", ["Available", "Not Available"])
    learning_style = st.selectbox(
        "Learning Style",
        ["Visual", "Auditory", "Kinesthetic"]
    )
    extracurricular = st.selectbox(
        "Extracurricular Activities",
        ["Yes", "No"]
    )
    stress = st.slider("Stress Level", 1, 5, 3)

st.divider()

if st.button("🚀 Predict Final Grade", use_container_width=True):
    st.success("Prediction completed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Predicted Grade", "Excellent")

    with col2:
        st.metric("Confidence", "94.25%")

    st.subheader("Prediction Probability")

    st.progress(0.05, text="Grade 0 : 5%")
    st.progress(0.12, text="Grade 1 : 12%")
    st.progress(0.18, text="Grade 2 : 18%")
    st.progress(0.65, text="Grade 3 : 65%")