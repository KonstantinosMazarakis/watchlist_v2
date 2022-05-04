from pickle import GLOBAL
from sqlite3 import Time
from yahoo_fin import stock_info
from threading import Timer



def  runNonStop(answer_Ticker,price_bought,quantity):
    print(stock_info.get_live_price(answer_Ticker))
    price = stock_info.get_live_price(answer_Ticker)
    if  price >= price_bought + (price_bought * 0.2):
        print(f"Current Price: {price}")
        print(f"Bought price: {price_bought}")
        print("you made 20% of your invesment")
        print(f"You are making {(price * quantity) - (price_bought * quantity)}")
        print("-----------------------------------------")
    elif price <= price_bought - (price_bought * 0.1):
        print(f"Current Price: {price}")
        print(f"Bought price: {price_bought}")
        print("you are losing more than 10%")
        print(f"You are making {(price * quantity) - (price_bought * quantity)}")
        print("-----------------------------------------")
    elif price > price_bought:
        print(f"Current Price: {price}")
        print(f"Bought price: {price_bought}")
        print(f"You are making {(price * quantity) - (price_bought * quantity)}")
        print("-----------------------------------------")
    elif price < price_bought:
        print(f"Current Price: {price}")
        print(f"Bought price: {price_bought}")
        print(f"You are losing {(price * quantity) - (price_bought * quantity)}")
        print("-----------------------------------------")


    Timer(5.0,runNonStop,[answer_Ticker,price_bought,quantity]).start()


def ask():
    answer_Ticker = input("Please enter Ticker: ")
    price_bought = float(input("Please enter Price bought: "))
    quantity = int(input("Please enter quantity: "))
    runNonStop(answer_Ticker,price_bought,quantity)


ask()