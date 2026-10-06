import time

import matplotlib.pyplot as plt
import pandas as pd

from analytics.data_loader import load_market_data
from analytics.market_analytics import calculate_analytics
from models.anomaly_detector import detect_anomalies


REFRESH_SECONDS = 5
LATEST_RECORDS = 100


def prepare_data():

    # Load market data from MySQL
    market_data = load_market_data()

    if market_data.empty:
        return pd.DataFrame()

    # Calculate market features
    analytics_data = calculate_analytics(
        market_data
    )

    # Detect anomalies
    results = detect_anomalies(
        analytics_data
    )

    # Keep only the latest records for each stock
    latest_data = (
        results
        .sort_values("event_time")
        .groupby("symbol")
        .tail(LATEST_RECORDS)
        .copy()
    )

    return latest_data


def create_dashboard(data):

    if data.empty:

        print("No data available for dashboard.")

        return

    symbols = sorted(
        data["symbol"].unique()
    )

    fig, axes = plt.subplots(
        nrows=len(symbols),
        ncols=2,
        figsize=(16, 12)
    )

    # Handle case where only one symbol exists
    if len(symbols) == 1:
        axes = [axes]

    fig.suptitle(
        "Real-Time Market Anomaly Monitoring",
        fontsize=20,
        fontweight="bold"
    )

    for row, symbol in enumerate(symbols):

        symbol_data = (
            data[data["symbol"] == symbol]
            .sort_values("event_time")
            .copy()
        )

        # -----------------------------------------
        # PRICE + ANOMALIES
        # -----------------------------------------

        ax_price = axes[row][0]

        ax_price.plot(
            symbol_data["event_time"],
            symbol_data["price"],
            label="Price"
        )

        anomalies = symbol_data[
            symbol_data["is_anomaly"] == True
        ]

        if not anomalies.empty:

            ax_price.scatter(
                anomalies["event_time"],
                anomalies["price"],
                marker="x",
                s=80,
                label="Anomaly"
            )

        ax_price.set_title(
            f"{symbol} - Price / Anomalies"
        )

        ax_price.set_xlabel("Time")
        ax_price.set_ylabel("Price")

        ax_price.legend()

        ax_price.grid(
            True,
            alpha=0.3
        )

        # -----------------------------------------
        # TRADING VOLUME
        # -----------------------------------------

        ax_volume = axes[row][1]

        ax_volume.plot(
            symbol_data["event_time"],
            symbol_data["volume"],
            label="Volume"
        )

        ax_volume.set_title(
            f"{symbol} - Trading Volume"
        )

        ax_volume.set_xlabel("Time")
        ax_volume.set_ylabel("Volume")

        ax_volume.legend()

        ax_volume.grid(
            True,
            alpha=0.3
        )

    # Automatically arrange spacing
    plt.tight_layout(
        rect=[0, 0, 1, 0.96]
    )

    plt.show()


def main():

    print(
        "========================================"
    )

    print(
        "REAL-TIME MARKET DASHBOARD"
    )

    print(
        "========================================"
    )

    print(
        f"Refreshing every "
        f"{REFRESH_SECONDS} seconds."
    )

    print(
        "Close the dashboard window to stop."
    )

    while True:

        try:

            print(
                "\nLoading latest market data..."
            )

            data = prepare_data()

            if data.empty:

                print(
                    "Waiting for market data..."
                )

                time.sleep(
                    REFRESH_SECONDS
                )

                continue

            print(
                f"Displaying latest "
                f"{LATEST_RECORDS} records "
                f"per stock."
            )

            create_dashboard(data)

            # Wait before refreshing
            time.sleep(
                REFRESH_SECONDS
            )

        except KeyboardInterrupt:

            print(
                "\nDashboard stopped."
            )

            break

        except Exception as error:

            print(
                "\nDashboard error:",
                error
            )

            time.sleep(
                REFRESH_SECONDS
            )


if __name__ == "__main__":

    main()