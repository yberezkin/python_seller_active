# encoding: utf-8
from __future__ import annotations

import json
import logging
from json import JSONDecodeError
from typing import Dict

import requests
from requests import Response
from requests.auth import HTTPBasicAuth

from seller_active.__info__ import __package_name__, __version__

from .helpers import params_override

logger = logging.getLogger(__name__)


class BaseClient:
    SCHEME = "https://"
    HOST = "rest.selleractive.com"
    API_VERSION = "api"
    USER_AGENT = f"{__package_name__}-{__version__}"

    def __init__(self, seller_id: str, api_key: str):
        self.seller_id = seller_id
        self.api_key = api_key

        self.session = requests.Session()
        self.session.headers = self.headers
        self.session.auth = self.basic_auth

    @property
    def basic_auth(self) -> HTTPBasicAuth:
        return HTTPBasicAuth(self.seller_id, self.api_key)

    @property
    def headers(self):
        return {
            "user-agent": self.USER_AGENT,
            "host": self.HOST,
            "accept": "application/json",
            "content-type": "application/json",
        }

    @property
    def endpoint(self):
        return self.endpoint

    def _request(
        self,
        method: str,
        data=None,
        params: dict | None = None,
        headers: dict | None = None,
        timeout: float | int | None = None,
    ) -> Dict:
        if params is None:
            params = {}
        else:
            params = params_override(params)
        if data is None:
            data = {}

        resp = self.session.request(
            method,
            f"{self.SCHEME}{self.HOST}/{self.API_VERSION}/{self.endpoint}",
            params=params,
            data=json.dumps(data) if data and method in ("POST", "PUT", "PATCH") else None,
            headers=headers,
            timeout=timeout,
        )
        return self.request_to_api_response(resp)

    @staticmethod
    def request_to_api_response(response: Response) -> Dict:
        try:
            js = response.json() or {}
        except JSONDecodeError:
            if response.request.method in ("DELETE", "PUT") and 200 <= response.status_code < 300:
                js = {}
            else:
                js = {"status_code": response.status_code}

        if isinstance(js, list):
            js = dict(data=js)

        error = js.get("Message", None)

        rate_limits = {
            "rate_limit": response.headers.get("X-RateLimit-Limit", None),
            "rate_limit_remaining": response.headers.get("X-RateLimit-Remaining", None),
            "rate_limit_reset": response.headers.get("X-RateLimit-Reset", None),
        }

        return {"data": js, "error": error, "headers": dict(response.headers), "rate_limits": rate_limits}
