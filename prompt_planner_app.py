import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
from datetime import datetime

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
def get_current_time():
    now=datetime.now()
    return now.strftime("%a,%d %b %y - %H:%M")
def get_user_input():
    print("What would you like to get done today?")
    user_input= input("> ")
    return user_input
def build_prompt(tasks_description):
    current_time=get_current_time()
    return f"""
It's currently {current_time}.
The user provided the following tasks:
{tasks_description}
Please create a realistic, structured plan for the day, starting with early morning and ending by 21:15.
Include buffer time and transitions between tasks. Use a clear format with time blocks and task names.
""" 
def get_plan_from_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
             {"role": "system", "content": "You are a helpful and structured daily planning assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,    )
    return response.choices[0].message.content

def export_plan_to_file(plan_text:str):
    "Saves the plan to a text file in the /plans folder."
    Path("plans").mkdir(parents=True, exist_ok=True)

    today_str= datetime.now().strftime("%Y-%m-%d")
    version=1
    while True:
        filename = f"plans/plan_{today_str}_v{version}.txt"
        if not os.path.exists(filename):
            break
        version += 1        

    with open(filename, "w",encoding="utf-8") as file:
        file.write(plan_text)
if __name__ == "__main__":
    print("🗓️  Prompt Planner")
    print("Current time:", get_current_time())
    
    tasks = get_user_input()
    prompt= build_prompt(tasks)
    print("\nSending the prompt to ChatGPT:\n")

    try:
        plan = get_plan_from_chatgpt(prompt)
        print("\nHere is your plan:\n")
        print(plan)
        export_plan_to_file(plan)
    except Exception as e:
        print("an error occurred while commuting with ChatGPT:",e)

        from openai import OpenAI


