from flask import Flask
from ConversionAppWebApi.Currency_Convertor_App import currency_conversion_blueprint

app = Flask(__name__)
app.register_blueprint(currency_conversion_blueprint)
app.run()
