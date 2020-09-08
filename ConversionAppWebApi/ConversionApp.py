from flask import Flask, jsonify, request, make_response
from WebApiHelper.CurrencyConversion import currency_conversion
from Constants.WebApiConstants import currency_rates
from ResponseBuilder.WebApiResponse import err_resp_model

app = Flask(__name__)


@app.route('/CurrencyConverter', methods=['POST'])
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


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)

