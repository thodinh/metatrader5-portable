import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import sys
import config

def main():
    # establish connection to the MetaTrader 5 terminal
    if not mt5.initialize(
        path=config.MT5_PATH,
        portable=True
    ):
        print("initialize() failed, error code =", mt5.last_error())
        sys.exit(1)
        
    print("initialize() success!")

    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    
    # Set the timezone to UTC for the request
    # NOTE: MT5 expects dates in the broker's timezone, but for testing we can fetch the last N bars
    
    print(f"Fetching 10 bars of historical data for {symbol} on H1 timeframe...")
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 10)
    
    if rates is None or len(rates) == 0:
        print(f"Failed to get rates for {symbol}, error code =", mt5.last_error())
    else:
        # Create a Pandas DataFrame out of the obtained data
        rates_frame = pd.DataFrame(rates)
        
        # Convert time in seconds into the datetime format
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        
        # Display the data
        print("\nRates Data:")
        print(rates_frame[['time', 'open', 'high', 'low', 'close', 'tick_volume']])

    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

if __name__ == "__main__":
    main()
