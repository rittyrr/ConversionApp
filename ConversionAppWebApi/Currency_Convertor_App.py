from flask import Blueprint, jsonify, request, make_response
from WebApiHelper.CurrencyConversion import currency_conversion, fetch_req_data, validate_currency_code
from ResponseBuilder.WebApiResponse import err_resp_model
from Constants.url_constants import fixer_api_url
from APIGeneralizer.APIHelper import *
from Logger.logging import logger

currency_conversion_blueprint = Blueprint('currency_conversion_blueprint', __name__)
"""Blueprint arg1 - blueprint' name, arg2 - __name__ to locate blueprint resources"""

def before_request():
    global currency_list
    fixer_api_response = resp(fixer_api_url)
    rates = fixer_api_response['rates']
    currency_list = list(rates.keys())


@currency_conversion_blueprint.route('/CurrencyConverter/', methods=['POST'])
def currency_converter():
    try:
        if request.method == 'POST':
            client_request = request.json
            source_currency, target_currency, amount = fetch_req_data(client_request)
            currency_check = validate_currency_code(source_currency, target_currency, currency_list)
            if currency_check:
                return jsonify(err_resp_model())
            else:
                client_response = currency_conversion(source_currency, target_currency, amount)
                logger.info('SUCCESS: Currency Converted Successfully')
                return jsonify(client_response)
    except Exception as e:
        logger.error('ERROR: ' + e)


currency_conversion_blueprint.before_request(before_request)






