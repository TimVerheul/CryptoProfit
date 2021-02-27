import requests
from dotenv import dotenv_values
# Load variables from .env and return them in a variable
config = dotenv_values(".env")


def main():
    beginamount = config.pop("BEGINAMOUNT")
    print(config)
    print(beginamount)


if __name__ == '__main__':
    main()
