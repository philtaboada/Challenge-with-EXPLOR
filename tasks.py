from crewai import Task
from textwrap import dedent
from agents import AgentManager  # Assuming you have the complete agents.py file

class CustomTasks:
    def __init__(self):
        """
        Initialize the CustomTasks class with an instance of AgentManager.
        """
        self.agent_manager = AgentManager()

    def __tip_section(self):
        """
        Provide a motivational tip or message for tasks.
        """
        return "Remember: Collaboration and precision lead to great results!"

    def task_1_define_event(self):
        """
        Define task 1: Event creation and configuration.
        
        :return: A Task object for event definition.
        """
        agent_name = "event_coordinator"
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        location = "San Francisco, CA"
        date = "2024-12-15"
        organizer = "Cycling Club"
        event_type = "Cycling Race"
        surface = "Road"
        registration_link = "https://example.com/register"
        route_name = "Golden Gate Bridge Loop"
        route_length = 50  # km
        route_map = "https://example.com/map"
        route_elevation = 150  # meters

        return Task(
            description=dedent(
                f"""
                Task 1: Define a cycling event.

                Event Details:
                - Location: {location}
                - Date: {date}
                - Organizer: {organizer}
                - Event Type: {event_type}
                - Surface Type: {surface}
                - Route Name: {route_name}
                - Route Length: {route_length} km
                - Route Elevation: {route_elevation} meters

                Useful Links:
                - Registration Link: {registration_link}
                - Route Map: {route_map}

                {self.__tip_section()}
                """
            ),
            expected_output="A fully defined event with all necessary details.",
            agent=agent,
        )

    def task_2_analyze_data(self):
        """
        Define task 2: Analyze event-related data.
        
        :return: A Task object for data analysis.
        """
        agent_name = "gpt3.5"
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        event_data = {"participants": 100, "feedback": "positive"}

        return Task(
            description=dedent(
                f"""
                Task 2: Analyze event data to extract meaningful insights.

                Data Source:
                - Participant count: {event_data['participants']}
                - Feedback summary: {event_data['feedback']}

                Responsibilities:
                - Analyze participant trends.
                - Identify performance metrics.
                - Generate actionable insights for event improvement.

                {self.__tip_section()}
                """
            ),
            expected_output="Insights and recommendations based on the analyzed data.",
            agent=agent,
        )

    def task_3_generate_content(self):
        """
        Define task 3: Generate promotional content for the event.
        
        :return: A Task object for content generation.
        """
        agent_name = "ollama"
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        event_name = "Golden Gate Cycling Challenge"
        key_highlights = "Scenic views, challenging routes, professional organization."
        target_audience = "Professional cyclists and cycling enthusiasts."

        return Task(
            description=dedent(
                f"""
                Task 3: Generate promotional content for '{event_name}'.

                Event Highlights:
                - {key_highlights}

                Target Audience:
                - {target_audience}

                Objective:
                - Create engaging and persuasive content to promote the event.

                {self.__tip_section()}
                """
            ),
            expected_output="A marketing-ready content piece for the event.",
            agent=agent,
        )

    def batch_task_execution(self):
        """
        Execute a batch of tasks sequentially or concurrently using agents.
        
        :return: A Task object for batch processing.
        """
        agent_name = "gpt4"
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        tasks = [
            self.task_1_define_event(),
            self.task_2_analyze_data(),
            self.task_3_generate_content()
        ]

        task_descriptions = "\n".join([f"Task {i+1}: {task.description}" for i, task in enumerate(tasks)])

        return Task(
            description=dedent(
                f"""
                Execute a batch of tasks using the assigned agent.

                Tasks:
                {task_descriptions}

                {self.__tip_section()}
                """
            ),
            expected_output="Batch tasks executed successfully.",
            agent=agent,
        )


# Example Usage
if __name__ == "__main__":
    # Initialize the CustomTasks
    custom_tasks = CustomTasks()

    # Execute Task 1: Define Event
    task1 = custom_tasks.task_1_define_event()
    print(f"Task 1 Description:\n{task1.description}\n")

    # Execute Task 2: Analyze Data
    task2 = custom_tasks.task_2_analyze_data()
    print(f"Task 2 Description:\n{task2.description}\n")

    # Execute Task 3: Generate Content
    task3 = custom_tasks.task_3_generate_content()
    print(f"Task 3 Description:\n{task3.description}\n")

    # Execute Batch Task Execution
    batch_task = custom_tasks.batch_task_execution()
    print(f"Batch Task Execution Description:\n{batch_task.description}\n")
