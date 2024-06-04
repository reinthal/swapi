
import requests
from dagster import asset, graph
from dagster_duckdb import DuckDBResource
import pandas as pd

@asset
def films() -> pd.DataFrame:
    response = requests.get('https://swapi.dev/api/films/')
    return pd.DataFrame(response.json()["results"])

@asset
def stg_films(films,  duckdb: DuckDBResource) -> None:
    duckdb.sql("CREATE TABLE stg_films AS SELECT * FROM films")

@asset
def stg_vehicles(vehicles,  duckdb: DuckDBResource) -> None:
    duckdb.sql("CREATE TABLE stg_vehicles AS SELECT * FROM vehicles")

@asset
def stg_people(people,  duckdb: DuckDBResource) -> None:
    duckdb.sql("CREATE TABLE stg_people AS SELECT * FROM people")

@asset
def vehicles() -> pd.DataFrame:
    response = requests.get('https://swapi.dev/api/vehicles/')
    return response.json()

@asset
def people() -> pd.DataFrame:
    response = requests.get('https://swapi.dev/api/people/')
    return response.json()

@graph
def star_wars_graph():
    films()
    vehicles()
    people()

star_wars_job = star_wars_graph.to_job()


