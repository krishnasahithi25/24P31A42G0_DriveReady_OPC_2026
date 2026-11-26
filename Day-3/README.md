# Day-3 SmartTrip Travel Planner
## Task
Build a SmartTrip Travel Planner using LangChain. Create an AI-powered chatbot that helps users with budget-friendly travel suggestions, remembers previous conversations, and provides trip-planning information.
## Implementation
- Installed LangChain and LangChain-Groq libraries.
- Configured the Groq API key using Google Colab Secrets.
- Initialized the ChatGroq model (`openai/gpt-oss-120b`).
- Created a System Prompt with facts, rules, and response format.
- Used ChatPromptTemplate to structure messages.
- Used MessagesPlaceholder to maintain conversation history.
- Used StrOutputParser to get text output.
- Created an `ask()` function to interact with the chatbot and maintain memory.
- Created a CSV test file (`test.csv`) to test travel-related questions.
- Explored LangChain's `create_agent()` to understand AI agents.
## How to Run
1. Open the Day 3 Google Colab notebook.
2. Install the required LangChain libraries.
3. Add the `GROQ_API_KEY` in Google Colab Secrets.
4. Run all the cells in order.
5. Ask travel-related questions to the SmartTrip chatbot.
6. Check conversation history and explore the agent implementation.
## Learning Outcome
Learned the difference between a chatbot and an AI agent, the four parts of an agent, the agent loop, LangChain basics, conversation memory, and testing an AI assistant.
