import pandas as pd

from database.connection import get_connection, close_connection


def load_market_data():

    connection = get_connection()

    if connection is None:
        raise RuntimeError("Could not connect to MySQL.")

    query = """
        SELECT
            event_id,
            symbol,
            event_time,
            price,
            volume
        FROM market_events
        ORDER BY event_time
    """

    dataframe = pd.read_sql(query, connection)

    close_connection(connection)

    return dataframe


if __name__ == "__main__":

    data = load_market_data()

    print("\nMarket data loaded successfully.")
    print("Total records:", len(data))

    print("\nFirst 10 records:")
    print(data.head(10))

    print("\nSymbols available:")
    print(data["symbol"].unique())