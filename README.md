# Binance Futures Testnet Trading Bot

## Installation

pip install -r requirements.txt

## Configure

Create .env

API_KEY=...

API_SECRET=...

## Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

## Assumptions

Uses Binance Futures Testnet
Requires testnet balance
Python 3.10+