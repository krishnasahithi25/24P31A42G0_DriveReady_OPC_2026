!pip install -q langchain langchain-groq gspread

import os
from google.colab import userdata, auth
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,
    max_retries=3
)
auth.authenticate_user()
import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)
sh = gc.create("assistant for SmartTrip Travel Planner")
ws = sh.sheet1
ws.append_row([
    "name", "destination", "travel_date",
    "days", "budget", "activities", "total"
])
print("Sheet ready:", sh.url)

from typing import Literal
from pydantic import BaseModel,Field
from langchain.tools import tool
MENU = {"goa": 30000, "kerala": 40000, "tamil nadu": 20000, "manali": 25000, "ooty": 35000}
HOURS = {"goa": "Beaches : 24 hours, Fort Aguada: 9:30AM t0 3: 00PM, Sinquerim Fort: 10:00AM to 4:00PM, Cabo de Rama: 11:00AM to 5:30PM",
         "kerala": "Munnar tea gardens: Daytime visits, Alleppey backwaters: Depends on boat schedule",
         "manali": "Hadimba Temple: 8:00 AM to 6:00 PM, Solang Valley: Daytime visits",
         "ooty": "Botanical Garden: 7:00 AM to 6:30 PM, Ooty Lake: 9:00 AM to 6:00 PM",
          "tamil nadu": "Meenakshi Amman Temple: 5:00 AM to 12:30 PM and 4:00 PM to 10:00 PM, Marina Beach: Open access"}
class TravelPlan(BaseModel):
    """A travel plan collected from a user's chat message."""
    name: str = Field(description="User's first name")
    destination: Literal[
        "goa","kerala","manali", "ooty", "tamil nadu"
    ] = Field(description="Travel destination")
    days: int = Field(description="Number of travel days", ge=1)
    travel_date: str = Field(description="Travel starting date")
    budget: int = Field(description="Total travel budget in rupees", ge=1)
    activities: str = Field(description="Activities the user wants to enjoy")

@tool
def get_price(destination: str) -> str:
    """Get the estimated travel budget for a destination.
    Args:
        destination: Travel destination, e.g. goa, kerala or ooty.
    """
    price = MENU.get(destination.lower().strip())
    if price is None:
        return f"'{destination}' is not available. We have: {', '.join(MENU)}."
    return f"Estimated budget for {destination} = Rs {price}"
@tool
def get_hours(destination: str) -> str:
    """Get tourist attraction visiting hours for a destination."""
    hours = HOURS.get(destination.lower().strip())
    if hours is None:
        return f"No visiting hours available for {destination}."
    return f"Visiting information for {destination}: {hours}"
@tool
def log_travel_plan(
    name: str,
    destination: str,
    days: int,
    travel_date: str,
    budget: int,
    activities: str
) -> str:
    """Save a confirmed travel plan to the Google Sheet."""
    try:
        plan = TravelPlan(
            name=name,
            destination=destination.lower().strip(),
            days=days,
            travel_date=travel_date,
            budget=budget,
            activities=activities
        )
    except Exception as e:
        return f"Could not save the travel plan: {e}"
    total = MENU[plan.destination]
    ws.append_row([
        plan.name,
        plan.destination,
        plan.travel_date,
        plan.days,
        plan.budget,
        plan.activities,
        total
    ])
    return f"Saved travel plan for {plan.name}: {plan.destination}, {plan.days} days, Rs {total} estimated destination budget."

from langchain.agents import create_agent
SYSTEM = """You are the assistant for SmartTrip Travel Planner.
Facts:
- We help users plan trips.
- We suggest tourist attractions, activities and travel tips.
- We provide budget-friendly travel suggestions.
- Users should share their destination and travel dates.
Rules:
- Never invent flight or hotel prices.
- Never guarantee weather conditions.
- If information is unavailable, clearly say so.
- Consider the user's budget when suggesting trips.
Format:
- Reply politely in under 60 words.
- Use simple English.
- Give suggestions in bullet points when needed.
"""
agent = create_agent(
    model=llm,
    tools=[get_price, get_hours, log_travel_plan],
    system_prompt=SYSTEM
)
history = []
def chat(text: str) -> str:
    global history
    try:
        result = agent.invoke({
            "messages": history + [
                {"role": "user", "content": text}
            ]
        })
        history = result["messages"]
        return history[-1].content
    except Exception as e:
        print("Agent error:", e)
        return "Sorry, I'm a little busy. Please try again in a minute."
print(chat("Can we plan a trip to Manali for this weekend?"))
print(chat("How much will it cost to travel to Manali and what are the famous places there?"))
print(chat("Save my travel plan."))
