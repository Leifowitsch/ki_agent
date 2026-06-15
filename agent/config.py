import os
from dotenv import load_dotenv

load_dotenv()


API_KEY=os.environ.get("API_KEY_GEMINI")
if not API_KEY:
    raise ValueError("Fehler beim API_KEY: Keiner Vorhanden")


MODEL_NAME= "gemini-1.5-flash"
MAX_RETRIES = 15
