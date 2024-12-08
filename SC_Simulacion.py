import random

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

# Modificamos la tarea de recolección para simular la solicitud a la API
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
            events=events
        )
