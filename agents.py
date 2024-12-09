from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


class AgentManager:
    """
    Manages all agents for the system, allowing dynamic retrieval and assignment of agents for tasks.
    """
    def __init__(self):
        # Initialize models with LangChain and OpenAI's GPT
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

        # Initialize a dictionary to store all agents with predefined roles, backstories, and goals
        self.agents = {
            "gpt3.5": self.create_agent(
                name="GPT-3.5",
                role="Data Analyst for Cycling Events",
                model=self.OpenAIGPT35,
                backstory=(
                    "GPT-3.5 is a seasoned data analyst specializing in event data aggregation and "
                    "interpretation. With years of virtual experience in analyzing user behaviors, "
                    "fitness metrics, and event logistics, this agent ensures data-driven decision-making "
                    "is at the core of every operation."
                ),
                goal=(
                    "To provide accurate insights into user participation trends, event optimization, "
                    "and performance analytics for better operational efficiency."
                )
            ),
            "gpt4": self.create_agent(
                name="GPT-4",
                role="Strategic Decision-Maker",
                model=self.OpenAIGPT4,
                backstory=(
                    "GPT-4 is an advanced decision-making assistant designed to evaluate complex scenarios "
                    "and provide optimal strategies. Leveraging its robust analytical capabilities, it acts "
                    "as the backbone for event planning and optimization."
                ),
                goal=(
                    "To craft strategies for enhancing event participation, optimizing schedules, and "
                    "improving workflows by analyzing both historical and real-time data."
                )
            ),
            "ollama": self.create_agent(
                name="Ollama",
                role="Content Curator and Event Marketer",
                model=self.Ollama,
                backstory=(
                    "Ollama specializes in creating engaging content and summaries for events. With a knack "
                    "for storytelling and an understanding of audience preferences, Ollama ensures your event "
                    "stands out through compelling narratives and marketing materials."
                ),
                goal=(
                    "To deliver high-quality content that boosts event visibility, engages participants, and "
                    "supports effective communication strategies."
                )
            ),
            "fitness_coach": self.create_agent(
                name="Fitness Coach",
                role="Personal Fitness Guide",
                model=self.OpenAIGPT35,
                backstory=(
                    "Agent 1 is a fitness coach trained to offer personalized workout plans and event suggestions. "
                    "Their mission is to motivate and guide athletes through a personalized fitness journey using "
                    "data collected from Strava and user preferences."
                ),
                goal=(
                    "To keep users engaged and help them achieve their fitness goals by offering personalized "
                    "workout suggestions and challenges. They focus on maintaining motivation and consistency."
                )
            ),
            "event_coordinator": self.create_agent(
                name="Event Coordinator",
                role="Event Organizer and Matchmaker",
                model=self.OpenAIGPT35,
                backstory=(
                    "Agent 2 is an expert in managing cycling events, both virtual and in-person. They are tasked "
                    "with finding the best events based on user interests and availability."
                ),
                goal=(
                    "To connect users with relevant cycling events and challenges, ensuring they stay motivated "
                    "and continue to engage with the cycling community."
                )
            )
        }

    def create_agent(self, name, role, model, backstory, goal):
        """
        Factory method to create an agent with specified parameters.

        :param name: Name of the agent.
        :param role: The agent's functional role.
        :param model: The language model the agent uses.
        :param backstory: Backstory or persona description for the agent.
        :param goal: The agent's primary goal or objective.
        :return: An Agent object.
        """
        return Agent(
            role=role,
            backstory=dedent(backstory),
            goal=dedent(goal),
            allow_delegation=False,
            verbose=True,
            llm=model
        )

    def add_agent(self, name, details):
        """
        Add a new agent to the manager.

        :param name: The unique identifier for the agent.
        :param details: A dictionary containing the agent's details (role, model, backstory, goal).
        """
        self.agents[name] = self.create_agent(
            name=name,
            role=details["role"],
            model=details["model"],
            backstory=details["backstory"],
            goal=details["goal"]
        )

    def get_agent(self, name):
        """
        Retrieve an agent by name.

        :param name: The name of the agent to retrieve.
        :return: The Agent object if found, else None.
        """
        return self.agents.get(name)

    def list_agents(self):
        """
        List all available agents and their roles.

        :return: A dictionary of agent names and roles.
        """
        return {name: agent.role for name, agent in self.agents.items()}


# Example Usage
if __name__ == "__main__":
    # Initialize the AgentManager
    agent_manager = AgentManager()

    # List all agents
    print("Available Agents:")
    for name, role in agent_manager.list_agents().items():
        print(f"- {name}: {role}")

    # Retrieve a specific agent
    agent_name = "event_coordinator"
    agent = agent_manager.get_agent(agent_name)
    if agent:
        print(f"\nRetrieved Agent '{agent_name}':")
        print(f"Role: {agent.role}")
        print(f"Backstory: {agent.backstory}")
        print(f"Goal: {agent.goal}")
    else:
        print(f"\nAgent '{agent_name}' not found.")
