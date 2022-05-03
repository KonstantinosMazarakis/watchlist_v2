from pickle import GLOBAL
from sqlite3 import Time
from yahoo_fin import stock_info
from threading import Timer



def  runNonStop(answer_Ticker):
    print(stock_info.get_live_price(answer_Ticker))
    price = stock_info.get_live_price(answer_Ticker)
    if price_bought == price:
        print("price you buy:")
        print(price_bought)
        print("price now:")
        print(price)

    Timer(5.0,runNonStop,[answer_Ticker]).start()


def ask():
    answer_Ticker = input("Please enter Ticker: ")
    global price_bought
    price_bought = stock_info.get_live_price(answer_Ticker)
    runNonStop(answer_Ticker)


ask()