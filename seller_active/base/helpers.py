# encoding: utf-8
PARAMS_MAPPING = {
    "sku": "req.SKU",
    "individual_sku": "req.individualSKU",
    "bundle_sku": "req.bundleSKU",
    "title": "req.title",
    "site": "req.site",
    "location_name": "req.locationName",
    "vendor": "req.vendor",
    "site_order_id": "req.siteOrderID",
    "seller_order_id": "req.sellerOrderID",
    "sa_order_id": "req.orderID",
    "site_item_id": "req.siteItemID",
    "order_status": "req.orderStatus",
    "upc": "req.UPC",
    "page": "req.page",
    "page_size": "req.size",
    "created_after": "req.dateCreatedFrom",
    "created_before": "req.dateCreatedTo",
    "updated_after": "req.dateUpdatedFrom",
    "updated_before": "req.dateUpdatedTo",
    "shipped_after": "req.dateShippedFrom",
    "shipped_before": "req.dateShippedTo",
    "ordered_after": "req.dateOrderedFrom",
    "ordered_before": "req.dateOrderedTo",
}


def params_override(params):
    result = {PARAMS_MAPPING[k]: v for k, v in params.items()}
    return result
