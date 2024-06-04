import pandas as pd

anomaly_data = pd.read_csv('../output/anomaly_detected_trade_data.csv')

def generate_alerts(data):
    alerts = []

    for index, row in data.iterrows():
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

alerts = generate_alerts(anomaly_data)

alerts.to_csv('../output/alerts.csv', index=False)

print(f"{len(alerts)} anomalies detected and alerts saved.")
