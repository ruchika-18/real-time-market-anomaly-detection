import pandas as pd
import matplotlib.pyplot as plt

from analytics.data_loader import load_market_data
from analytics.market_analytics import calculate_analytics
from models.anomaly_detector import detect_anomalies


def main():

    print("Loading market data...")

    df = load_market_data()

    df = calculate_analytics(df)

    df = detect_anomalies(df)

    stocks = df["symbol"].unique()

    fig, axes = plt.subplots(
        len(stocks),
        2,
        figsize=(16, 12)
    )

    fig.suptitle(
        "Real-Time Market Anomaly & Risk Analytics",
        fontsize=20,
        fontweight="bold"
    )

    for i, symbol in enumerate(stocks):

        stock = df[df["symbol"] == symbol].copy()

        # -----------------------------
        # PRICE + ANOMALIES
        # -----------------------------

        axes[i, 0].plot(
            stock["event_time"],
            stock["price"],
            label="Price"
        )

        anomalies = stock[stock["is_anomaly"] == True]

        axes[i, 0].scatter(
            anomalies["event_time"],
            anomalies["price"],
            marker="x",
            s=80,
            label="Anomaly"
        )

        axes[i, 0].set_title(
            f"{symbol} - Price & Anomalies"
        )

        axes[i, 0].set_ylabel("Price")

        axes[i, 0].legend()

        axes[i, 0].grid(True)

        # -----------------------------
        # VOLUME
        # -----------------------------

        axes[i, 1].plot(
            stock["event_time"],
            stock["volume"],
            label="Trading Volume"
        )

        axes[i, 1].set_title(
            f"{symbol} - Trading Volume"
        )

        axes[i, 1].set_ylabel("Volume")

        axes[i, 1].legend()

        axes[i, 1].grid(True)

    plt.tight_layout()

    plt.savefig(
        "market_anomaly_dashboard.png",
        dpi=150
    )

    print("\nDashboard saved as:")
    print("market_anomaly_dashboard.png")

    plt.show()


if __name__ == "__main__":
    main()