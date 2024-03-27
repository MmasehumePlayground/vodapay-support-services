from datetime import datetime

from config import Configuration
from services.VodaPay.utils.signature import generate_signature

def construct_headers (method, endPoint, body, isRequest = True):

    time_stamp_key = 'request-time' if isRequest else 'response-time'
    now = datetime.now()
    requestTime = now.astimezone().isoformat()

    signature_value = generate_signature (method, endPoint, requestTime, body)
    config = Configuration._instance
    VODAPAY_CLIENT_ID = config.get_config()["VODAPAY_CLIENT_ID"]

    headers = {
        'Content-Type': 'application/json',
        'client-id': VODAPAY_CLIENT_ID, 
        'signature': f'algorithm=RSA256, keyVersion=1, signature={signature_value}'
    }

    headers[time_stamp_key] = requestTime

    return headers