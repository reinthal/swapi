import dlt
from dlt.common import logger
from dlt.sources.helpers import requests
from typing import Any


@dlt.source
def swapi() -> Any:
    base_url = "https://swapi.dev/api/"
    
    def _get_data(endpoint):
        logger.info(f"Extracting {endpoint}")
        print(f"Extracting {endpoint}")
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
    logger.info("Starting pipeline")
    source = swapi()
    pipeline = dlt.pipeline(
        pipeline_name="swapi",
        destination="snowflake",
        dataset_name="swapi"
    )
    pipeline.run(source, write_disposition="replace")