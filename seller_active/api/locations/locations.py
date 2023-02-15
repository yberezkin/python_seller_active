# encoding: utf-8
from datetime import datetime
from typing import Dict, Optional

from seller_active.base import BaseClient


class Locations(BaseClient):
    endpoint = "Location"

    def get_locations(
        self,
        sku: Optional[str] = None,
        location_name: Optional[str] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
        page: int = 1,
        page_size: int = 100,
    ):
        """
        Retrieve list of inventory locations using provided filter parameters Requests for pages > 1,000 will be
        rejected. Please use the parameters (e.g. updated_after) to reduce the data returned.
        """
        params = {
            k: v
            for k, v in {
                "page": page,
                "page_size": page_size,
                "sku": sku,
                "location_name": location_name,
                "created_after": created_after,
                "created_before": created_before,
                "updated_after": updated_after,
                "updated_before": updated_before,
            }.items()
            if v is not None
        }

        return self._request("GET", params=params)

    def update_location(self, data: Dict):
        """
        Modify an existing inventory location, must specify the location by both
        required attributes 'SKU' and 'LocationName'.
        data = {
          "SKU": "string",
          "LocationName": "string",
          "Quantity": 0,
          "Priority": 0,
          "Type": "None",
          "Integration": "None"
        }
        """
        if "SKU" not in data.keys() or "LocationName" not in data.keys():
            raise ValueError("'SKU' or 'LocationName' attribute(s) was not found in `data`.")
        return self._request("PUT", data=data)

    def delete_location(self, sku: str, location_name: str):
        """
        Delete an existing inventory location, must specify the location by both
        required attributes 'SKU' and 'LocationName'.
        """
        params = {
            "sku": sku,
            "location_name": location_name,
        }
        return self._request("DELETE", params=params)

    def create_location(self, data: Dict):
        """
        Adds a new location to an existing inventory item, attribute 'SKU' is required to specify the item and
        quantity of location must be greater than or equal to 0. Location names should be unique.
        data = {
          "SKU": "string",
          "LocationName": "string",
          "Quantity": 0,
          "Priority": 0,
          "Type": "None",
          "Integration": "None"
        }
        """
        required_keys = {"SKU", "LocationName", "Quantity", "Priority"}
        if not required_keys.issubset(data.keys()):
            missing_keys = [k for k in required_keys if k not in data.keys()]
            raise ValueError(f"{missing_keys} attribute(s) was not found in `data`.")

        return self._request("POST", data=data)
