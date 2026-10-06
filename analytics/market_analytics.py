import pandas as pd

from analytics.data_loader import load_market_data


def calculate_analytics(dataframe):

    df = dataframe.copy()

    # Make sure data is ordered correctly
    df = df.sort_values(
        by=["symbol", "event_time"]
    ).reset_index(drop=True)

    # Calculate percentage price change
    df["return_pct"] = (
        df.groupby("symbol")["price"]
        .pct_change() * 100
    )

    # Calculate 10-event moving average
    df["moving_average"] = (
        df.groupby("symbol")["price"]
        .transform(
            lambda x: x.rolling(window=10).mean()
        )
    )

    # Calculate rolling volatility
    df["volatility"] = (
        df.groupby("symbol")["return_pct"]
        .transform(
            lambda x: x.rolling(window=10).std()
        )
    )

    # Calculate average trading volume
    df["average_volume"] = (
        df.groupby("symbol")["volume"]
        .transform(
            lambda x: x.rolling(window=10).mean()
        )
    )

    # Compare current volume with average volume
    df["volume_ratio"] = (
        df["volume"] / df["average_volume"]
    )

    return df


if __name__ == "__main__":

    print("Loading market data...")

    data = load_market_data()

    print("Calculating market analytics...")

    analytics_data = calculate_analytics(data)

    print("\nAnalytics calculated successfully.")

    print("\nFirst 15 rows:")
    print(
        analytics_data[
            [
                "symbol",
                "event_time",
                "price",
                "volume",
                "return_pct",
                "moving_average",
                "volatility",
                "volume_ratio"
            ]
        ].head(15)
    )

    print("\nNumber of records:", len(analytics_data))

    print("\nColumns created:")
    print(analytics_data.columns.tolist())