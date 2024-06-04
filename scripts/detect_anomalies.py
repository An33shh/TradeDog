import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

trade_data = pd.read_csv('../data/preprocessed_trade_data.csv')

def detect_anomalies(data):
    anomalies = []

    # Method 1: Z-score for trade volume
    trade_volume_mean = data['TradeVolume'].mean()
    trade_volume_std = data['TradeVolume'].std()
    data['TradeVolume_ZScore'] = (data['TradeVolume'] - trade_volume_mean) / trade_volume_std
    anomalies.extend(data[data['TradeVolume_ZScore'].abs() > 3].index)

    # Method 2: Z-score for trade price
    trade_price_mean = data['TradePrice'].mean()
    trade_price_std = data['TradePrice'].std()
    data['TradePrice_ZScore'] = (data['TradePrice'] - trade_price_mean) / trade_price_std
    anomalies.extend(data[data['TradePrice_ZScore'].abs() > 3].index)

    # Method 3: Interquartile Range (IQR) for trade volume
    Q1 = data['TradeVolume'].quantile(0.25)
    Q3 = data['TradeVolume'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    anomalies.extend(data[(data['TradeVolume'] < lower_bound) | (data['TradeVolume'] > upper_bound)].index)

    # Method 4: Moving Average for trade volume
    window_size = 10
    data['TradeVolume_MovingAverage'] = data['TradeVolume'].rolling(window=window_size).mean()
    anomalies.extend(data[data['TradeVolume'] > 2 * data['TradeVolume_MovingAverage']].index)

    return list(set(anomalies))

anomaly_indices = detect_anomalies(trade_data)

trade_data['Anomaly'] = 0
trade_data.loc[anomaly_indices, 'Anomaly'] = 1

trade_data.to_csv('../output/anomaly_detected_trade_data.csv', index=False)

print("Anomalies detected and results saved.")
