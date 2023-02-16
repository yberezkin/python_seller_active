import setuptools

from seller_active import __info__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__info__.__package_name__,
    version=__info__.__version__,
    author=__info__.__author__,
    author_email=__info__.__email__,
    description="Wrapper around SellerActive.com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__info__.__repo_url__,
    project_urls={"Bug Tracker": __info__.__bug_tracker__},
    license=__info__.__license__,
    install_requires=["requests"],
    packages=[
        "seller_active",
        "seller_active.base",
        "seller_active.api",
        "seller_active.api.bundles",
        "seller_active.api.inventory",
        "seller_active.api.locations",
        "seller_active.api.orders",
        "seller_active.api.rate_limit_status",
    ],
)
