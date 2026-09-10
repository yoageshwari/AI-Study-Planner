
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def create_study_plan(subjects, exam_days, study_hours, difficult_subjects):

    prompt = f"""
You are an AI Study Planner Agent.

Your goal is to create a realistic and personalized study plan for a student.

Student information:
- Subjects: {subjects}
- Days until exam: {exam_days}
- Available study hours per day: {study_hours}
- Difficult subjects: {difficult_subjects}

Instructions:
1. Give more study time to difficult subjects.
2. Distribute time across all subjects.
3. Do not exceed the available study hours per day.
4. Create a plan for the next {exam_days} days.
5. Include short breaks where appropriate.
6. Keep the plan simple and realistic.
7. At the end, give 2-3 study tips.

Format the answer clearly using headings and bullet points.
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI study planning agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content