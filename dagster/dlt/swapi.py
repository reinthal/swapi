import dlt
from dlt.sources.helpers import requests
from typing import Any


@dlt.source
def swapi() -> Any:
    # Create a REST API configuration for the GitHub API
    # Use RESTAPIConfig to get autocompletion and type checking
    base_url = "https://swapi.dev/api/"
    
    def _get_data(endpoint):
        response = requests.get(base_url + endpoint)
        response.raise_for_status()
        return response.json()
    
    @dlt.resource
    def films():
        yield _get_data("films")

    @dlt.resource
    def vehicles():
        yield _get_data("vehicles")

    @dlt.resource
    def people():
        yield _get_data("people")

    return films, vehicles, people


if __name__ == "__main__":

    pipeline = dlt.pipeline(
        pipeline_name="swapi",
        destination="snowflake",
        dataset_name="swapi"
    )
    pipeline.run()