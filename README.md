# 💹 Real-Time Crypto Trade Simulator (Tkinter GUI)

A **desktop crypto trade simulator** built using **Python** and **Tkinter**. It allows users to simulate real-time cryptocurrency trading with a simple graphical interface. No real funds are involved — this is a safe environment to practice trading strategies.

## 🧰 Built With

- **Python 3**
- **Tkinter** – for GUI
- **Threading** – for background price updates
- **(Optional)** `websocket-client` or `requests` – for live price data
- **SQLite** – to store trades (optional)

## ✨ Features

- 🔴 Live price updates (mocked or real)
- 🧾 Place "Buy" and "Sell" orders
- 💼 Track your virtual wallet balance and holdings
- 📈 Real-time price display and history log
- 🗃️ View trade history in the GUI

## 📸 GUI Preview

![image](https://github.com/user-attachments/assets/0b653d24-c644-48f1-9831-37c6d7d4148e)


## 🔧 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/crypto-tkinter-simulator.git
cd crypto-tkinter-simulator


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


pip install -r requirements.txt


python app.py



⚙️ How It Works
The GUI is rendered using Tkinter widgets.

The current crypto price is updated every few seconds (either mocked or via live WebSocket).

When a trade is placed, the simulator calculates:

Entry price

Quantity

Fee (flat or %)

Updates wallet balance and logs trade

🧪 Simulated Trade Example
Action	Symbol	Quantity	Price	PnL
BUY	BTC	0.005	62,300.12	N/A
SELL	BTC	0.005	62,700.00	+19.40

📌 Optional Enhancements
⏱️ Historical chart using matplotlib

📦 SQLite trade storage and export

📊 Strategy backtesting

👤 User login system

📄 License
MIT License


