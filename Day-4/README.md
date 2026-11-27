# Day-4 - SmartTrip Travel Planner

## Task
To create a SmartTrip Travel Planner using an AI agent. It helps users plan trips, know the budget and save trip details in Google Sheets.

## Implementation

- Installed the required libraries.
- Connected the Groq API using the API key.
- Used the ChatGroq model.
- Connected Google Sheets with Colab.
- Created a Google Sheet to save trip details.
- Used Pydantic to check the travel plan details.
- Created three tools:
  - `get_price()` – To check the trip budget.
  - `get_hours()` – To get visiting time details.
  - `log_travel_plan()` – To save trip details in Google Sheets.
- Created an AI agent using `create_agent()`.
- Used a chat function to interact with the agent.
- Added error handling for API problems.

## How to Run

1. Open the Day-4 Colab notebook.
2. Install the required libraries.
3. Add the Groq API key in Colab Secrets.
4. Connect your Google account.
5. Run all the cells.
6. Ask questions to the SmartTrip Travel Planner.
7. Check Google Sheets to see the saved trip details.

## Learning Outcome

Learned how to create AI agents, use tools, validate data with Pydantic, connect Google Sheets and handle errors.
