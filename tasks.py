# tasks.py
from crewai import Task
from textwrap import dedent
from agent_manager import AgentManager

class CustomTasks:
    def __init__(self, agent_manager: AgentManager):
        """
        Initialize the CustomTasks class with an instance of AgentManager.
        
        :param agent_manager: An instance of AgentManager for managing and retrieving agents.
        """
        self.agent_manager = agent_manager

    def __tip_section(self):
        """
        Provide a motivational tip or message for tasks.
        """
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent_name, var1, var2):
        """
        Define task 1 and assign it to a specific agent.
        
        :param agent_name: Name of the agent responsible for this task.
        :param var1: First variable for the task.
        :param var2: Second variable for the task.
        :return: A Task object.
        """
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        return Task(
            description=dedent(
                f"""
                Task 1: Perform specific operations with agent {agent_name}.
                
                {self.__tip_section()}

                Use these variables:
                  - Variable 1: {var1}
                  - Variable 2: {var2}
                
                Ensure to process the most recent cycling event data available.
                """
            ),
            expected_output="Processed event data output",
            agent=agent,
        )

    def task_2_name(self, agent_name, location, date, organizer, event_type, surface, registration_link, route_name, route_length, route_map, route_elevation):
        """
        Normalize and process event data from various input sources.
        
        :param agent_name: Name of the agent responsible for this task.
        :param location: The event's location.
        :param date: The event's date.
        :param organizer: Name of the event organizer.
        :param event_type: The type of cycling event (e.g., race, ride, etc.).
        :param surface: Type of surface for the event (e.g., road, gravel, etc.).
        :param registration_link: Link to register for the event.
        :param route_name: Name of the route for the event.
        :param route_length: Length of the route in kilometers.
        :param route_map: Link to the route map.
        :param route_elevation: Elevation of the route in meters.
        
        :return: A Task object with cleaned event data.
        """
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        # Normalizing event information
        normalized_event = {
            "event_name": "Cycling Event in Nigeria",
            "location": location,
            "date": date,
            "organizer": organizer,
            "event_type": event_type,
            "surface": surface,
            "registration_link": registration_link,
        }

        # Normalizing route information
        route_info = {
            "route_name": route_name,
            "route_length": route_length,
            "route_map": route_map,
            "route_elevation": route_elevation,
        }

        # Clean the event data
        cleaned_event_data = self.clean_event_data(normalized_event, route_info)

        return Task(
            description=dedent(
                f"""
                Normalize and store event data:
                Event details: {cleaned_event_data['event_name']} at {cleaned_event_data['location']} on {cleaned_event_data['date']}
                
                {self.__tip_section()}

                Ensure that all event data is cleaned and ready for further processing or storage.
                """
            ),
            expected_output="Cleaned event data",
            agent=agent,
        )

    def task_3_name(self, agent_name, additional_info):
        """
        Perform complex processing or aggregation of data.
        
        :param agent_name: Name of the agent responsible for this task.
        :param additional_info: Additional parameters or info for task processing.
        :return: A Task object with processed data output.
        """
        agent = self.agent_manager.get_agent(agent_name)
        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found in AgentManager.")

        # Example complex processing or aggregation (can be extended as per project needs)
        processed_data = f"Processed data based on {additional_info}."

        return Task(
            description=dedent(
                f"""
                Perform complex aggregation or data processing using the provided information:
                
                {self.__tip_section()}
                
                Data to be processed: {additional_info}
                """
            ),
            expected_output="Processed complex data",
            agent=agent,
        )

    def clean_event_data(self, event_data, route_data):
        """
        Clean and normalize the event and route data.
        
        :param event_data: Raw event data.
        :param route_data: Raw route data.
        :return: A dictionary with cleaned event and route data.
        """
        cleaned_event = {
            "event": event_data,
            "route": route_data,
            "status": "cleaned",
        }

        # Implement cleaning logic here, such as removing invalid data
        # Example: removing any empty fields or correcting date formats

        return cleaned_event
