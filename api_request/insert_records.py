from google.cloud import bigquery
from weather_api_request import mock_fetch_data, fetch_data
from datetime import datetime

# CONFIG
PROJECT_ID = "gothic-sled-453213-i2"
DATASET_ID = "weather_data"
TABLE_ID = "raw_weather_data"

def get_bq_client():
    print("Connecting to BigQuery...")
    client = bigquery.Client(project=PROJECT_ID)
    print("Connected to BigQuery")
    return client


def create_table_if_not_exists(client):
    print("Creating dataset and table if not exists...")

    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    dataset_ref.location = "US"
    client.create_dataset(dataset_ref, exists_ok=True)

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    schema = [
        bigquery.SchemaField("city", "STRING"),
        bigquery.SchemaField("temperature", "FLOAT"),
        bigquery.SchemaField("weather_descriptions", "STRING"),
        bigquery.SchemaField("wind_speed", "FLOAT"),
        bigquery.SchemaField("time", "TIMESTAMP"),
        bigquery.SchemaField("inserted_at", "TIMESTAMP"),
        bigquery.SchemaField("utc_offset", "STRING"),
    ]

    table = bigquery.Table(table_ref, schema=schema)
    client.create_table(table, exists_ok=True)

    print("Table is ready")


def insert_record(client, data):
    print("Inserting record into BigQuery...")

    weather = data["current"]
    location = data["location"]

    rows_to_insert = [
        {
            "city": location["name"],
            "temperature": weather["temperature"],
            "weather_descriptions": weather["weather_descriptions"][0],
            "wind_speed": weather["wind_speed"],
            "time": location["localtime"],
            "inserted_at": datetime.utcnow().isoformat(),
            "utc_offset": location["utc_offset"],
        }
    ]

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    errors = client.insert_rows_json(table_ref, rows_to_insert)

    if errors:
        raise Exception(f"BigQuery insert errors: {errors}")

    print("Data successfully inserted")


def main():
    try:
        # data = mock_fetch_data()
        data = fetch_data()

        client = get_bq_client()
        create_table_if_not_exists(client)
        insert_record(client, data)

    except Exception as e:
        print(f"An error occurred during execution: {e}")


if __name__ == "__main__":
    main()
