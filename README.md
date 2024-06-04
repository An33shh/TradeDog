# TradeDog

TradeDog is a Python and Bash project that simulates a trade data management system for investment banking products such as FX, Equity, and Fixed Income.

## Description

TradeDog provides a solution for managing trade data in investment banking, with features for generating synthetic trade data, preprocessing, and analyzing trade data, and detecting anomalies. It aims to simulate the trade cycle and provide insights into trade activities.

## Tech Stack

- Python
- Bash

## Setup

To set up the TradeDog project, follow these steps:

1. **Clone the Repository**: Clone the TradeDog repository to your local machine.

2. **Set Up Environment**: Create a Python virtual environment and activate it.

   ```bash
   python3 -m venv tradedog_env
   source tradedog_env/bin/activate
   ```

3. **Install Dependencies**: Install the required Python dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

4. **Generate Trade Data**: Run the `generate_trade_data.sh` script to generate synthetic trade data.

   ```bash
   ./generate_trade_data.sh
   ```

5. **Preprocess Data**: Execute the `preprocess_trade_data.py` script to preprocess the generated trade data.

   ```bash
   python preprocess_trade_data.py
   ```

6. **Detect Anomalies**: Run the `detect_anomalies.py` script to detect anomalies in the preprocessed trade data.

   ```bash
   python detect_anomalies.py
   ```

7. **Generate Alerts and Reports**: Execute the `generate_alerts_reports.py` script to generate alerts and reports based on detected anomalies.

   ```bash
   python generate_alerts_reports.py
   ```

8. **Monitor in Real-Time**: Use the provided API to monitor trade data in real-time and receive alerts for any suspicious activities.

## License

TradeDog is licensed under the [MIT License](LICENSE).
