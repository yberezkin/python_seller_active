# encoding: utf-8
__version__ = '0.1'
import requests
import json
from requests.auth import HTTPBasicAuth
import os
import sys
import configparser
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def load_config(path=None):
    if path is None:
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, 'config.ini')
    _config = configparser.ConfigParser()
    _config.read(path)
    return _config


class SellerActive:
    HOST = 'https://rest.selleractive.com'

    def __init__(self, _config):
        config = load_config()
        self.SELLER_ID = config.get(_config, 'SELLER_ID')
        self.API_KEY = config.get(_config, 'API_KEY')

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.SELLER_ID, self.API_KEY)
        self.session.headers = {
            'User-Agent': f'SellerActiveAPIWrapper/v.{__version__} (python 3.9)',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Host': 'rest.selleractive.com',
            'Connection': 'keep-alive'
        }

    def _request(self, method='GET', path='/', params=None, data=None, headers=None):
        if params is None:
            params = {}
        if data is None:
            data = {}
        if headers is not None:
            self.session.headers.update(**headers)

        resp = self.session.request(
            method, url=f'{self.HOST}/{path}', params=params,
            data=json.dumps(data) if data and method in ('POST', 'PUT') else None,
        )
        return resp

    # def check_for_errors(self, response):
    #     error = response.json().get('errors', None)
    #     if error:
    #         exception = get_exception_for_code(response.status_code)
    #         raise exception(error)
    #     return ApiResponse(**res.json(), headers=res.headers)
