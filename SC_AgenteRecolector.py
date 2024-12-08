from crewai import Agent, Task, Crew
from textwrap import dedent
from langchain.llms import ChatOpenAI
import logging
import json
import random

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Simulación de recolección de eventos deportivos
def simulate_api_request(location, level, date):
    event_types = ['Marathon', 'Triathlon', 'Cycling', 'Running', 'Swimming']
    events = []
    
    for i in range(5):
        event = {
            'name': f"Evento {i+1}",
            'date': date,
            'type': random.choice(event_types),
            'location': location,
            'link': f"https://www.strava.com/events/{i+1}"
        }
        events.append(event)
    
    logging.info(f"Eventos simulados para {location} en {date}: {events}")
    return events

# Validación de entradas del usuario
def validate_inputs(location, level, date):
    if not location or level not in ['Beginner', 'Intermediate', 'Advanced'] or len(date.split('-')) != 3:
        raise ValueError("Entrada inválida. Asegúrate de que la ubicación sea válida, el nivel sea uno de ['Beginner', 'Intermediate', 'Advanced'] y la fecha esté en formato YYYY-MM-DD.")
    logging.info(f"Entradas válidas: Ubicación={location}, Nivel={level}, Fecha={date}")
    return True

# Configuración de los agentes
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    def agent_recolector(self):
        return Agent(
            role="Recolector de eventos",
            backstory=dedent("""Este agente busca eventos deportivos relevantes en función de la ubicación, el nivel y la fecha."""),
            goal=dedent("""Obtener una lista de eventos deportivos filtrados según las preferencias del usuario."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_personalizador(self):
        return Agent(
            role="Personalizador de eventos",
            backstory=dedent("""Este agente personaliza eventos deportivos según las necesidades del usuario."""),
            goal=dedent("""Seleccionar y recomendar los eventos más relevantes para el usuario."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

# Configuración de las tareas
class CustomTasks:
    def task_recolectar(self, agent, location, level, date):
        events = simulate_api_request(location, level, date)
        return Task(
            description=dedent(
                f"""
                Buscar eventos deportivos en función de:
                - Ubicación: {location}
                - Nivel: {level}
                - Fecha: {date}

                Asegúrate de que los datos sean recientes y precisos.
                """
            ),
            expected_output="Lista de eventos filtrados por ubicación, nivel y fecha.",
            agent=agent,
            extra_data=events 
        )

    def task_personalizar(self, agent, events):
        return Task(
            description=dedent(
                f"""
                Personaliza la lista de eventos:
                - Filtra los eventos más relevantes según las preferencias del usuario.
                - Presenta una lista clara y fácil de entender.
                """
            ),
            expected_output="Lista de eventos personalizados y recomendados.",
            agent=agent,
            extra_data=events  
        )

# Configuración del Crew
class CustomCrew:
    def __init__(self, location, level, date):
        self.location = location
        self.level = level
        self.date = date

    def run(self):
        try:
            validate_inputs(self.location, self.level, self.date)

            agents = CustomAgents()
            tasks = CustomTasks()

            recolector = agents.agent_recolector()
            personalizador = agents.agent_personalizador()

            events = simulate_api_request(self.location, self.level, self.date)
            
            tarea_1 = tasks.task_recolectar(recolector, self.location, self.level, self.date)
            tarea_2 = tasks.task_personalizar(personalizador, events)

            crew = Crew(
                agents=[recolector, personalizador],
                tasks=[tarea_1, tarea_2],
                verbose=True,
            )

            results = crew.kickoff()

            with open("resultados_eventos.json", "w") as file:
                json.dump(events, file, indent=4)

            logging.info("Resultados exportados a 'resultados_eventos.json'")
            return results

        except Exception as e:
            logging.error(f"Error al ejecutar el Crew: {e}")
            return f"Error: {e}"

if __name__ == "__main__":
    print("## Bienvenido a CycleMatch AI")
    print("-------------------------------")
    
    location = input("Ingresa tu ubicación: ")
    level = input("Ingresa tu nivel (Beginner, Intermediate, Advanced): ")
    date = input("Ingresa la fecha (YYYY-MM-DD): ")
    
    crew = CustomCrew(location, level, date)
    result = crew.run()

    print("\n\n########################")
    print("## Resultados del Crew:")
    print("########################\n")
    print(result)
