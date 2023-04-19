from dataclasses import dataclass
from json import JSONDecodeError
from typing import Dict, List

from requests import Response


@dataclass
class ApiResponse:
    _response: Response
    status_code: int | None = None
    data: List | None = None
    error: str | None = None
    headers: Dict | None = None
    rate_limits: Dict | None = None

    def __post_init__(self):
        self.status_code = self._response.status_code
        self.headers = dict(self._response.headers)
        self._check_response()

    def _check_response(self):
        try:
            js = self._response.json() or {}
        except JSONDecodeError:
            if self._response.request.method in ("DELETE", "PUT") and 200 <= self._response.status_code < 300:
                js = {}
            else:
                js = {"status_code": self._response.status_code}

        if isinstance(js, list):
            js = {"data": js}

        self.error = js.get("Message", None)

        self.rate_limits = {
            "rate_limit": self._response.headers.get("X-RateLimit-Limit", None),
            "rate_limit_remaining": self._response.headers.get("X-RateLimit-Remaining", None),
            "rate_limit_reset": self._response.headers.get("X-RateLimit-Reset", None),
        }

        self.data = js.get("data", None)

    def is_success(self) -> bool:
        return self.error is None

    def __str__(self) -> str:
        return (
            f"API response with data: {self.data}, error: {self.error}, "
            f"headers: {self.headers}, rate_limits: {self.rate_limits}"
        )
