# encoding: utf-8
from api.api import SellerActive


class Orders(SellerActive):
    """
        DELETE /api/Order Delete existing order
        GET /api/Order Get list of orders
        POST /api/Order Add new order
        PUT /api/Order
    """

    def get_orders(self, **kwargs):
        print(self.SELLER_ID, self.API_KEY)
        # params={'SiteOrderID': '111-8818282-8868216'}
        return self._request(path='api/Order', **kwargs)
