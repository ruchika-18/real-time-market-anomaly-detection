import time

from analytics.data_loader import load_market_data
from analytics.market_analytics import calculate_analytics
from models.anomaly_detector import detect_anomalies
from analytics.database_writer import save_analytics

from analytics.risk_analytics import calculate_risk_metrics
from analytics.risk_database_writer import save_risk_metrics


REFRESH_SECONDS = 5


def run_pipeline_once():

    print("\n----------------------------------------")
    print("Starting analytics cycle")
    print("----------------------------------------")

    # -----------------------------------------
    # 1. LOAD MARKET DATA
    # -----------------------------------------

    market_data = load_market_data()

    print(
        "Market records:",
        len(market_data)
    )

    if market_data.empty:

        print(
            "No market data available."
        )

        return

    # -----------------------------------------
    # 2. FEATURE ENGINEERING
    # -----------------------------------------

    analytics_data = calculate_analytics(
        market_data
    )

    print(
        "Feature engineering completed."
    )

    # -----------------------------------------
    # 3. ANOMALY DETECTION
    # -----------------------------------------

    results = detect_anomalies(
        analytics_data
    )

    anomaly_count = int(
        results["is_anomaly"].sum()
    )

    print(
        "Usable records:",
        len(results)
    )

    print(
        "Anomalies detected:",
        anomaly_count
    )

    # -----------------------------------------
    # 4. SAVE ANALYTICS
    # -----------------------------------------

    rows_saved = save_analytics(
        results
    )

    print(
        "Analytics rows saved:",
        rows_saved
    )

    # -----------------------------------------
    # 5. RISK ANALYTICS
    # -----------------------------------------

    risk_data = calculate_risk_metrics(
        market_data
    )

    print(
        "Risk calculations completed."
    )

    # -----------------------------------------
    # 6. SAVE RISK METRICS
    # -----------------------------------------

    risk_rows_saved = save_risk_metrics(
        risk_data
    )

    print(
        "Risk rows saved:",
        risk_rows_saved
    )

    print(
        "Analytics cycle completed."
    )


def main():

    print(
        "========================================"
    )

    print(
        "CONTINUOUS MARKET ANALYTICS PIPELINE"
    )

    print(
        "========================================"
    )

    print(
        f"Pipeline refresh: "
        f"{REFRESH_SECONDS} seconds"
    )

    print(
        "Press Ctrl+C to stop."
    )

    while True:

        try:

            run_pipeline_once()

            print(
                f"\nWaiting {REFRESH_SECONDS} "
                f"seconds before next cycle..."
            )

            time.sleep(
                REFRESH_SECONDS
            )

        except KeyboardInterrupt:

            print(
                "\nContinuous pipeline stopped."
            )

            break

        except Exception as error:

            print(
                "\nPipeline error:",
                error
            )

            print(
                f"Retrying in "
                f"{REFRESH_SECONDS} seconds..."
            )

            time.sleep(
                REFRESH_SECONDS
            )


if __name__ == "__main__":

    main()