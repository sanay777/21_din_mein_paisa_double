## MONEY MAKER 

# import packages
import csv                        
import talib                       
import numpy  # scientific
import pandas as pd
import websockets
import pprint
import backtrader as bt   # if import works then sqigglies take time to go


# Initialise the client
from binance.client import Client
from binance.enums import *         # 

API_KEY= '7icZ7sVpPV3lYJ93ZuewqdVvB4HRyW9mNLj3nmBogScSxXv1L5MkPCSh2UBskOIb' 
API_SECRET= 'WyLaLbwj4wElUX3zO4F9Q9oepTOpzFUTsseNMykNsQ0REXrJTZB9exy00JEzU34R'

client = Client(API_KEY, API_SECRET, tld='us',)  # tld = top level domain = US (binance.us), testnet = remove the testnet for accesing historical kline data 


## GET HISTORICAL DATA 
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2018", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2018", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2018", "20 Apr, 2022")

#candlesticks = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2018", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2018", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2018", "20 Apr, 2022")

#candlesticks = client.get_historical_klines("SOLUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2018", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("SOLUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2018", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("SOLUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2018", "20 Apr, 2022")

#candlesticks = client.get_historical_klines("APEUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2022", "20 Apr, 2022")
#candlesticks = client.get_historical_klines("APEUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2022", "20 Apr, 2022")
candlesticks = client.get_historical_klines("APEUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Jan, 2022", "20 Apr, 2022")

csvfile = open('APE_USDT 2022 30min.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter = ',')
for candlestick in  candlesticks:
    #candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)
csvfile.close()



# Print(candles)
#csvfile = open('BTC_USDT 1min.csv', 'w', newline='')
#candlestick_writer = csv.writer(csvfile, delimiter = ',')
#candles = client.get_klines(symbol = 'BTCUSDT', interval = Client.KLINE_INTERVAL_15MINUTE)

#for candlestick in candles:
#  print(candlestick)
#  candlestick_writer.writerow(candlestick)
#print(len(candles))



## TALIB



# Backtesting with Backtrader

cerebro = bt.Cerebro()

# BUY SIGNAL LOGIC (RSI < 25)


# SELL SIGNAL LOGIC (RSI > 68)



# RISK MANAGEMENT









# TODO: GG4GKRC
# FIXME: GUGHHRL 

# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan 2021", "31 Dec, 2021")

# for candlestick in candlesticks:
  #  candlestick_writer.writerow(candlestick)
# csvfile.close()

# info = client.get_account()
# print(info)


# GENERAL NOTES, TIPS, 
# Running code - # shift + Enter to run code line by line
# 

#klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")