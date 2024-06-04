
import requests
from dagster import asset, graph

@asset
def films():
    response = requests.get('https://swapi.dev/api/films/')
    return response.json()

@asset
def vehicles():
    response = requests.get('https://swapi.dev/api/vehicles/')
    return response.json()

@asset
def people():
    response = requests.get('https://swapi.dev/api/people/')
    return response.json()

@graph
def star_wars_graph():
    films()
    vehicles()
    people()

star_wars_job = star_wars_graph.to_job()


