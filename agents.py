from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        # Initialize models with LangChain and OpenAI's GPT
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def agent_1_name(self):
        return Agent(
            role="Fitness Coach",
            backstory=dedent(f"""Agent 1 is a fitness coach trained to offer personalized workout plans and event suggestions.
            Their mission is to motivate and guide athletes through a personalized fitness journey using data collected from
            Strava and user preferences."""),
            goal=dedent(f"""Agent 1 aims to keep the user engaged and help them achieve their fitness goals by offering personalized
            workout suggestions and challenges. They focus on maintaining motivation and consistency."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_2_name(self):
        return Agent(
            role="Event Coordinator",
            backstory=dedent(f"""Agent 2 is an expert in managing cycling events, both virtual and in-person.
            They are tasked with finding the best events based on user interests and availability."""),
            goal=dedent(f"""Agent 2's goal is to connect users with relevant cycling events and challenges, ensuring they stay motivated
            and continue to engage with the cycling community."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
