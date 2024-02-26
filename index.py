
from services.VodaPay.v2.applyToken import applyToken
from services.VodaPay.v2.inquiryUserInfo import inquiryUserInfo
from services.VodaPay.utils.error import errorHandling
from services.VodaPay.utils.request import request

def userInfo(authCode):
        applyTokenCode = applyToken(authCode)
        info = inquiryUserInfo(applyTokenCode)

        return errorHandling(info)

def pay (paymentRequestId, paymentNotifyUrl, paymentExpiryTime, amountInCents, goodsId, buyerId, goodsName = "mobile1", orderDescription = "title"):

        body = {
                "productCode":"CASHIER_PAYMENT",
                "salesCode":"51051000101000000011",
                "paymentNotifyUrl": f"{paymentNotifyUrl}",
                "paymentRequestId": f"{paymentRequestId}",
                "paymentRedirectUrl":"http://mock.vision.vodacom.aws.corp/mock/api/v1/payments/notifyPayment.htm",
                "paymentExpiryTime": f"{paymentExpiryTime}",
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

        paymentResponse = request('POST', "v2/payments/pay", body)
        
        return errorHandling(paymentResponse.json())

def paymentInfo(paymentId):

        body = {
            "paymentId": f"{paymentId}",
            "extraParams":{
            },
            "extendInfo":"automation test cases"
        }

        paymentInfoResponse = request('POST', "v2/payments/inquiryPayment", body)

        return errorHandling(paymentInfoResponse.json())