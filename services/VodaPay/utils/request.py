import json
import requests

from config import Configuration
from services.VodaPay.utils.headerConstructor import construct_headers

def build_url(endpoint):
    config = Configuration._instance
    VODAPAY_BASEURL = config.get_config()["VODAPAY_BASEURL"]

    return f"{VODAPAY_BASEURL}/{endpoint}"

def request (method, endPoint, body):

    url = build_url(endPoint)
    jsonBody = json.dumps(body).replace(" ", "")
    headers = construct_headers(method, endPoint, jsonBody)

    response = requests.post(url=url, data=jsonBody, headers=headers)
    return response