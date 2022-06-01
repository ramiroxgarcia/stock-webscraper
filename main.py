import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, redirect, url_for, render_template, request


def stock(name1):  # function to scrape price with n
    try:

        url = 'https://finance.yahoo.com/quote/' + name1.upper() + '?p=' + name1.upper() + '&.tsrc=fin-srch'

        r = requests.get(url)  # get request

        soup = bs(r.content, 'html.parser')  # html source code

        stock_price = soup.find('fin-streamer', {'data-test': 'qsp-price'})['value']

        return "The price of " + name1.upper() + " is $" + stock_price
    except:  # if exception return exception message to web page
        return "Not a valid stock symbol"


app = Flask(__name__)


# @app.route("/")
# def home():
#   return "Welcome! please enter a valid stock symbol to the url"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user_symbol = request.form["sym"]  # get key from form
        return redirect(url_for("user", name1=user_symbol))  # redirect to page with symbol
    else:
        return render_template("form.html")


@app.route("/<name1>")  # name as argument
def user(name1):
    return stock(name1)  # call webscraping function and return


if __name__ == "__main__":
    app.run()
