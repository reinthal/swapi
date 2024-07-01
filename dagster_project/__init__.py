from dagster import Definitions, load_assets_from_modules, EnvVar
from dagster_snowflake import SnowflakeIOManager
from dagster_embedded_elt.dlt import DagsterDltResource

from dagster_project.assets import swapi_assets

# Resources
dlt_resource = DagsterDltResource()
snowflake_resource = SnowflakeIOManager(
            database=EnvVar("DESTINATION__SNOWFLAKE__CREDENTIALS__DATABASE"),
            account=EnvVar("DESTINATION__SNOWFLAKE__CREDENTIALS__HOST"),
            user=EnvVar("DESTINATION__SNOWFLAKE__CREDENTIALS__USERNAME"),
            password=EnvVar("DESTINATION__SNOWFLAKE__CREDENTIALS__PASSWORD"),
            role=EnvVar("DESTINATION__SNOWFLAKE__CREDENTIALS__ROLE"),
            warehouse=EnvVar("DESTINATION__SNOWFLAKE__CREDENTIALS__WAREHOUSE"),
        )

# Assets
all_assets = [swapi_assets]

# Definitions
defs = Definitions(
    assets=all_assets,
    resources={
        "io_manager": snowflake_resource,
        "dlt": dlt_resource,
    }
)
