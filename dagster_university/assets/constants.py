import os
from datetime import datetime

S3_BUCKET_PREFIX = os.getenv("S3_BUCKET_PREFIX")

def get_path_for_env(path: str) -> str:
    """A utility method for Dagster University. Generates a path based on the environment.

    Args:
        path (str): The local path to the file.

    Returns:
        result_path (str): The path to the file, based on the environment.
    """
    if os.getenv("DAGSTER_ENVIRONMENT") == "prod":
        return S3_BUCKET_PREFIX + path
    else:
        return path

SERVICE_AREA_REQUEST_PATH = get_path_for_env("data/raw/service_area/{date}/{hour}.parquet")

TAXI_ZONES_FILE_PATH = get_path_for_env("data/raw/taxi_zones.csv")
TAXI_TRIPS_TEMPLATE_FILE_PATH = get_path_for_env("data/raw/taxi_trips_{}.parquet")

TAXI_ZONES_FILE_PATH = get_path_for_env(os.path.join("data", "raw", "taxi_zones.csv"))
TAXI_TRIPS_TEMPLATE_FILE_PATH = get_path_for_env(os.path.join("data", "raw", "taxi_trips_{}.parquet"))

TRIPS_BY_AIRPORT_FILE_PATH = get_path_for_env(os.path.join("data", "outputs", "trips_by_airport.csv"))

MANHATTAN_STATS_FILE_PATH = get_path_for_env(os.path.join("data", "staging", "manhattan_stats.geojson"))
MANHATTAN_MAP_FILE_PATH = get_path_for_env(os.path.join("data", "outputs", "manhattan_map.png"))

REQUEST_DESTINATION_TEMPLATE_FILE_PATH = get_path_for_env(os.path.join("data", "outputs", "{}.png"))

DATE_FORMAT = "%Y-%m-%d"



START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 4, 1)


DBT_DIRECTORY = os.path.abspath(os.path.join(__file__, "..", "..", "..", "analytics"))

AIRPORT_TRIPS_FILE_PATH = get_path_for_env(os.path.join("data", "outputs", "airport_trips.png"))


RAW_DATA_SCHEMA = "raw_data"