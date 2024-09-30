from dagster import asset, MetadataValue, MaterializeResult
from dagster_duckdb import DuckDBResource
import requests
import pandas as pd
import os
from dagster_university.assets import constants
from dagster_university.partitions import hourly_partition

@asset(
    group_name="service_requests",
    compute_kind="Python",
    partitions_def=hourly_partition,
)
def get_service_requests_for_hour(context) -> MaterializeResult:
    """
        Fetches service requests for a specific hour and saves them as a parquet file.
    """

    
    start_date = context.asset_partition_key_for_output()
    date = start_date[:10]
    hour = start_date[11:13] + ":00"
    formated_start_date = date + "T" + hour

    end_date = formated_start_date[:13] + ":59:59"

    # Base URL for the New York City Open Data API
    base_url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    
    # Construct the start and end date for the hourly query

    # Building the query parameters
    query = f"SELECT * WHERE `created_date` BETWEEN '{formated_start_date}'::floating_timestamp AND '{end_date}'::floating_timestamp ORDER BY `created_date` DESC NULL FIRST"
    
    params = {
        "$query": query,
    }
    
    # Sending the GET request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        df = pd.DataFrame(response.json())

        # Extract the date and hour from the input hour
        date = start_date[:10]  # 'YYYY-MM-DD'
        hour_str = start_date[11:13]  # 'HH'

        # Construct the file path
        file_path = constants.SERVICE_AREA_REQUEST_PATH.format(date=date, hour=hour_str)

        
        if os.getenv("DAGSTER_ENVIRONMENT") == "dev":
            # create the directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # lowercase the column names and replace spaces with underscores
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        df.to_parquet(file_path, index=False)
        
    else:
        raise Exception(f"Error fetching data: {response.status_code}, {response.text}")



@asset(
    deps=["get_service_requests_for_hour"],
    group_name="service_requests",
    partitions_def=hourly_partition,
    compute_kind="DuckDB",
)
def service_requests(context, database: DuckDBResource):
    """
        The raw service requests dataset, loaded into a DuckDB database.
    """

    partition_date_str = context.asset_partition_key_for_output()
    date = partition_date_str[:10]
    hour = partition_date_str[11:13]

    file_name = constants.SERVICE_AREA_REQUEST_PATH.format(date=date, hour=hour)
    query = f"""
        create or replace table {constants.RAW_DATA_SCHEMA}.service_requests as (
            select
                *
            from '{file_name}'
        );
    """

    with database.get_connection() as conn:
        conn.execute(query)