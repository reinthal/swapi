# TODO make schedule

from dagster import define_asset_job, AssetSelection
AssetSelection.groups("star_wars")

all_assets_job = define_asset_job(name="all_assets_job", description="Loads all assets in this repository")

dlt_swapi_films_job = \
    define_asset_job(
        name="swapi_job", 
        selection=AssetSelection.groups("star_wars"),
        description="Loads only `star_wars` group from this repository"
)
