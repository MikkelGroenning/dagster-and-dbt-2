from dagster import ScheduleDefinition
from ..jobs import service_request_update_job
## Lesson 7
trip_update_schedule = ScheduleDefinition(
    job=service_request_update_job,
    cron_schedule="0 0 5 * *", # every 5th of the month at midnight
)
