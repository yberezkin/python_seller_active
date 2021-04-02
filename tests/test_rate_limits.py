# encoding: utf-8
import unittest
from api.endpoints import *


class RateLimitsTestCase(unittest.TestCase):

    def test_rate_limit_status(self):
        resp = RateLimit().rate_limit_status()
        self.assertIsNotNone(resp)
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json(), dict)


if __name__ == '__main__':
    unittest.main()
# r = Orders().get_orders()

