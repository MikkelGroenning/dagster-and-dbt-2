from dagster import MonthlyPartitionsDefinition, WeeklyPartitionsDefinition, DailyPartitionsDefinition, HourlyPartitionsDefinition

from  dagster_university.assets import constants

## Lesson 8 
start_date = constants.START_DATE
end_date = constants.END_DATE


monthly_partition = MonthlyPartitionsDefinition(
    start_date=start_date,
    end_date=end_date
)

weekly_partition = WeeklyPartitionsDefinition(
    start_date=start_date,
    end_date=end_date
)

daily_partition = DailyPartitionsDefinition(
    start_date=start_date,
    end_date=end_date
)

hourly_partition = HourlyPartitionsDefinition(
    start_date=start_date,
    end_date=end_date
)