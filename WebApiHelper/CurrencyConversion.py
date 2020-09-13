from APIGeneralizer.APIHelper import *
from Constants.url_constants import fixer_api_url
from ResponseBuilder.WebApiResponse import response_model
from Logger.logging import logger

def fetch_req_data(request):
    source_currency = request['Source Currency'].upper()
    target_currency = request['Target Currency'].upper()
    amount = request['Amount']
    return source_currency, target_currency, amount

def validate_currency_code(src_curr_code, target_curr_code, curr_list):
    def currency_check(curr_code):
        if curr_code not in curr_list:
            return True
    src_curr_code = currency_check(src_curr_code)
    target_curr_code = currency_check(target_curr_code)
    if src_curr_code:
        logger.error('ERROR: Invalid Source Currency Code')
        return True
    if target_curr_code:
        logger.error('ERROR : Invalid Target Currency Code')
        return True

def currency_conversion(source_currency, target_currency, amount):
    response_content = resp(fixer_api_url)
    currency_rate = response_content['rates']
    base_currency_value = currency_rate['EUR']
    source_currency_rate = currency_rate[source_currency]
    curr_to_eur = base_currency_value/source_currency_rate
    target_curr_rate = currency_rate[target_currency]
    conversion_calc = target_curr_rate * curr_to_eur
    target_amount = float(amount) * float(conversion_calc)
    response = response_model(source_currency, target_currency, amount, target_amount)
    return response



