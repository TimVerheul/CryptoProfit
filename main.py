import requests
from dotenv import dotenv_values
# Load variables from .env and return them in a variable
config = dotenv_values(".env")
CURRENT_PRICE = "https://www.binance.com/api/v3/ticker/price"


def main():
    beginamount = config.pop("BEGINAMOUNT")
    r = requests.get(CURRENT_PRICE)
    symbol_prices = r.json()
    euro = 0  # note that only Euro will work, make sure your only FIAT currency is Euro.
    crypto_price = 0

    print(symbol_prices)
    for symbol in config:
        if any(symbol == sublist['symbol'] for sublist in symbol_prices):
            for price in symbol_prices:
                if price['symbol'] == symbol:
                    crypto_price += float(price['price']) * float(config[symbol])
        else:
            euro += float(config[symbol])

    total_price = crypto_price + euro
    total_profit = total_price - float(beginamount)
    print(total_price)
    print(total_profit)
    print(config)


if __name__ == '__main__':
    main()
