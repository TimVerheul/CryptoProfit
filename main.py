import matplotlib.pyplot as plt
import numpy as np
import requests
from dotenv import dotenv_values

# Load variables from .env and return them in a variable
config = dotenv_values(".env")
CURRENT_PRICE = "https://www.binance.com/api/v3/ticker/price"  # You should not change this.
# The max percentage of the potential profit
LIMIT = 500


def gain(current_price, x):
    return current_price / 100 * (x + 100)


def main():
    beginamount = config.pop("BEGINAMOUNT")
    raising = config.pop("RAISING")
    r = requests.get(CURRENT_PRICE)
    symbol_prices = r.json()
    # Make sure your only FIAT currency is Euro.
    euro = raising_price = crypto_price = raising_crypto = current_price = 0

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

    # Calculations
    percentage = [i for i in range(1, LIMIT + 1)]
    percentage_price = [gain(current_price, x) for x in percentage]
    percentage_raised_price = [raising_crypto * x for x in percentage_price]
    percentage_total_price = [(raising_crypto * x) + crypto_price + euro for x in percentage_price]
    total_price = crypto_price + raising_price + euro
    total_profit = total_price - float(beginamount)

    # Set title and labels
    plt.title(f"CryptoProfit €{round(total_profit, 2)} (€{round(total_price, 2)} - €{round(float(beginamount), 2)})")
    plt.xlabel("Profit in €")
    plt.ylabel("Raised percentage in %")
    # Plot lines
    plt.plot(percentage_raised_price, percentage, label=f"{raising} profit")
    plt.plot(percentage_total_price, percentage, label="Total profit")
    # Make ticks smaller
    plt.xticks(np.arange(0, max(percentage_raised_price) + 1, 200))
    plt.yticks(np.arange(0, max(percentage), 100))
    # Show legend and chart
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
