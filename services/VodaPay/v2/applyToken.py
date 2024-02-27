import requests

from services.VodaPay.utils.request import request

def applyToken (authCode):
        applyTokenBody = {
                "grantType":"AUTHORIZATION_CODE",
                "authCode": authCode
            }
        
        try:
            applyTokenRequest = request('POST', "v2/authorizations/applyToken", applyTokenBody)
            applyTokenRequest.raise_for_status()
            applyTokenResponse = applyTokenRequest.json()

            return applyTokenResponse
        
        except requests.exceptions.HTTPError as http_err:
            return http_err
        
        except requests.exceptions.RequestException as req_err:
            return req_err