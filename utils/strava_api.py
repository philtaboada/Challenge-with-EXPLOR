# in this section we will use the strava api to get the user's activities

from langchain_groq import ChatGroq


class StravaAPI:
    def __init__(self):
        self.groq = ChatGroq(model="llama3-8b-8192")
        self.client_id = os.getenv("STRAVA_CLIENT_ID")
        self.client_secret = os.getenv("STRAVA_CLIENT_SECRET")
        self.access_token = os.getenv("STRAVA_ACCESS_TOKEN")
        self.refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")

    def get_activities(self):
        # get the user's activities
        pass
