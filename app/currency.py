import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CURRENCY_API_KEY")
print('API_KEY: ', API_KEY)
ENDPOINT = f'https://api.currencyfreaks.com/v2.0/rates/latest?apikey={API_KEY}'


def get_currency(from_currency):
    response = requests.get(ENDPOINT)
    data = response.json()
    rates = data.get("rates", {})
    from_rate = rates.get(from_currency.upper())

    if from_rate is None:
        return {"error": f"Currency '{from_currency}' not found"}

    return float(from_rate)
