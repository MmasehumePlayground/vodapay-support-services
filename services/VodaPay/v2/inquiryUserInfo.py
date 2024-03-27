import requests

from config import Configuration
from services.VodaPay.utils.request import request

def inquiryUserInfo (accessCode) :

    if not isinstance(accessCode, Exception) and (accessCode.get("result", {}).get("resultStatus").lower() != 'f'):

        code = accessCode['accessToken']
        config = Configuration._instance
        VODAPAY_CLIENT_ID = config.get_config()["VODAPAY_CLIENT_ID"]

        userInfoBody = {
            "authClientId": VODAPAY_CLIENT_ID,
            "accessToken": code
        }
        
        try:
            inquiryUserInfoRequest = request('POST', "v2/customers/user/inquiryUserInfo", userInfoBody)
            inquiryUserInfoRequest.raise_for_status()
            inquiryUserInfoResponse = inquiryUserInfoRequest.json()
            
            return inquiryUserInfoResponse
        
        except requests.exceptions.HTTPError as http_err:
            return http_err
        except requests.exceptions.RequestException as req_err:
            return req_err
    
    else:
        return accessCode