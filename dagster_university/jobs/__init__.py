from dagster import define_asset_job, AssetSelection
from dagster_dbt import build_dbt_asset_selection

from ..assets.dbt import dbt_analytics
from ..partitions import (
    monthly_partition, 
    weekly_partition, 
    daily_partition, 
    hourly_partition,
)

dbt_trips_selection = build_dbt_asset_selection([dbt_analytics], "stg_trips").downstream()

service_request_update_job = define_asset_job(
    name="service_request_update_job",
    partitions_def=hourly_partition,
    selection=AssetSelection.all()  - dbt_trips_selection
)
