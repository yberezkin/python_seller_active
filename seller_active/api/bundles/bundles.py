# encoding: utf-8
from datetime import datetime
from typing import Dict, Optional

from seller_active.base import BaseClient


class Bundles(BaseClient):
    endpoint = "Bundle"

    def get_bundles(
        self,
        bundle_sku: Optional[str] = None,
        individual_sku: Optional[str] = None,
        created_after: Optional[datetime] = None,
        created_before: Optional[datetime] = None,
        updated_after: Optional[datetime] = None,
        updated_before: Optional[datetime] = None,
        page: int = 1,
        page_size: int = 100,
    ):
        """
        Retrieve list of bundles using provided filter parameters. Requests for pages > 1,000 will be
        rejected. Please use the parameters (e.g. updated_after) to reduce the data returned.
        """
        params = {
            k: v
            for k, v in {
                "page": page,
                "page_size": page_size,
                "bundle_sku": bundle_sku,
                "individual_sku": individual_sku,
                "created_after": created_after,
                "created_before": created_before,
                "updated_after": updated_after,
                "updated_before": updated_before,
            }.items()
            if v is not None
        }

        return self._request("GET", params=params)

    def update_bundle(self, data: Dict):
        """
        Modifies an existing inventory bundle, all SKUs and relationships must exist prior. Quantity and price values
        are adjusted through the 'Inventory' POST API operations, 'Bundle' POST API operations modify the
        relationship amounts of individual SKUs in each bundle.
        data = {
          "BundleSKU": "string",
          "BundledItems": [
            {
              "SKU": "string",
              "AmountPerBundle": 0
            }
          ]
        }
        """
        if "BundleSKU" not in data.keys() or "BundledItems" not in data.keys():
            raise ValueError("'BundleSKU' or 'BundledItems' attribute was not found in `data`.")
        return self._request("PUT", data=data)

    def delete_inventory(self, bundle_sku: str, individual_sku: Optional[str] = None):
        """
        Deletes an existing bundle relationship. BundleSKU attribute is required to specify the bundle, individual
        SKU is an optional attribute. Specifying the individual SKU will remove that single item from the bundle
        relationship, specifying only the bundle SKU will remove all items from the bundle relationship.

        """
        params = {
            k: v
            for k, v in {
                "bundle_sku": bundle_sku,
                "individual_sku": individual_sku,
            }.items()
            if v is not None
        }
        return self._request("DELETE", params=params)

    def create_bundle(self, data: Dict):
        """
        Creates a new inventory bundle relationship, all SKUs specified must exist in inventory table prior.
        Limitations still apply, SKUs that have warehouse locations or are FBA items cannot be bundled. A bundle SKU
        cannot be contained in another bundle as an individual SKU, and an individual SKU cannot be specified as a
        bundle SKU.
        data = {
          "BundleSKU": "string",
          "BundledItems": [
            {
              "SKU": "string",
              "AmountPerBundle": 0
            }
          ]
        }
        """
        required_keys = {"BundleSKU", "BundledItems"}
        if not required_keys.issubset(data.keys()):
            missing_keys = [k for k in required_keys if k not in data.keys()]
            raise ValueError(f"{missing_keys} attribute(s) was not found in `data`.")

        return self._request("POST", data=data)
