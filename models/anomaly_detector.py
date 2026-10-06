import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df):

    data = df.copy()

    features = [
        "return_pct",
        "volatility",
        "volume_ratio"
    ]

    # Remove rows where required features are unavailable
    model_data = data.dropna(
        subset=features
    ).copy()

    # Replace infinite values
    model_data[features] = model_data[features].replace(
        [float("inf"), float("-inf")],
        0
    )

    model = IsolationForest(
        n_estimators=150,
        contamination=0.05,
        random_state=42
    )

    predictions = model.fit_predict(
        model_data[features]
    )

    scores = model.decision_function(
        model_data[features]
    )

    model_data["anomaly_score"] = -scores
    model_data["is_anomaly"] = predictions == -1

    # Explain detected anomalies
    def explain_anomaly(row):

        reasons = []

        if abs(row["return_pct"]) >= 3:
            reasons.append("large price movement")

        if row["volume_ratio"] >= 2:
            reasons.append("unusually high trading volume")

        if row["volatility"] >= 1:
            reasons.append("high price volatility")

        if not reasons:
            reasons.append(
                "unusual combination of market indicators"
            )

        return " + ".join(reasons)

    model_data["anomaly_reason"] = ""

    anomaly_mask = model_data["is_anomaly"]

    model_data.loc[
        anomaly_mask,
        "anomaly_reason"
    ] = model_data.loc[
        anomaly_mask
    ].apply(
        explain_anomaly,
        axis=1
    )

    return model_data


if __name__ == "__main__":

    from analytics.data_loader import load_market_data
    from analytics.market_analytics import calculate_analytics

    market_data = load_market_data()

    analytics_data = calculate_analytics(
        market_data
    )

    results = detect_anomalies(
        analytics_data
    )

    anomalies = results[
        results["is_anomaly"]
    ]

    print("\nDetected anomalies:")
    print(
        anomalies[
            [
                "symbol",
                "event_time",
                "price",
                "return_pct",
                "volatility",
                "volume_ratio",
                "anomaly_reason"
            ]
        ].to_string(index=False)
    )