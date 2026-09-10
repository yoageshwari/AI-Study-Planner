
import streamlit as st
from agent import create_study_plan


st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="centered"
)


st.title("🤖 AI Study Planner Agent")

st.write(
    "Enter your study information and the AI agent "
    "will create a personalized study plan."
)


subjects_input = st.text_input(
    "📚 Subjects",
    placeholder="Example: Python, DBMS, AI, Operating Systems"
)


exam_days = st.number_input(
    "📅 How many days until your exam?",
    min_value=1,
    max_value=365,
    value=20
)


study_hours = st.number_input(
    "⏰ How many hours can you study per day?",
    min_value=1,
    max_value=16,
    value=3
)


difficult_input = st.text_input(
    "🔥 Which subjects are difficult?",
    placeholder="Example: AI, Operating Systems"
)


if st.button("🚀 Generate Study Plan"):

    if not subjects_input:
        st.warning("Please enter your subjects.")

    else:
        subjects = [
            subject.strip()
            for subject in subjects_input.split(",")
            if subject.strip()
        ]

        difficult_subjects = [
            subject.strip()
            for subject in difficult_input.split(",")
            if subject.strip()
        ]

        with st.spinner("🤖 Agent is creating your study plan..."):

            try:
                plan = create_study_plan(
                    subjects,
                    exam_days,
                    study_hours,
                    difficult_subjects
                )

                st.success("Your study plan is ready!")

                st.markdown("## 📚 Your Personalized Study Plan")

                st.markdown(plan)

            except Exception as e:
                st.error("Something went wrong:")
                st.code(str(e))