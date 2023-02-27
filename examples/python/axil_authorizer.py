'''
Pass your auth0 client ID and secret to authenticate and retrieve your token
'''

import requests

class AxilAuthorizer:

    def __init__(self, client_id, client_secret, client_token = None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = client_token
        
        if client_token is None:
            self.authenticate()
    

    def authenticate(self):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'audience': 'https://api.axil.ai',
            'grant_type': 'client_credentials'
        }
        
        headers = {'content-type': 'application/json'}
        
        req_resp = requests.post('https://axil.auth0.com/oauth/token',
                         headers=headers,
                         json=payload,
                         )
        if req_resp.status_code != requests.codes.ok:
            raise Exception(f'Error occurred getting Bearer token: {req_resp.reason}')
        
        self.token = req_resp.json()['access_token']
        
        
