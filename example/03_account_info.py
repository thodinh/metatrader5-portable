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

    # get account info
    account_info = mt5.account_info()
    if account_info is None:
        print("Failed to get account info, error code =", mt5.last_error())
    else:
        print("Account info:")
        print(f" - Login: {account_info.login}")
        print(f" - Server: {account_info.server}")
        print(f" - Balance: {account_info.balance}")
        print(f" - Equity: {account_info.equity}")
        print(f" - Profit: {account_info.profit}")
        print(f" - Margin: {account_info.margin}")
        print(f" - Free Margin: {account_info.margin_free}")
        print(f" - Currency: {account_info.currency}")

    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

if __name__ == "__main__":
    main()
