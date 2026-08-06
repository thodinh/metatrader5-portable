import MetaTrader5 as mt5
import sys
import config

def main():
    print("MetaTrader5 package author: ", mt5.__author__)
    print("MetaTrader5 package version: ", mt5.__version__)

    # establish connection to the MetaTrader 5 terminal
    if not mt5.initialize(
        path=config.MT5_PATH,
        portable=True
    ):
        print("initialize() failed, error code =", mt5.last_error())
        sys.exit(1)
        
    print("initialize() success!")

    # display data on the MetaTrader 5 terminal
    terminal_info = mt5.terminal_info()
    if terminal_info is not None:
        print(f"Terminal Info: {terminal_info}")
    
    # display data on MetaTrader 5 version
    print("MT5 Version:", mt5.version())

    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

if __name__ == "__main__":
    main()
