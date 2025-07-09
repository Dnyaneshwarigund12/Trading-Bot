# Binance Futures Testnet Trading Bot

A simplified Python-based trading bot for placing **market**, **limit**, and **stop-limit** orders on the **Binance Futures Testnet** using the `python-binance` library. This bot supports both buy and sell operations via a command-line interface (CLI) and logs all API activity for easy debugging.

---

## 🔧 Features

- Place market, limit, and stop-limit orders for **BTCUSDT** on Binance Futures Testnet.
- Query real-time **market price** and **account balance (USDT)**.
- Validate user inputs for order quantity and prices.
- Log all API requests, responses, and errors to `trading_bot.log`.
- Robust error handling for stable execution.

---

## 🛠️ Prerequisites

- **Python**: Version 3.6 or higher  
- **Binance Futures Testnet Account**: [Register here](https://testnet.binancefuture.com)  
- **API Credentials**: API Key and Secret with `Enable Reading`, `Enable Trading`, and `Enable Futures` permissions  
- **Test Funds**: Make sure your Testnet account has 3,000–10,000 USDT  

---

## 🚀 Installation

### 1. Set Up Python

Install Python from [python.org](https://www.python.org/)  
Verify the installation:
```bash
python --version

2. (Optional) Create a Virtual Environment
python -m venv myenv

Activate the environment:

Windows:
myenv\Scripts\activate

3. Install Dependencies

pip install python-binance
pip show python-binance 

API Setup
Log in to Binance Futures Testnet.

Go to API Management and generate an HMAC_SHA256 API Key.

Enable:
Reading
Trading
Futures

Save the API Key and Secret Key securely (Secret is shown only once).

💰 Add Test Funds
Check your USDT balance in Testnet Futures Wallet.

If needed, use the Faucet in the Mock Trading section or reset your account.

🧠 Usage
Save the Script
Save the trading_bot.py in your project directory.

Run the Script

cd path/to/TradingBot
python trading_bot.py
Enter API Credentials

Enter Binance Testnet API Key: (myenv) C:\Users\Vitthal Gund\Desktop\Assignment>python trading_bot.py
Enter Binance Testnet API Key: fl0Gz6i4vXsLxw1aIQ689jgrmJdCfVDWOrhGl6iSLfCWNoh33cMjcAdO7zZvQlBe


Simplified Trading Bot (BTCUSDT)
Available commands: market, limit, stop-limit, balance, price, exit

Enter command: cash
Invalid command. Available: market, limit, stop-limit, balance, price, exit

Enter command: balance
Available USDT Balance: 0.0

Command	Description
balance	View current USDT balance
price	Get current BTCUSDT market price
market	Execute market order (buy/sell + quantity)
limit	Place a limit order (side, quantity, price)
stop-limit	Place a stop-limit order (side, qty, stop, limit)
exit	Exit the bot

Example:

Enter command: balance
Available USDT Balance: 10000.0

Enter command: price
Current BTCUSDT Price: 58000.0

Enter command: market
Enter side (buy/sell): buy
Enter quantity (min 0.001): 0.001
Market order executed: 123456789 - FILLED
📜 Logging
All events are logged in trading_bot.log.

View logs:

Windows: type trading_bot.log

Linux/macOS: cat trading_bot.log

Example Log:

2025-07-09 14:29:00,000 - INFO - Trading bot initialized successfully
2025-07-09 14:29:05,000 - INFO - Retrieved balance: 10000.0 USDT
🧩 Troubleshooting
Issue	Solution
Zero Balance	Use the Testnet Faucet or create a new account.
API Errors	Check permissions and remove extra spaces in keys.
Command Errors	Use valid commands. Ensure enough USDT (min 0.001 BTC).
Connection Issues	Check access to testnet site or upgrade the library: pip install python-binance --upgrade

⚠️ Notes
Testnet Only: Do not use live API keys.

Security: Never hardcode API credentials or share them.

Min Order Size: Ensure orders meet the 0.001 BTCUSDT minimum.

Test Funds: Testnet balances may reset periodically.

Docs: Refer to Binance Futures API Documentation.

📄 License
This project is for educational purposes only and is provided as-is. Use at your own risk.
