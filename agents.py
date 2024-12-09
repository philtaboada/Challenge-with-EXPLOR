import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model_name="llama3-70b-8192"
api_key = os.getenv("GROQ_API_KEY")



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.groq_llama = ChatGroq(model_name="llama3-70b-8192", api_key=api_key, temperature=0.7)
        self.groq_mixtral = ChatGroq(model_name="mixtral-8x7b-32768", api_key=api_key, temperature=0.5)

    def QueryBot(self):
        return Agent(
            role="Cycling Event Finder in Peru",
            backstory=dedent(f"""The agent has been designed to search for and recommend cycling events in Peru. It uses advanced search tools and data analysis to identify relevant events from various online sources. Its focus is on finding competitions, marathons, and other cycling-related activities in different regions of the country. The agent analyzes the available information, filtering only the most relevant events for the user."""),
            goal=dedent(f"""The goal of the agent is to provide an up-to-date and accurate list of cycling events in Peru. The agent searches, filters, and presents relevant events based on the user's requirements, such as location, event type, dates, and difficulty level. Its mission is to help cyclists and sports enthusiasts quickly find events that match their interests and abilities."""),
            allow_delegation=False,
            verbose=True,
            llm=self.groq_llama,
        )

    def agent_2_name(self):
        return Agent(
            role="Define agent 2 role here",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Define agent 2 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
