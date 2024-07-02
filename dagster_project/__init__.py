from dagster import Definitions, load_assets_from_package_module
from dagster_project.resources import snowflake_resource, dlt_resource
from dagster_project.jobs import swapi_job
from dagster_project.schedules import swapi_schedule
from dagster_project import assets

all_assets = load_assets_from_package_module(assets)

# Definitions
defs = Definitions(
    assets=all_assets,
    jobs=[swapi_job],
    schedules=[swapi_schedule],
    resources={
        "snowflake": snowflake_resource,
        "dlt": dlt_resource,
    }
)
