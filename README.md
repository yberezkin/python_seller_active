# SELLER-ACTIVE-API Python Wrapper

This project provides a Python wrapper for interacting with the [rest.selleractive.com](https://rest.selleractive.com/) API, allowing developers to easily integrate the API's functionality into their Python applications.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Installing
[![Badge](https://img.shields.io/pypi/v/xsellco-api?style=for-the-badge)](https://pypi.org/project/xsellco-api/)

    pip install xsellco_api

---

### Usage

```python
from seller_active.api import Inventory

# repricer reports API
data = Inventory(seller_id='your_username', api_key='your_password').get_inventory()
print(data)  # list of dictionaries
# or utilize
cli = Inventory(seller_id='your_username', api_key='your_password')
data = cli.get_inventory()
print(data)
```

## License

![License](https://img.shields.io/github/license/yberezkin/xsellco-api?style=for-the-badge)
