
def formatResponse (response):
    
    if isinstance(response, Exception) :
        message = {
            'results' : 'fail',
        }
        message.update({
            'error' : {
                'code' : 'INTERNAL_ERROR',
                'message' : 'An internal error occurred while processing the request.'
            }            
        })
    
    elif  response.get('result').get('resultStatus').upper() == 'S' or  response.get('result').get('resultStatus').upper() == 'A':
        message = {
            'results' : 'success',
        }
        if response.get('result').get('resultStatus').upper() == 'A':
            message.update({
                'paymentId' : response.get('paymentId'),
                'redirectUrl' : response.get('redirectActionForm').get('redirectUrl')
            })
            
        else:
            message.update({
                'userInfo' : {
                    'userID' :response.get('userInfo').get('userID') ,
                    'username' : response.get('userInfo').get('nickName') ,
                    'firstname' : response.get('userInfo').get('userName').get('firstName') ,
                    'lastname': response.get('userInfo').get('userName').get('lastName') ,
                    'email': [contact_info['contactNo'] for contact_info in response.get('userInfo', {}).get('contactInfos', []) if contact_info.get('contactType') == 'EMAIL'][0],
                    'phone': [contact_info['contactNo'] for contact_info in response.get('userInfo', {}).get('contactInfos', []) if contact_info.get('contactType') == 'MOBILE_PHONE'][0]
                }
            })
      
    else:
        message = {
            'results' : 'fail',
        }
        message.update({
            'error' : {
                'code' : response.get('result').get('resultCode'),
                'message' : response.get('result').get('resultMessage')
            }            
        })
    
    return message 