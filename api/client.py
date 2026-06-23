import requests

BASE_URL = "http://127.0.0.1:8000/auth"

class ApiClient:

    @staticmethod
    def get(endpoint):
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def post(endpoint, data):
        response = requests.post(f"{BASE_URL}{endpoint}", json=data)
        if response.status_code >= 400:
            raise Exception(response.json())
        return response.json()