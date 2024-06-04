#!/bin/bash

NUM_RECORDS=1000
OUTPUT_FILE="../data/trade_data.csv"
START_DATE="2023-01-01"
END_DATE="2023-12-31"

echo "TradeID,ProductType,TradeVolume,TradePrice,TradeTime" > "$OUTPUT_FILE"

START_TIMESTAMP=$(date -jf "%Y-%m-%d" "$START_DATE" +%s)
END_TIMESTAMP=$(date -jf "%Y-%m-%d" "$END_DATE" +%s)
TOTAL_DAYS=$(( (END_TIMESTAMP - START_TIMESTAMP) / 86400 ))

generate_random_date() {
  RANDOM_DAYS=$((RANDOM % (TOTAL_DAYS + 1)))
  date -r $((START_TIMESTAMP + RANDOM_DAYS * 86400)) +%Y-%m-%d
}

for ((i=1; i<=$NUM_RECORDS; i++))
do
  TRADE_ID=$i
  # Generate a random product type
  PRODUCT_TYPE_INDEX=$((RANDOM % 3))
  case $PRODUCT_TYPE_INDEX in
    0) PRODUCT_TYPE="FX" ;;
    1) PRODUCT_TYPE="Equity" ;;
    *) PRODUCT_TYPE="FixedIncome" ;;
  esac
  
  TRADE_VOLUME=$((RANDOM % 1000 + 1))
  
  TRADE_PRICE_MEAN=$((RANDOM % (200 - 50 + 1) + 50))
  TRADE_PRICE_STD=$((RANDOM % (20 - 5 + 1) + 5))
  TRADE_PRICE=$(echo "scale=2; $TRADE_PRICE_MEAN + ($RANDOM % (2 * $TRADE_PRICE_STD + 1)) - $TRADE_PRICE_STD" | bc)

  TRADE_DATE=$(generate_random_date)
  
  TRADE_TIME=$(printf "%02d:%02d:%02d" $((RANDOM % 24)) $((RANDOM % 60)) $((RANDOM % 60)))
  
  echo "$TRADE_ID,$PRODUCT_TYPE,$TRADE_VOLUME,$TRADE_PRICE,$TRADE_DATE $TRADE_TIME" >> "$OUTPUT_FILE"
done

echo "Trade data generated in $OUTPUT_FILE"
