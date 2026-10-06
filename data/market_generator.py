import random
import time
from datetime import datetime

from database.connection import get_connection, close_connection


STOCKS = {
    "AAPL": {
        "price": 250.00,
        "base_volume": 1000
    },
    "MSFT": {
        "price": 500.00,
        "base_volume": 900
    },
    "NVDA": {
        "price": 180.00,
        "base_volume": 1200
    },
    "AMZN": {
        "price": 230.00,
        "base_volume": 800
    }
}


def generate_market_event(stock):
    current_price = STOCKS[stock]["price"]
    base_volume = STOCKS[stock]["base_volume"]

    price_change = random.uniform(-0.003, 0.003)

    volume = int(
        random.uniform(0.7, 1.3) * base_volume
    )

    # Occasionally generate an unusual market event
    if random.random() < 0.05:
        price_change = random.uniform(-0.08, 0.08)
        volume = int(random.uniform(3, 8) * base_volume)

    new_price = current_price * (1 + price_change)

    STOCKS[stock]["price"] = new_price

    return {
        "symbol": stock,
        "event_time": datetime.now(),
        "price": round(new_price, 4),
        "volume": volume
    }


def insert_event(connection, event):
    query = """
        INSERT INTO market_events
        (symbol, event_time, price, volume)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        event["symbol"],
        event["event_time"],
        event["price"],
        event["volume"]
    )

    cursor = connection.cursor()

    cursor.execute(query, values)

    connection.commit()

    cursor.close()


def main():
    connection = get_connection()

    if connection is None:
        print("Could not connect to MySQL.")
        return

    print("Starting market data generator...")
    print("Press Ctrl+C to stop.")

    try:
        while True:

            for stock in STOCKS:

                event = generate_market_event(stock)

                insert_event(connection, event)

                print(
                    f"{event['event_time']} | "
                    f"{event['symbol']} | "
                    f"Price: {event['price']} | "
                    f"Volume: {event['volume']}"
                )

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMarket data generator stopped.")

    finally:
        close_connection(connection)


if __name__ == "__main__":
    main()