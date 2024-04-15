from uuid import uuid4
from index import config, getConfig, pay, userInfo, paymentInfo

if __name__ == "__main__":
    config("2020122653946739963336", "216620000000188034591", "./certificates/rsa_private_key.pem", "sandbox")

    # print(getConfig())

    # user info
    # authcode = "0000000001sUUMM2meQy767N00719609"
    # userInfoResponse = userInfo(authcode)
    # print(userInfoResponse)

    # payment
    # paymentExpiryTime = 2
    # paymentId = uuid4()
    # paymentNotifyUrl = "https://webhook.site/c7add433-3e51-4e46-8ebc-9adb4a129042"
    # amountInCents = 2000
    # goodsId = "goods123"
    # buyerId = 216610000000920845761
    # paymentResponse = pay(paymentId, paymentNotifyUrl, paymentExpiryTime, amountInCents, goodsId, buyerId)
    # print(paymentResponse)

    # payment Info
    # paymentInfoResponse = paymentInfo('20240415111212800100166760400601553')
    # print(paymentInfoResponse)