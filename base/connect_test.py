import MetaTrader5 as mt5
import sys
import time

def main():
    print("Initializing MT5...")
    path = "C:\\Metatrader-5\\terminal64.exe"
    
    success = False
    for i in range(3):
        print(f"Attempt {i+1}...")
        success = mt5.initialize(
            path=path,
            portable=True,
            login=10011910442,
            password="2tS_TpRm",
            server="MetaQuotes-Demo"
        )
        if success:
            break
        print("Error:", mt5.last_error())
        time.sleep(5)
        
    if not success:
        print("initialize() failed.")
        mt5.shutdown()
        sys.exit(1)
        
    print("MT5 initialized successfully!")
    print(mt5.terminal_info())
    mt5.shutdown()
    print("Test passed.")

if __name__ == "__main__":
    main()
