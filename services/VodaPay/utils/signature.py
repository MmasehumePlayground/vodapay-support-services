import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from config import Configuration

def generate_payload (method, endPoint, requestTime, body):
    '''
        @params:
            - method : the HTTP method used when calling VodaPay APIs (POST)
            - endPoint : the endpoint the request is sent to
            - request time: specifies the time when a request is sent, as defined by RFC3339
            - body : the data of the request body
    '''
    config = Configuration._instance
    VODAPAY_CLIENT_ID = config.get_config()["VODAPAY_CLIENT_ID"]

    unsignedContent = (f"{method} {endPoint}\n{VODAPAY_CLIENT_ID}.{requestTime}.{body}".encode())
    return unsignedContent

def generate_signature (method, endPoint, requestTime, body):
    '''
        @variables :
        - unsignedContent : the content to be signed
        - the algorithm to use is RSA256
        - privateKey : the content of the private key value
    '''
    unsignedContent = generate_payload(method, endPoint, requestTime, body)

    hash = SHA256.new(unsignedContent)
    config = Configuration._instance
    PRIVATE_KEY_PATH = config.get_config()["PRIVATE_KEY_PATH"]

    try:
        with open(PRIVATE_KEY_PATH, 'r') as file:
            privateKeyData = file.read()
            privateKey = RSA.import_key(privateKeyData)

    except FileNotFoundError:
        raise FileNotFoundError(f"Private key file not found at: {configurations['PRIVATE_KEY_PATH']}")

    signature = pkcs1_15.new(privateKey).sign(hash)
    encodedSignature = base64.b64encode(signature).decode()

    return encodedSignature