import pandas as pd

from database.connection import get_connection, close_connection


def save_analytics(dataframe):

    connection = get_connection()

    if connection is None:
        raise RuntimeError("Could not connect to MySQL.")

    cursor = connection.cursor()

    # Clear old analytics results
    cursor.execute("DELETE FROM market_analytics")

    insert_query = """
        INSERT INTO market_analytics (
            symbol,
            event_time,
            price,
            volume,
            return_pct,
            moving_average,
            volatility,
            volume_ratio,
            anomaly_score,
            is_anomaly
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    rows_saved = 0

    for _, row in dataframe.iterrows():

        values = (
            row["symbol"],
            row["event_time"],
            float(row["price"]),
            int(row["volume"]),

            None if pd.isna(row["return_pct"])
            else float(row["return_pct"]),

            None if pd.isna(row["moving_average"])
            else float(row["moving_average"]),

            None if pd.isna(row["volatility"])
            else float(row["volatility"]),

            None if pd.isna(row["volume_ratio"])
            else float(row["volume_ratio"]),

            float(row["anomaly_score"]),

            bool(row["is_anomaly"])
        )

        cursor.execute(insert_query, values)

        rows_saved += 1

    connection.commit()

    cursor.close()
    close_connection(connection)

    return rows_saved