import json
import requests
from services.VodaPay.utils.constants import configurations
from services.VodaPay.utils.headerConstructor import construct_headers

def build_url(endpoint):
        return f"{configurations['VODAPAY_BASEURL']}/{endpoint}"

def request (method, endPoint, body):

    url = build_url(endPoint)
    jsonBody = json.dumps(body).replace(" ", "")
    headers = construct_headers(method, endPoint, jsonBody)

    response = requests.post(url=url, data=jsonBody, headers=headers)
    return response