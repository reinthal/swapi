
from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from data_sources.swapi import swapi

dlt_resource = DagsterDltResource()

@dlt_assets(
    dlt_source=swapi(),
    dlt_pipeline=pipeline(
        pipeline_name="swapi",
        destination="snowflake",
        dataset_name="swapi",
         progress="log",
    ),
    name="swapi",
    group_name="swapi",
)
def swapi_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)




