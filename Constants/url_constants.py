"""Fixer API URL"""
from SecureToken.token_reader import decrypt_msg

fixer_api_url = 'http://data.fixer.io/api/latest?access_key='+decrypt_msg+'&format=1'
