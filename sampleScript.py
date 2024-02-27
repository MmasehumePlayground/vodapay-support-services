from uuid import uuid4
from config import config, getConfig
from index import pay, userInfo, paymentInfo
from datetime import datetime, timedelta


if __name__ == "__main__":
    config("2020122653946739963336", "216620000000188034591", "./certificates/rsa_private_key.pem", "sandbox")

    # print(getConfig())

    # user info
    # authcode = "0000000001aSwCRUNfce76y800675232"
    # userInfoResponse = userInfo(authcode)
    # print(userInfoResponse)

    # payment
    # now = datetime.now() + timedelta(hours=2)
    # paymentExpiryTime = now.astimezone().isoformat()
    # paymentId = uuid4()
    # paymentNotifyUrl = "https://webhook.site/c7add433-3e51-4e46-8ebc-9adb4a129042"
    # amountInCents = 2000
    # goodsId = "goods123"
    # buyerId = 216610000000920845761
    # paymentResponse = pay(paymentId, paymentNotifyUrl, paymentExpiryTime, amountInCents, goodsId, buyerId)
    # print(paymentResponse)

    # # payment Info
    # paymentInfoResponse = paymentInfo('20240213111212800100166768100558564')
    # print(paymentInfoResponse)