import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_workout_gemini(
    username,
    age,
    weight,
    goal,
    intensity
):
    prompt = f"""
Create a personalized fitness workout plan.

Name: {username}
Age: {age}
Weight: {weight} kg
Fitness Goal: {goal}
Workout Intensity: {intensity}

Give a simple weekly workout plan.

Include:
1. Weekly workout schedule
2. Exercises
3. Sets and repetitions
4. Rest time
5. Warm-up
6. Cool-down
7. Basic safety tips

Make the plan easy to understand.
"""

    response = model.generate_content(prompt)

    return response.text