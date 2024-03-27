
from config import Configuration
from services.VodaPay.v2.pay import payment
from services.VodaPay.v2.applyToken import applyToken
from services.VodaPay.v2.inquiryPayment import inquiryPayment
from services.VodaPay.v2.inquiryUserInfo import inquiryUserInfo

from services.VodaPay.utils.formatResponse import formatResponse
 
config_obj = Configuration()

def config(clientId, merchantId, privateKeyPath, environment):

    # Set configuration using methods
    config_obj.set_config(
        clientId= clientId,
        merchantId= merchantId,
        privateKeyPath= privateKeyPath,
        environment= environment  #"production" or "sandbox", "test4"
    )

def getConfig():
    return config_obj.get_config()

def userInfo(authCode):
    applyTokenCode = applyToken(authCode)
    info = inquiryUserInfo(applyTokenCode)

    return formatResponse(info)

def pay (paymentRequestId, paymentNotifyUrl, paymentExpiryTime, amountInCents, goodsId, buyerId, goodsName = "default", orderDescription = "default"):
    paymentResponse = payment(paymentRequestId, paymentNotifyUrl, paymentExpiryTime, amountInCents, goodsId, buyerId, goodsName, orderDescription)

    return formatResponse(paymentResponse)

def paymentInfo(paymentId):
    paymentInfoResponse = inquiryPayment(paymentId)

    return paymentInfoResponse