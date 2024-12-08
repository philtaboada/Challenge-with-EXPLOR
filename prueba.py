from crewai import Agent, Task, Crew
from textwrap import dedent
from langchain.llms import ChatOpenAI

# Configuración de los agentes
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    def agent_recolector(self):
        return Agent(
            role="Recolector de eventos",
            backstory=dedent("""
                Este agente busca eventos deportivos relevantes en función de la ubicación, el nivel y la fecha.
            """),
            goal=dedent("""
                Obtener una lista de eventos deportivos filtrados según las preferencias del usuario.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_personalizador(self):
        return Agent(
            role="Personalizador de eventos",
            backstory=dedent("""
                Este agente personaliza eventos deportivos según las necesidades del usuario.
            """),
            goal=dedent("""
                Seleccionar y recomendar los eventos más relevantes para el usuario.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

# Configuración de las tareas
class CustomTasks:
    def task_recolectar(self, agent, location, level, date):
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
        )

    def task_personalizar(self, agent):
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
        )

# Configuración del Crew
class CustomCrew:
    def __init__(self, location, level, date):
        self.location = location
        self.level = level
        self.date = date

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        recolector = agents.agent_recolector()
        personalizador = agents.agent_personalizador()

        tarea_1 = tasks.task_recolectar(recolector, self.location, self.level, self.date)
        tarea_2 = tasks.task_personalizar(personalizador)

        crew = Crew(
            agents=[recolector, personalizador],
            tasks=[tarea_1, tarea_2],
            verbose=True,
        )

        return crew.kickoff()

# Punto de entrada principal
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
