import os
from google.colab import userdata
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
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
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])
chain = prompt | llm | StrOutputParser()
history = []
def ask(question: str) -> str:
    answer = chain.invoke({"history": history, "question": question})
    history.extend([("human", question), ("ai", answer)])
    return answer
print(ask("Hi, I'm Sahi. I have only two days. Which places can I visit?"))
print(ask("Plan a trip without knowing my destination."))

import csv
data = [
    ["question", "must_include"],
    ["Suggest a trip to Goa", "Goa"],
    ["Plan a trip to Kerala", "Kerala"],
    ["Suggest a budget trip to Vizag", "Vizag"]
]
with open("/content/test.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
def run_tests(path="/content/test.csv"):
    rows = list(csv.DictReader(open(path)))
    passed = 0
    total = len(rows)
    for row in rows:
        question = row["question"]
        expected = row["must_include"]
        answer = ask(question)
        if expected.lower() in answer.lower():
            print("PASS:", question)
            passed += 1
        else:
            print("FAIL:", question)
            print("Expected:", expected)
            print("Actual:", answer)

    print(f"\nPassed: {passed}/{total}")

run_tests()

from langchain.agents import create_agent
agent_order = create_agent(
    model=llm,
    tools=[],
    system_prompt=SYSTEM
)  # Tools come tomorrow
result_order = agent_order.invoke({
    "messages": [
        {"role": "user", "content": "Can I plan a trip within ₹5,000?"}
    ]
})
print(result_order["messages"][-1].content)
