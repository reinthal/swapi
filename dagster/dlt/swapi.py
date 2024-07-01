import dlt
from dlt.sources.helpers import requests
from typing import Any


@dlt.source
def swapi() -> Any:
    # Create a REST API configuration for the GitHub API
    # Use RESTAPIConfig to get autocompletion and type checking
    @dlt.resource
    def films():
        base_url = "https://swapi.dev/api/films"
        response = requests.get(base_url)
        response.raise_for_status()

        return response.json()

    @dlt.resource
    def vehicles():
        base_url = "https://swapi.dev/api/vehicles"
        response = requests.get(base_url)
        response.raise_for_status()
        
        return response.json()

    @dlt.resource
    def people():
        base_url = "https://swapi.dev/api/people"
        response = requests.get(base_url)
        response.raise_for_status()

        return response.json()


    yield films
    yield vehicles
    yield people


if __name__ == "__main__":
    pass