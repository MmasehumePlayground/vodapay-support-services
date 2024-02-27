from datetime import datetime

from services.VodaPay.utils.signature import generate_signature
from services.VodaPay.utils.constants import configurations

def construct_headers (method, endPoint, body, isRequest = True):

    time_stamp_key = 'request-time' if isRequest else 'response-time'
    now = datetime.now()
    requestTime = now.astimezone().isoformat()

    signature_value = generate_signature (method, endPoint, requestTime, body)

    headers = {
        'Content-Type': 'application/json',
        'client-id': configurations['VODAPAY_CLIENT_ID'], 
        'signature': f'algorithm=RSA256, keyVersion=1, signature={signature_value}'
    }

    headers[time_stamp_key] = requestTime

    return headers