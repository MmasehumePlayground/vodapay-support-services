import requests

from services.VodaPay.utils.request import request

def inquiryPayment(paymentId):

    body = {
        "paymentId": f"{paymentId}",
        "extraParams":{
        },
        "extendInfo":"automation test cases"
    }

    try :
        paymentInfoResquest = request('POST', "v2/payments/inquiryPayment", body)
        paymentInfoResquest.raise_for_status()
        paymentInfoResponse = paymentInfoResquest.json()

        return paymentInfoResponse
    except requests.exceptions.HTTPError as http_err:
        return http_err
    
    except requests.exceptions.RequestException as req_err:
        return req_err