import MetaTrader5 as mt5
import sys
import config

def main():
    # establish connection to the MetaTrader 5 terminal
    if not mt5.initialize(
        path=config.MT5_PATH,
        portable=True,
        login=config.MT5_LOGIN,
        password=config.MT5_PASSWORD,
        server=config.MT5_SERVER
    ):
        print("initialize() failed, error code =", mt5.last_error())
        sys.exit(1)
        
    print("initialize() success!")

    # get all symbols
    symbols = mt5.symbols_get()
    print("Total symbols:", len(symbols))

    # filter for symbols containing 'EUR' or 'GBP'
    eur_gbp_symbols = [s for s in symbols if "EUR" in s.name or "GBP" in s.name]
    
    print("\nSome EUR/GBP symbols found:")
    # print the first 10 for demonstration
    for sym in eur_gbp_symbols[:10]:
        print(f" - {sym.name}: {sym.description}")
        
    # specifically check EURUSD
    symbol = "EURUSD"
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"\n{symbol} not found, can not check info")
    else:
        print(f"\n{symbol} Info:")
        print(f" - Spread: {symbol_info.spread}")
        print(f" - Digits: {symbol_info.digits}")
        print(f" - Ask: {symbol_info.ask}")
        print(f" - Bid: {symbol_info.bid}")

    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

if __name__ == "__main__":
    main()
