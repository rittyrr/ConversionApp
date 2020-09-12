import requests as re

def resp(url):
    response = re.get(url)
    response_content = response.json()
    return response_content

