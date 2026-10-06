# Real-Time Market Anomaly & Risk Analytics System

## Overview

This project is a Python-based market monitoring system that detects unusual
price and trading-volume activity and calculates basic risk metrics.

The system uses simulated market events for multiple stocks and processes
the data using Python, Pandas, SQL and machine learning.

## Features

- Continuous market data generation
- MySQL database for storing market events
- Market return calculation
- Moving average calculation
- Rolling volatility calculation
- Trading volume analysis
- Volume ratio calculation
- Machine learning based anomaly detection
- Isolation Forest model
- Automatic anomaly explanation
- Risk analytics
- Value at Risk (VaR)
- Maximum drawdown
- Trading volume monitoring
- Matplotlib visualization dashboard

## Technology Used

- Python
- MySQL
- SQL
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Isolation Forest
- Git

## System Flow

Market Data Generator
        |
        v
MySQL Database
        |
        v
Pandas Data Processing
        |
        v
Feature Engineering
        |
        v
Isolation Forest
        |
        v
Anomaly Detection
        |
        v
Risk Analytics
        |
        v
Visualization Dashboard

## Machine Learning

Isolation Forest is used to identify unusual observations based on:

- Price returns
- Rolling volatility
- Trading volume ratio

The system labels unusual market behavior as an anomaly.

## Risk Metrics

The system calculates:

- Total Return
- Average Return
- Volatility
- 95% Value at Risk
- Maximum Drawdown

## Example Anomaly

An anomaly can be triggered when the system observes:

- Large price movement
- Unusually high trading volume
- High price volatility

The system also provides an explanation for detected anomalies.

## Project Structure

RealTimeMarketAnalytics/

    api/

    analytics/

    dashboard/

    database/

    data/

    models/

    risk_metrics.csv

    market_anomaly_dashboard.png

    run_pipeline.py

    README.md

## How to Run

Install the required packages:

    pip install pandas numpy matplotlib scikit-learn mysql-connector-python

Configure the MySQL database connection in:

    database/connection.py

Start the market data generator.

Then run the analysis pipeline.

Finally run:

    dashboard/final_dashboard.py

to generate the visualization dashboard.

## Purpose

The project demonstrates how market data can be collected, processed,
analysed and monitored using Python, SQL, machine learning and data
visualization.