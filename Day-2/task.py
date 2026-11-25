
import functools
from openai import OpenAI, RateLimitError, APIConnectionError
from google.colab import userdata
# API Configuration
client = OpenAI(
    api_key=userdata.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
MODEL = "openai/gpt-oss-120b"
# Travel Package Details
MENU = {
    "goa trip": 5000,
    "hyderabad trip": 3000,
    "kerala trip": 7000,
    "vizag trip": 2500,
    "manali trip": 10000
}
# System Prompt
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
- Give suggestions in bullet points when needed."""
# Decorator
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"  [log] {func.__name__}{args} -> {result!r}")
        return result
    return wrapper
# Price Calculation Function
@log_call
def get_price(item: str, qty: int = 1) -> int:
    """Return the total price in rupees for qty of an item."""
    return MENU[item.lower().strip()] * qty
# Conversation Memory
history = [{"role": "system", "content": SYSTEM}]
MAX_TURNS = 8
# Chat Function
def chat(user_text: str) -> str:
    history.append({"role": "user", "content": user_text})
    recent = [history[0]] + history[1:][-MAX_TURNS:]
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent,
            temperature=0.3
        )
        reply = response.choices[0].message.content
    except RateLimitError:
        reply = "We're a little busy. Please try again in a minute."
    except APIConnectionError:
        reply = "I can't reach the server right now. Please try again shortly."
    history.append({"role": "assistant", "content": reply})
    return reply
# Chat Loop
while True:
    text = input("You: ")
    if text.lower().strip() in ("bye", "exit", "quit"):
        print("Bot: Thank you for using SmartTrip!")
        break
    print("Bot:", chat(text))
