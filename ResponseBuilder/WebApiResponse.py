import json

def response_model(source_currency, target_currency, amount, target_amount):
    resp = {'Source Currency': source_currency, 'Target Currency': target_currency,
            'Amount': amount, 'Target Amount': target_amount}
    return resp

def err_resp_model():
    resp = {"success": False,
            "error": {
                "code": 404,
                "info": "Requested resource does not exist"
            }
            }
    return resp
