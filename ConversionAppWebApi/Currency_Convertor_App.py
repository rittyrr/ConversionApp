from flask import Blueprint, Flask, jsonify, request, make_response
from WebApiHelper.CurrencyConversion import currency_conversion
from Constants.WebApiConstants import currency_rates
from ResponseBuilder.WebApiResponse import err_resp_model

currency_conversion_blueprint = Blueprint('currency_conversion_blueprint', __name__)
"""Blueprint arg1 - blueprint' name, arg2 - __name__ to locate blueprint resources"""

@currency_conversion_blueprint.route('/CurrencyConverter_api', methods=['POST'])
def currency_converter():
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        client_request = request.json
        source_currency = client_request['Source Currency'].upper()
        target_currency = client_request['Target Currency'].upper()
        amount = client_request['Amount']
        if source_currency not in currency_rates:
            return jsonify(err_resp_model())
        else:
            client_response = currency_conversion(source_currency, target_currency, amount)
            return jsonify(client_response)


