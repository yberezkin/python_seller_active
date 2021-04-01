# encoding: utf-8
from api.api import SellerActive


class Orders(SellerActive):
    """
        DELETE /api/Order Delete existing order
        GET /api/Order Get list of orders
        POST /api/Order Add new order
        PUT /api/Order
    """

    def get_orders(self):
        return self._request(path='api/Order', params={'SiteOrderID': '111-8818282-8868216'})
