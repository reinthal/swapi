from dagster import Definitions
from dagster_project.resources import snowflake_resource, dlt_resource
from dagster_project.assets.swapi import swapi_assets, swapi_pipeline_upstream_asset


# Assets
all_assets = [swapi_pipeline_upstream_asset, swapi_assets]

# Definitions
defs = Definitions(
    assets=all_assets,
    resources={
        "snowflake": snowflake_resource,
        "dlt": dlt_resource,
    }
)
