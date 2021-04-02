# encoding: utf-8
__version__ = '0.1'
from api.config import CONFIGS
import requests
import json
from requests.auth import HTTPBasicAuth


class SellerActive(CONFIGS['bnm']):

    def __init__(self):
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
