import os
import argparse
import time
import json
import requests
import jwt
from axil_authorizer import AxilAuthorizer

URL_ENV_MAP = {
    'dev': 'https://dev-api.axil.ai/airmethane/external/inspections',
    'prod': 'https://api.axil.ai/airmethane/external/inspections'
}


def get_records(auth_token: str, request_url: str) -> dict:
    print('get_records :: starting')
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    req_resp = requests.request(method='get', url=request_url, headers=headers)
    if req_resp.status_code != requests.codes.ok:
        raise Exception(f'Error occurred retrieving inspections: {req_resp.reason}')
    recs = req_resp.json()
    print(f'get_records :: {len(recs.get("inspections", 0))} recs :: completed\n')
    return recs


if __name__ == '__main__':
    
    client_credentials = {
        'client_id': os.environ.get('AUTH0_CLIENT_ID'),
        'client_secret': os.environ.get('AUTH_CLIENT_SECRET')
    }
    
    jwt_token = None
    
    if os.path.isfile('jwt.json'):
        with open('jwt.json', 'r', encoding='utf-8') as jwt_file:
            jwt_val = jwt_file.read()
        jwt_token = jwt_val
        
        jwt_decoded = jwt.decode(jwt_val, options={"verify_signature": False})

        if jwt_decoded['exp'] <= time.time():
            jwt_token = None

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--environment',
                        help='The environment to be used',
                        choices=['dev', 'prod'],
                        default='dev',
                        )
    parser.add_argument('-o', '--orgs', help='Return inspections for given org/company ID', required=False)
    parser.add_argument('-s', '--sites', help='Return inspections for given site/location ID', required=False)
    parser.add_argument('-a', '--inspectionDateAfter', help='Return inspections on or after this date, ISO format YYYY-MM-DD', required=False)
    parser.add_argument('-b', '--inspectionDateBefore', help='Return inspections on or before this date, ISO format YYYY-MM-DD', required=False)
    parser.add_argument('-i', '--id', help='Return inspections for matching ID', required=False)
    args = parser.parse_args()

    token_obj = AxilAuthorizer(client_credentials['client_id'], client_credentials['client_secret'], jwt_token)
    
    if token_obj.token is not None:
        with open('jwt.json', 'w+', encoding='utf-8') as jwt_write:
            jwt_write.write(token_obj.token)

    get_url = f'{URL_ENV_MAP[args.environment]}/'
    parameters_url = '/'.join([f'{arg_key}/{arg_val}' for arg_key, arg_val in vars(args).items()
                                if arg_key != 'environment' and arg_val is not None])
    
    request_url = get_url + parameters_url
    
    print(f'{request_url}\n')

    inspection_response = get_records(token_obj.token, request_url)
    
    with open('inspections.json', 'w+', encoding='utf-8') as json_write:
        json_write.write(json.dumps(inspection_response, indent=4))