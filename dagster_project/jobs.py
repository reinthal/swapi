# TODO make schedule

from dagster import define_asset_job, AssetSelection


swapi_job = \
    define_asset_job(
        name="swapi_job", 
        selection=AssetSelection.groups("star_wars"),
        description="Loads only `star_wars` group from this repository"
)
