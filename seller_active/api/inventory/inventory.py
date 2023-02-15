# encoding: utf-8
from datetime import datetime
from typing import Dict, Optional

from seller_active.base import BaseClient


class Inventory(BaseClient):
    endpoint = "Inventory"

    def get_inventory(
        self,
        sku: Optional[str] = None,
        title: Optional[str] = None,
        site: Optional[str] = None,
        vendor: Optional[str] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
        page: int = 1,
        page_size: int = 100,
    ):
        """
        Retrieve list of inventory items using provided filter parameters Note: Requests for pages > 1,000 will be
        rejected. Please use the parameters (e.g. updated_after) to reduce the data returned.
        """
        params = {
            k: v
            for k, v in {
                "page": page,
                "page_size": page_size,
                "sku": sku,
                "site": site,
                "title": title,
                "vendor": vendor,
                "created_after": created_after,
                "created_before": created_before,
                "updated_after": updated_after,
                "updated_before": updated_before,
            }.items()
            if v is not None
        }

        return self._request("GET", params=params)

    def update_inventory(self, data: Dict):
        """
        Modifies an existing inventory item, inventory is identified using required attribute 'SKU'.
        """
        if "SKU" not in data.keys():
            raise ValueError(
                "'SKU' attribute was not found in `data`."
                "Inventory Product is identified using required attribute 'SKU'"
            )
        return self._request("PUT", data=data)

    def delete_inventory(self, sku: str, site: Optional[str] = None):
        """
        Deletes an existing inventory item, or if attribute 'site' is specified deletes an existing listing under the
        specified marketplace. Only specifying SKU will delete all listings and the item.
        """
        params = {
            k: v
            for k, v in {
                "sku": sku,
                "site": site,
            }.items()
            if v is not None
        }
        return self._request("DELETE", params=params)

    def create_inventory(self, data: Dict):
        """
        Creates a new inventory item, SKU must be unique for every inventory item (Case insensitive), as well as
        at least one marketplace specified for the item to be listed under.

        Required fields include SKU, Condition, Title, ProductID, ProductTypy, Price, and Quantity
        """
        required_keys = {"SKU", "Condition", "Title", "ProductID", "ProductType", "Price", "Quantity"}
        if not required_keys.issubset(data.keys()):
            missing_keys = [k for k in required_keys if k not in data.keys()]
            raise ValueError(
                f"{missing_keys} attribute(s) was not found in `data`."
                f"Required fields include SKU, Condition, Title, ProductID, ProductTypy, Price, "
                f"and Quantity"
            )

        return self._request("POST", data=data)
