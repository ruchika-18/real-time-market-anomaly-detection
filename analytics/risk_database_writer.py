import pandas as pd

from database.connection import get_connection, close_connection


def save_risk_metrics(dataframe):

    connection = get_connection()

    if connection is None:
        raise RuntimeError("Could not connect to MySQL.")

    cursor = connection.cursor()

    # Remove previous risk results
    cursor.execute("DELETE FROM risk_metrics")

    insert_query = """
        INSERT INTO risk_metrics (
            symbol,
            event_time,
            volatility,
            value_at_risk,
            sharpe_ratio,
            max_drawdown
        )
        VALUES (
            %s, %s, %s, %s, %s, %s
        )
    """

    rows_saved = 0

    for _, row in dataframe.iterrows():

        values = (
            row["symbol"],
            row["event_time"],
            float(row["volatility"]),
            float(row["value_at_risk"]),
            float(row["sharpe_ratio"]),
            float(row["max_drawdown"])
        )

        cursor.execute(
            insert_query,
            values
        )

        rows_saved += 1

    connection.commit()

    cursor.close()
    close_connection(connection)

    return rows_saved