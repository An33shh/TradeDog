import pandas as pd
import numpy as np

# Load preprocessed trade data
trade_data = pd.read_csv('../data/preprocessed_trade_data.csv')

# Implement anomaly detection using z-score
def detect_anomalies_zscore(data, threshold=3):
    data_mean = np.mean(data)
    data_std = np.std(data)
    z_scores = [(x - data_mean) / data_std for x in data]
    return np.where(np.abs(z_scores) > threshold)

# Detect anomalies in TradeVolume
anomalies = detect_anomalies_zscore(trade_data['TradeVolume'])

# Highlight anomalies
trade_data['Anomaly'] = 0
trade_data.loc[anomalies, 'Anomaly'] = 1

# Save the results
trade_data.to_csv('../output/anomaly_detected_trade_data.csv', index=False)

print("Anomalies detected and results saved.")
