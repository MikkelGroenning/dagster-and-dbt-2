from dagster import Definitions, load_assets_from_modules

from dagster_university.assets import trips, dbt, service_requests
from dagster_university.resources import database_resource, dbt_resource
from dagster_university.jobs import service_request_update_job
from dagster_university.schedules import trip_update_schedule


## Lesson 5 -> prob every other section after that
trip_assets = load_assets_from_modules([trips])

service_request_assets = load_assets_from_modules([service_requests])

dbt_analytics_assets = load_assets_from_modules(modules=[dbt])

all_jobs = [service_request_update_job]
all_schedules = [trip_update_schedule]

defs = Definitions(
    assets=service_request_assets,
    resources={
        "database": database_resource,
        "dbt": dbt_resource,
    },
    jobs=all_jobs,
    schedules=all_schedules,
)