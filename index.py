
from services.VodaPay.v2.pay import payment
from services.VodaPay.v2.applyToken import applyToken
from services.VodaPay.v2.inquiryPayment import inquiryPayment
from services.VodaPay.v2.inquiryUserInfo import inquiryUserInfo

from services.VodaPay.utils.formatResponse import formatResponse

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