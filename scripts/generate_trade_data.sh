#!/bin/bash

# Number of trade records to generate
NUM_RECORDS=1000

# Output file
OUTPUT_FILE="trade_data.csv"

# Header
echo "TradeID,ProductType,TradeVolume,TradePrice,TradeTime" > $OUTPUT_FILE

# Generate trade data
for i in $(seq 1 $NUM_RECORDS)
do
  TRADE_ID=$i
  PRODUCT_TYPE=$(shuf -n 1 -e FX Equity FixedIncome)
  TRADE_VOLUME=$((RANDOM % 1000 + 1))
  TRADE_PRICE=$(echo "scale=2; $RANDOM % 1000 / 10" | bc)
  TRADE_TIME=$(date -d "$((RANDOM % 365)) days ago" +"%Y-%m-%d %H:%M:%S")

  echo "$TRADE_ID,$PRODUCT_TYPE,$TRADE_VOLUME,$TRADE_PRICE,$TRADE_TIME" >> $OUTPUT_FILE
done

echo "Trade data generated in $OUTPUT_FILE"
