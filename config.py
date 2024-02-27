from services.VodaPay.utils.constants import configurations

environments = {
    "production": "https://gateway.vodapay.vodacom.co.za",
    "sandbox": "https://vodapay-gateway.sandbox.vfs.africa",
    "test4": "https://vodapay-gateway.test4.vfs.africa"
}
    
def set_environment(environment):
    if environment.lower() in environments:
        configurations['VODAPAY_BASEURL'] = environments[environment]
    else:
        raise ValueError(f'Invalid environment: {environment}. Supported values are "production", "sandbox" and "test4".')


def config(clientId, merchantId, privateKeyPath, environment):
        '''
            @params:
                - clientId :
                - userId :
                - merchantId :
                - privateKeyPath :
                - environment
            @response: none
        '''
        configurations['VODAPAY_CLIENT_ID'] = clientId
        configurations['VODAPAY_MERCHANT_ID'] = merchantId
        configurations['PRIVATE_KEY_PATH'] = privateKeyPath
        
        set_environment(environment)

def getConfig():
     return configurations