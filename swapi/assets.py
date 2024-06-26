
import requests
from dagster import asset, graph
from dagster_duckdb import DuckDBResource
import pandas as pd

# TODO: Verifiera att vi har data i snowflake
# X TODO: Ta bort staging assets
# TODO: Lägg till DLT



@asset(
    key_prefix=["raw_swapi"]
)
def films() -> pd.DataFrame:
    response = requests.get('https://swapi.dev/api/films/')
    return pd.DataFrame(response.json()["results"])

@asset(
    key_prefix=["raw_swapi"]
)
def vehicles() -> pd.DataFrame:
    response = requests.get('https://swapi.dev/api/vehicles/')
    return pd.DataFrame(response.json()["results"])

@asset(
    key_prefix=["raw_swapi"]
)
def people() -> pd.DataFrame:
    response = requests.get('https://swapi.dev/api/people/')
    return pd.DataFrame(response.json()["results"])

@graph
def star_wars_graph():
    films()
    vehicles()
    people()

star_wars_job = star_wars_graph.to_job()


