# encoding: utf-8
from datetime import datetime
from typing import Dict, Optional

from seller_active.base import BaseClient


class Orders(BaseClient):
    endpoint = "Order"

    def get_orders(
        self,
        site_order_id: Optional[str] = None,
        seller_order_id: Optional[str] = None,
        sa_order_id: Optional[str] = None,
        site_item_id: Optional[str] = None,
        sku: Optional[str] = None,
        site: Optional[str] = None,
        order_status: Optional[str] = None,
        upc: Optional[str] = None,
        vendor: Optional[str] = None,
        shipped_after: Optional[datetime] = None,
        shipped_before: Optional[datetime] = None,
        ordered_after: Optional[datetime] = None,
        ordered_before: Optional[datetime] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
        page: int = 1,
        page_size: int = 100,
    ):
        """
        Retrieve list of orders using provided filter parameters. Requests for pages > 1,000 will be
        rejected. Please use the parameters (e.g. updated_after) to reduce the data returned.
        """
        params = {
            k: v
            for k, v in {
                "page": page,
                "page_size": page_size,
                "site_order_id": site_order_id,
                "seller_order_id": seller_order_id,
                "sa_order_id": sa_order_id,
                "site_item_id": site_item_id,
                "sku": sku,
                "site": site,
                "order_status": order_status,
                "upc": upc,
                "vendor": vendor,
                "shipped_after": shipped_after,
                "shipped_before": shipped_before,
                "ordered_after": ordered_after,
                "ordered_before": ordered_before,
                "created_after": created_after,
                "created_before": created_before,
                "updated_after": updated_after,
                "updated_before": updated_before,
            }.items()
            if v is not None
        }

        return self._request("GET", params=params)

    def update_order(self, data: Dict):
        """
        Modifies an existing order, orders are specified using the combination of required attributes 'Site' and
        'SiteOrderID'. Specific order items are related back using 'SiteItemID'. Ensure orders exist before
        attempting to modify. To quickly fulfill an order (Post tracking information and mark as shipped) use the
        additional fields 'Status', 'OrderTracking', 'OrderService', and 'OrderCarrier'. This will post the shipping
        information to all order details related to that order.
        """
        if "Site" not in data.keys() or "SiteOrderID" not in data.keys():
            raise ValueError("'Site' or 'SiteOrderID' attribute(s) was not found in `data`.")
        return self._request("PUT", data=data)

    def delete_order(self, site_order_id: str, site: str, site_item_id: Optional[str] = None):
        """
        Deletes an existing order specified by required attributes 'SiteOrderID' and 'Site'. Attribute 'SiteItemID'
        is an optional field, if specified the action will delete the single order item, otherwise if not specified
        the entirety of the order is deleted.
        """
        params = {
            "site_order_id": site_order_id,
            "site": site,
            "site_item_id": site_item_id,
        }
        return self._request("DELETE", params=params)

    def create_order(self, data: Dict):
        """
        Creates a new order, Site Order ID must be unique per marketplace. Required fields include SiteOrderID, Site,
        OrderStatus, and SiteItemID (On the order detail level). Requires at least one order detail specified.
        """
        required_keys = {"SiteOrderID", "Site", "OrderStatus", "SiteItemID", "OrderDetails"}
        if not required_keys.issubset(data.keys()):
            missing_keys = [k for k in required_keys if k not in data.keys()]
            raise ValueError(f"{missing_keys} attribute(s) was not found in `data`.")

        return self._request("POST", data=data)
