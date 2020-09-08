import requests as re
from Constants.url_constants import fixer_api_url
from ResponseBuilder.WebApiResponse import response_model

def currency_conversion(source_currency, target_currency, amount):
    resp = re.get(fixer_api_url)
    response_content = resp.json()
    currency_rate = response_content['rates']
    base_currency_value = currency_rate['EUR']
    source_currency_rate = currency_rate[source_currency]
    curr_to_eur = base_currency_value/source_currency_rate
    target_curr_rate = currency_rate[target_currency]
    conversion_calc = target_curr_rate * curr_to_eur
    target_amount = float(amount) * float(conversion_calc)
    response = response_model(source_currency, target_currency, amount, target_amount)
    return response



