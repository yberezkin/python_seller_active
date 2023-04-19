from enum import Enum


class RequestParams(Enum):
    SKU = "req.SKU"
    INDIVIDUAL_SKU = "req.individualSKU"
    BUNDLE_SKU = "req.bundleSKU"
    TITLE = "req.title"
    SITE = "req.site"
    LOCATION_NAME = "req.locationName"
    VENDOR = "req.vendor"
    SITE_ORDER_ID = "req.siteOrderID"
    SELLER_ORDER_ID = "req.sellerOrderID"
    SA_ORDER_ID = "req.orderID"
    SITE_ITEM_ID = "req.siteItemID"
    ORDER_STATUS = "req.orderStatus"
    UPC = "req.UPC"
    PAGE = "req.page"
    PAGE_SIZE = "req.size"
    CREATED_AFTER = "req.dateCreatedFrom"
    CREATED_BEFORE = "req.dateCreatedTo"
    UPDATED_AFTER = "req.dateUpdatedFrom"
    UPDATED_BEFORE = "req.dateUpdatedTo"
    SHIPPED_AFTER = "req.dateShippedFrom"
    SHIPPED_BEFORE = "req.dateShippedTo"
    ORDERED_AFTER = "req.dateOrderedFrom"
    ORDERED_BEFORE = "req.dateOrderedTo"


def params_override(params):
    result = {RequestParams[k.upper()].value: v for k, v in params.items()}
    return result
