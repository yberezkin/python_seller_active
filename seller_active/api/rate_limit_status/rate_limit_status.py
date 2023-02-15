# encoding: utf-8
from seller_active.base import BaseClient


class RateLimitStatus(BaseClient):
    endpoint = "RateLimitStatus"

    def get_rate_limit_status(self):
        return self._request("GET")
