
from dlt import pipeline
from typing import Iterable
from dataclasses import dataclass
from dlt.extract.resource import DltResource
from dagster import AssetExecutionContext, AssetKey, SourceAsset
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dagster_embedded_elt.dlt.translator import DagsterDltTranslator
from data_sources.swapi import swapi
from dagster._annotations import public


swapi_pipeline_upstream_asset = SourceAsset("swapi_pipeline", group_name="star_wars")

@dataclass
class SwapiDltTranslator(DagsterDltTranslator):
    """inspired by: https://github.com/dagster-io/dagster/issues/21049#issuecomment-2043147862"""

    @public
    def get_deps_asset_keys(self, resource: DltResource) -> Iterable[AssetKey]:
        return [AssetKey(["swapi_pipeline"])]

@dlt_assets(
    dlt_source=swapi(),
    dlt_pipeline=pipeline(
        pipeline_name="swapi_pipeline",
        dataset_name="star_wars",
        destination="snowflake",
        progress="log",
    ),
    name="swapi",
    group_name="star_wars",
    dlt_dagster_translator=SwapiDltTranslator()
)
def swapi_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)

