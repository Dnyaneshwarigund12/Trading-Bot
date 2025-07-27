import logging
from binance import Client
from binance.enums import *
import sys
from decimal import Decimal, ROUND_DOWN
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TradingBot:
    def __init__(self, api_key, api_secret, testnet=True):
        """Initialize the trading bot with Binance API credentials"""
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            self.base_url = "https://testnet.binancefuture.com"
            logging.info("Trading bot initialized successfully")
            # Note: Removed change_leverage to avoid attribute error
            # Leverage can be set manually in Testnet dashboard if needed
        except Exception as e:
            logging.error(f"Initialization failed: {str(e)}")
            raise

    def get_balance(self, asset='USDT'):
        """Get available balance for specified asset"""
        try:
            balance = self.client.get_asset_balance(asset=asset)
            available = float(balance['free'])
            logging.info(f"Retrieved balance: {available} {asset}")
            return available
        except Exception as e:
            logging.error(f"Failed to get balance: {str(e)}")
            return 0.0

    def place_market_order(self, symbol, side, quantity):
        """Place a market order"""
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Market order failed: {str(e)}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order"""
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit order failed: {str(e)}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        """Place a stop-limit order"""
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                stopPrice=stop_price,
                price=limit_price
            )
            logging.info(f"Stop-limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Stop-limit order failed: {str(e)}")
            raise

    def get_symbol_price(self, symbol):
        """Get current market price for a symbol"""
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            logging.info(f"Retrieved price for {symbol}: {price}")
            return price
        except Exception as e:
            logging.error(f"Failed to get price for {symbol}: {str(e)}")
            return None

def validate_quantity(quantity, min_qty=0.001):
    """Validate order quantity"""
    try:
        qty = Decimal(str(quantity)).quantize(Decimal('0.001'), rounding=ROUND_DOWN)
        if qty < Decimal(str(min_qty)):
            raise ValueError(f"Quantity must be at least {min_qty}")
        return qty
    except Exception as e:
        logging.error(f"Quantity validation failed: {str(e)}")
        raise

def main():
    # Initialize bot with testnet credentials
    api_key = input("Enter Binance Testnet API Key: ")
    api_secret = input("Enter Binance Testnet API Secret: ")
    
    try:
        bot = TradingBot(api_key, api_secret, testnet=True)
    except Exception as e:
        print(f"Failed to initialize bot: {str(e)}")
        return

    symbol = 'BTCUSDT'  # Default trading pair
    print("\nSimplified Trading Bot (BTCUSDT)")
    print("Available commands: market, limit, stop-limit, balance, price, exit")

    while True:
        try:
            command = input("\nEnter command: ").lower().strip()
            
            if command == 'exit':
                print("Exiting bot...")
                break
                
            elif command == 'balance':
                balance = bot.get_balance()
                print(f"Available USDT Balance: {balance}")

            elif command == 'price':
                price = bot.get_symbol_price(symbol)
                if price:
                    print(f"Current {symbol} Price: {price}")

            elif command in ['market', 'limit', 'stop-limit']:
                side = input("Enter side (buy/sell): ").lower().strip()
                if side not in ['buy', 'sell']:
                    print("Invalid side. Use 'buy' or 'sell'")
                    continue

                quantity = input("Enter quantity (min 0.001): ")
                try:
                    quantity = validate_quantity(quantity)
                except Exception as e:
                    print(f"Invalid quantity: {str(e)}")
                    continue

                side = SIDE_BUY if side == 'buy' else SIDE_SELL

                if command == 'market':
                    order = bot.place_market_order(symbol, side, quantity)
                    print(f"Market order executed: {order['orderId']} - {order['status']}")

                elif command == 'limit':
                    price = input("Enter limit price: ")
                    try:
                        price = float(price)
                        order = bot.place_limit_order(symbol, side, quantity, price)
                        print(f"Limit order placed: {order['orderId']} - {order['status']}")
                    except Exception as e:
                        print(f"Invalid price or order failed: {str(e)}")
                        continue

                elif command == 'stop-limit':
                    stop_price = input("Enter stop price: ")
                    limit_price = input("Enter limit price: ")
                    try:
                        stop_price = float(stop_price)
                        limit_price = float(limit_price)
                        order = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
                        print(f"Stop-limit order placed: {order['orderId']} - {order['status']}")
                    except Exception as e:
                        print(f"Invalid prices or order failed: {str(e)}")
                        continue

            else:
                print("Invalid command. Available: market, limit, stop-limit, balance, price, exit")

        except Exception as e:
            logging.error(f"Command execution failed: {str(e)}")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()