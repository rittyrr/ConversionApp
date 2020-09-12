from flask import Blueprint, jsonify, request, make_response
from WebApiHelper.CurrencyConversion import currency_conversion
from ResponseBuilder.WebApiResponse import err_resp_model
from Constants.url_constants import fixer_api_url
from APIGeneralizer.APIHelper import *

currency_conversion_blueprint = Blueprint('currency_conversion_blueprint', __name__)
"""Blueprint arg1 - blueprint' name, arg2 - __name__ to locate blueprint resources"""


def before_request():
    global currency_list
    fixer_api_response = resp(fixer_api_url)
    rates = fixer_api_response['rates']
    currency_list = list(rates.keys())


@currency_conversion_blueprint.route('/CurrencyConverter/', methods=['POST'])
def currency_converter():
    if request.method == 'GET' or request.method == 'PUT' or request.method == 'DELETE':
        return make_response('failure')
    if request.method == 'POST':
        client_request = request.json
        source_currency = client_request['Source Currency'].upper()
        target_currency = client_request['Target Currency'].upper()
        amount = client_request['Amount']
        if source_currency not in currency_list:
            return jsonify(err_resp_model())
        else:
            client_response = currency_conversion(source_currency, target_currency, amount)
            return jsonify(client_response)


currency_conversion_blueprint.before_request(before_request)






