import requests
import matplotlib.pyplot as plt
from dotenv import dotenv_values
# Load variables from .env and return them in a variable
config = dotenv_values(".env")
CURRENT_PRICE = "https://www.binance.com/api/v3/ticker/price"


def gain(current_price, x):
    return current_price / 100 * (x + 100)


def main():
    beginamount = config.pop("BEGINAMOUNT")
    raising = config.pop("RAISING")
    r = requests.get(CURRENT_PRICE)
    symbol_prices = r.json()
    # Make sure your only FIAT currency is Euro.
    euro = raising_price = crypto_price = raising_crypto = current_price = 0

    print(symbol_prices)
    for symbol in config:
        if any(symbol == sublist['symbol'] for sublist in symbol_prices):
            for price in symbol_prices:

                if raising not in config:
                    exit('The crypto that you want to raise is not in your wallet. Check the .env file.')
                else:
                    if price['symbol'] == symbol and price['symbol'] != raising:
                        crypto_price += float(price['price']) * float(config[symbol])
                    if price['symbol'] == raising:
                        raising_crypto = float(config[raising])
                        current_price = float(price['price'])
                        raising_price = raising_crypto * current_price

        else:
            euro += float(config[symbol])

    percentage = [i for i in range(1, 1001)]
    percentage_price = [gain(current_price, x) for x in percentage]
    # percentage_price = [current_price / 100 * x for x in range(100, 1101)]
    percentage_raised_price = [raising_crypto * x for x in percentage_price]

    print(percentage_price)
    print(percentage_raised_price)
    plt.plot(percentage, percentage_raised_price)
    plt.show()
    # print(percentage_price)
    print(crypto_price)
    total_price = crypto_price + raising_price + euro
    total_profit = total_price - float(beginamount)

    print(current_price)
    # print(total_price)
    print(total_profit)
    print(raising_crypto)


if __name__ == '__main__':
    main()
