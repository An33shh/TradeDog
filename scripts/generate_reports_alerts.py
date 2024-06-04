import pandas as pd

# Load anomaly detected trade data
anomaly_data = pd.read_csv('../output/anomaly_detected_trade_data.csv')

# Define function to generate alerts
def generate_alerts(data):
    alerts = []

    for index, row in data.iterrows():
        # Check if trade volume is significantly higher than usual
        if row['Anomaly'] == 1 and row['TradeVolume'] > 2 * data['TradeVolume'].mean():
            alert = {
                'TradeID': row['TradeID'],
                'ProductType': row['ProductType'],
                'TradeVolume': row['TradeVolume'],
                'TradePrice': row['TradePrice'],
                'TradeTime': row['TradeTime'],
                'AlertType': 'HighVolume'
            }
            alerts.append(alert)

        # Check if trade price is significantly different from the average price
        elif row['Anomaly'] == 1 and abs(row['TradePrice'] - data['TradePrice'].mean()) > 2 * data['TradePrice'].std():
            alert = {
                'TradeID': row['TradeID'],
                'ProductType': row['ProductType'],
                'TradeVolume': row['TradeVolume'],
                'TradePrice': row['TradePrice'],
                'TradeTime': row['TradeTime'],
                'AlertType': 'PriceChange'
            }
            alerts.append(alert)

    return pd.DataFrame(alerts)

# Generate alerts
alerts = generate_alerts(anomaly_data)

# Save alerts
alerts.to_csv('../output/alerts.csv', index=False)

print(f"{len(alerts)} anomalies detected and alerts saved.")
