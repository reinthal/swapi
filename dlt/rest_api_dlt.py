import dlt
from dlt.sources.helpers import requests
from typing import Any

from rest_api import(
    RESTAPIConfig,
    rest_api_resources
)

@dlt.source
def film_source() -> Any:
    # Create a REST API configuration for the GitHub API
    # Use RESTAPIConfig to get autocompletion and type checking
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://swapi.dev/api/",
        },
        "resources": [
        {
            "name": "films",
            "endpoint": {
                "data_selector": "results",
            },
        }
    ],
    }
    yield from rest_api_resources(config)


def load_film() -> None:

    pipeline = dlt.pipeline(
        pipeline_name="film",
        destination="snowflake",
        dataset_name="movies"
    )

    pipeline.run(film_source())


if __name__ == "__main__":
    load_film()