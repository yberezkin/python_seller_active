# encoding: utf-8
from api.api import SellerActive


class Bundles(SellerActive):
    """
        DELETE /api/Order Delete existing order
        GET /api/Order Get list of orders
        POST /api/Order Add new order
        PUT /api/Order
    """

    def get_bundle(self, **kwargs):
        # params={'SiteOrderID': '111-8818282-8868216'}
        return self._request(path='api/Bundle', **kwargs)
