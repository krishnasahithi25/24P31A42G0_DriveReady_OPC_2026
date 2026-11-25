# Day 1 – SmartTrip Travel Planner
## Task
Build a Python-based AI chatbot that helps users plan trips by providing destination suggestions, travel information, activities, tips, and budget details.
## Implementation
The chatbot uses the Groq API and an LLM (`openai/gpt-oss-120b`) to understand user queries and generate travel-related responses.
It provides travel package information for different destinations:
- Goa – ₹5,000
- Hyderabad – ₹3,000
- Kerala – ₹7,000
- Vizag – ₹2,500
- Manali – ₹10,000
The chatbot uses a system prompt to define its role and instructions. It asks users about their destination and travel dates, suggests activities and travel tips, and provides budget suggestions.
A Python `get_price()` function calculates the total package cost based on the selected package and quantity.
The chatbot maintains conversation history and handles API rate-limit and connection errors. It continues accepting questions until the user enters `exit`, `bye`, or `quit`.
## How to Run
1. Install the required OpenAI Python library.
2. Set the Groq API key as an environment variable.
3. Run the Python program in Google Colab.
4. Enter travel-related questions.
5. Type `exit` to stop the chatbot.
## Technologies Used
- Python
- Google Colab
- Groq API
- OpenAI Python Library
- Large Language Model (LLM)
