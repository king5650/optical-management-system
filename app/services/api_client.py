import requests
from app.config.app_config import SERVER_URL, TIMEOUT


def get_patients():
    response = requests.get(
        f"{SERVER_URL}/auth/",
        timeout=TIMEOUT
    )
    response.raise_for_status()
    return response.json()
