from dagster import Definitions
from dagster_project.resources import snowflake_resource, dlt_resource
from dagster_project.assets.swapi import swapi_assets, swapi_pipeline_upstream_asset
from dagster_project.jobs import all_assets_job, dlt_swapi_films_job

# TODO import assets from assets module using `load_assets_from_module`



# Definitions
defs = Definitions(
    assets=[swapi_pipeline_upstream_asset, swapi_assets],
    jobs=[all_assets_job, dlt_swapi_films_job],
    resources={
        "snowflake": snowflake_resource,
        "dlt": dlt_resource,
    }
)
