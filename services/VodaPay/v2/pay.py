import requests
from datetime import datetime, timedelta
from services.VodaPay.utils.request import request

def payment (paymentRequestId, paymentNotifyUrl, paymentExpiryTime, amountInCents, goodsId, buyerId, goodsName = "mobile1", orderDescription = "title"):

    now = datetime.now() + timedelta(hours=paymentExpiryTime)
    expiryTime = now.astimezone().isoformat()

    body = {
            "productCode":"CASHIER_PAYMENT",
            "salesCode":"51051000101000000011",
            "paymentNotifyUrl": f"{paymentNotifyUrl}",
            "paymentRequestId": f"{paymentRequestId}",
            "paymentRedirectUrl":"http://mock.vision.vodacom.aws.corp/mock/api/v1/payments/notifyPayment.htm",
            "paymentExpiryTime": f"{expiryTime}",
            "paymentAmount":{
                "currency":"ZAR",
                "value": f"{amountInCents}"
            },
            "order":{
                "goods":{
                    "referenceGoodsId": f"{goodsId}",
                    "goodsUnitAmount":{
                        "currency":"ZAR",
                        "value": f"{amountInCents}"
                    },
                    "goodsName": f"{goodsName}"
                },
                "env":{
                    "terminalType":"MINI_APP"
                },
                "orderDescription": f"{orderDescription}",
                "buyer":{
                    "referenceBuyerId": f"{buyerId}"
                }
            },
            "extendInfo":"{}"
        }

    try :
        paymentRequest = request('POST', "v2/payments/pay", body)
        paymentRequest.raise_for_status()
        paymentResponse = paymentRequest.json()

        return paymentResponse
    
    except requests.exceptions.HTTPError as http_err:
        return http_err
    
    except requests.exceptions.RequestException as req_err:
        return req_err