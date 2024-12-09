# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            Do something as part of task 1
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            Use this variable: {var1}
            And also this variable: {var2}
        """
            ),
            expected_output="The expected output of the task",
            agent=agent,
        )

    def task_2_name(self, agent, location, date, organizer, organizer_base_location, event_type, surface, registration_link, currency, route_name, route_length, route_map, route_elevation, route_elevation_profile):
        # Normalizing event information
        normalized_event = {
            "event_name": "Cycling Event in Peru",
            "location": location,
            "date": date,
            "organizer": organizer,
            "organizer_base_location": organizer_base_location,
            "attributes": {
                "event_type": event_type,
                "surface": surface,
            },
            "registration_link": registration_link,
            "currency": currency,
        }
        # Normalizing route information
        route_info = {
            "route_name": route_name,
            "route_length": route_length,
            "route_map": route_map,
            "route_elevation": route_elevation,
            "route_elevation_profile": route_elevation_profile,
        }

        # Here, we can assume the agent filters and cleans the data before storing or processing it.
        cleaned_event_data = self.clean_event_data(normalized_event, route_info)

        # Now, store or process the cleaned event data (this part depends on how you want to save/store it)
        # For demonstration purposes, we just return the cleaned event data.
        return Task(
            description=dedent(
                f"""
            Normalize and store event data:
            Event details: {cleaned_event_data['event_name']} at {cleaned_event_data['location']} on {cleaned_event_data['date']}
            
            {self.__tip_section()}

            Make sure the data is cleaned and ready for storage or further processing.
        """
            ),
            expected_output="Cleaned event data",
            agent=agent,
        )

    def clean_event_data(self, event_data, route_data):
        # Cleaning and organizing the event data
        cleaned_event = {
            "event": event_data,
            "route": route_data,
            "status": "cleaned"
        }
        # In this function, you would implement logic to filter out any unnecessary or malformed data.
        # This could involve removing incomplete fields, correcting formats, or removing irrelevant information.
        return cleaned_event

