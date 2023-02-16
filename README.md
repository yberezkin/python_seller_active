# SELLER-ACTIVE-API Python Wrapper

This project provides a Python wrapper for interacting with the [rest.selleractive.com](https://rest.selleractive.com/) API, allowing developers to easily integrate the API's functionality into their Python applications.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Installing

![Badge](https://img.shields.io/pypi/v/python_seller_active?style=for-the-badge)(https://pypi.org/project/python-seller-active/)


    pip install python_seller_active


---

### Usage

```python
from seller_active.api import Inventory

# repricer reports API
data = Inventory(seller_id='your_username', api_key='your_password').get_inventory()
print(data)
# or
cli = Inventory(seller_id='your_username', api_key='your_password')
data = cli.get_inventory()
print(data)
```

## License

![License](https://img.shields.io/github/license/yberezkin/python_seller_active?style=for-the-badge)
