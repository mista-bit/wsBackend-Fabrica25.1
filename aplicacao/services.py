import requests
from django.conf import settings

FIXER_API_URL = 'http://data.fixer.io/api/latest'
FIXER_API_KEY = settings.FIXER_API_KEY

def get_exchange_rate():
    response = requests.get(FIXER_API_URL, params={
        'access_key': FIXER_API_KEY,
    })
    data = response.json()

    if response.status_code == 200 and data.get("success", False):
        return data.get("rates", {})
    return None

def get_conversion_rate(base_currency, target_currency):
    rates = get_exchange_rate()
    if not rates:
        return None
    
    if base_currency == "EUR":
        return rates.get(target_currency)
    
    rate_base = rates.get(base_currency)
    rate_target = rates.get(target_currency)
    if rate_base and rate_target:
        return rate_target / rate_base
    return None

def convert_currency(amount, base_currency, target_currency):
    conversion_rate = get_conversion_rate(base_currency, target_currency)
    if conversion_rate:
        return round(amount * conversion_rate, 2)
    return None
