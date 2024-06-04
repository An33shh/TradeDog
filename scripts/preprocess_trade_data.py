import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

trade_data = pd.read_csv('../data/trade_data.csv')

trade_data.fillna(method='ffill', inplace=True)

label_encoder = LabelEncoder()
trade_data['ProductType'] = label_encoder.fit_transform(trade_data['ProductType'])

scaler = StandardScaler()
numerical_features = ['TradeVolume', 'TradePrice']
trade_data[numerical_features] = scaler.fit_transform(trade_data[numerical_features])

trade_data.to_csv('../data/preprocessed_trade_data.csv', index=False)

print("Trade data preprocessed and saved.")
