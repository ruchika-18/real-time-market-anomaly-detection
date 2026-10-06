import pandas as pd
import numpy as np

from analytics.data_loader import load_market_data
from analytics.market_analytics import calculate_analytics


def calculate_risk_metrics(df):

    results = []

    for symbol in df["symbol"].unique():

        stock = df[df["symbol"] == symbol].copy()

        stock = stock.sort_values("event_time")

        returns = stock["return_pct"].dropna()

        if len(returns) == 0:
            continue

        total_return = ((stock["price"].iloc[-1] /
                         stock["price"].iloc[0]) - 1) * 100

        volatility = returns.std()

        average_return = returns.mean()

        max_drawdown = calculate_max_drawdown(stock["price"])

        var_95 = np.percentile(returns, 5)

        results.append({
            "symbol": symbol,
            "total_return_pct": total_return,
            "average_return_pct": average_return,
            "volatility": volatility,
            "VaR_95": var_95,
            "max_drawdown_pct": max_drawdown
        })

    return pd.DataFrame(results)


def calculate_max_drawdown(prices):

    cumulative_max = prices.cummax()

    drawdown = (prices - cumulative_max) / cumulative_max

    return drawdown.min() * 100


def main():

    print("\nLoading market data...")

    df = load_market_data()

    df = calculate_analytics(df)

    risk = calculate_risk_metrics(df)

    
    print("RISK ANALYTICS")

    print(risk.to_string(index=False))

    risk.to_csv("risk_metrics.csv", index=False)

    print("\nRisk metrics saved to risk_metrics.csv")


if __name__ == "__main__":
    main()