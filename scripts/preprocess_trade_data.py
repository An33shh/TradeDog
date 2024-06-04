import pandas as pd

# Load trade data
trade_data = pd.read_csv('../data/trade_data.csv')

# Convert TradeTime to datetime
trade_data['TradeTime'] = pd.to_datetime(trade_data['TradeTime'])

# Sort data by TradeTime
trade_data.sort_values('TradeTime', inplace=True)

# Save the preprocessed data
trade_data.to_csv('preprocessed_trade_data.csv', index=False)

print("Trade data preprocessed and saved to 'preprocessed_trade_data.csv'")
