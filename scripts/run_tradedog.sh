#!/bin/bash

source ../tradedog/bin/activate   # Unix/MacOS
# .\tradedog\Scripts\activate    # Windows

./generate_trade_data.sh

python3 preprocess_trade_data.py

python3 detect_anomalies.py

python3 generate_alerts_reports.py

echo "TradeDog pipeline executed successfully."
