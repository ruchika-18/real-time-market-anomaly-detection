from analytics.data_loader import load_market_data
from analytics.market_analytics import calculate_analytics
from models.anomaly_detector import detect_anomalies
from analytics.database_writer import save_analytics
from analytics.risk_analytics import calculate_risk_metrics
from analytics.risk_database_writer import save_risk_metrics


def main():

    print("REAL-TIME MARKET ANALYTICS PIPELINE")

    print("\n1. Loading market data...")

    market_data = load_market_data()

    print("Records loaded:", len(market_data))

    print("\n2. Calculating market features...")

    analytics_data = calculate_analytics(
        market_data
    )

    print("Feature engineering completed.")

    print("\n3. Running anomaly detection...")

    results = detect_anomalies(
        analytics_data
    )

    anomaly_count = results["is_anomaly"].sum()

    print("Anomaly detection completed.")
    print("Usable records:", len(results))
    print("Anomalies detected:", anomaly_count)

    print("\n4. Saving analytics results to MySQL...")

    rows_saved = save_analytics(results)

    print(
        "Analytics rows saved:",
        rows_saved
    )

    print("\n5. Calculating risk metrics...")

    risk_data = calculate_risk_metrics(
        market_data
    )

    print("Risk calculations completed.")

    print("\n6. Saving risk metrics to MySQL...")

    risk_rows_saved = save_risk_metrics(
        risk_data
    )

    print(
        "Risk rows saved:",
        risk_rows_saved
    )

    print("PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()