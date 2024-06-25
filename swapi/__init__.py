import os
from dataclasses import dataclass
from dagster import Definitions, load_assets_from_modules, EnvVar
from . import assets
from dagster_snowflake_pandas import SnowflakePandasIOManager

all_assets = load_assets_from_modules([assets])

@dataclass
class SnowflakeConfiguration:
    database: str = EnvVar("SNOWFLAKE_DATABASE")
    account: str = EnvVar("SNOWFLAKE_ACCOUNT")
    user: str = EnvVar("SNOWFLAKE_USER")
    password: str = EnvVar("SNOWFLAKE_PASSWORD")
    role: str = EnvVar("SNOWFLAKE_ROLE")
    warehouse: str = EnvVar("SNOWFLAKE_WAREHOUSE")
    schema: str = EnvVar("SNOWFLAKE_SCHEMA")

defs = Definitions(
    assets=all_assets,
    resources={
        "io_manager": SnowflakePandasIOManager(
            database=SnowflakeConfiguration.database,
            account=SnowflakeConfiguration.account,
            user=SnowflakeConfiguration.user,
            schema=SnowflakeConfiguration.schema,
            password=SnowflakeConfiguration.password,
            role=SnowflakeConfiguration.role,
            warehouse=SnowflakeConfiguration.warehouse,
        )
    }

)
