from flask import render_template, request, redirect, session, flash
from flask_app import app
from yahoo_fin import stock_info




def in_out(ticker):
    from yahoo_fin import stock_info
    stockPrice = stock_info.get_live_price("AMZN")
    return stockPrice

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stock_info", methods=['POST'])
def stock_info():
    data = request.form
    data = data["ticker"]
    results = in_out(request.form)
    return render_template("index.html", results = results)


