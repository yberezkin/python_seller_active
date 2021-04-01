# encoding: utf-8
from pydantic import BaseModel
from api.api import SellerActive


class Status(BaseModel):
    """
    Validation object
    """
    Limit: str
    Remaining: str
    Reset: str


class RateLimit(SellerActive):
    def rate_limit_status(self):
        """GET  api/RateLimitStatus"""
        return self._request(path='api/RateLimitStatus')
