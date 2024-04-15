# vodapay-support-services
**vodapay-support-services** is Python Library for interacting with VodaPay API for m-commerce.

**vodapay-support-services** allows you to interact with the VodaPay API for m-commerce very easily. There’s no need to manually code the functionality to interact with the API.

# 

# Installation
To install **vodapay-support-services**, simply run this simple command in your terminal of choice:
```
$ pip install vodapay-support-services
```
## Get the Source Code
**vodapay-support-services** is actively developed on GitHub, where the code is always available.

You can clone the public repository:
```
$ https://github.com/MmasehumePlayground/vodapay-support-services.git
```
Once you have a copy of the source, you can embed it in your own Python package, or install it into your site-packages easily:
```
$ cd vodapay-support-services
$ python -m pip install .
```

# Configuration
Before using the library, you need to configure it with your VodaPay API credentials. Use the config function to set the environment, client ID, merchant ID, and private key path.
```
from index import config

config(
        "your_client_id", 
        "your_merchant_id", 
        "path_to_your_private_key.pem", 
        "environment"
    )
```
Environment is ```sandbox``` while project is in dev mode and should be changed to ```production``` when the project is in production.

# Functions


# Usage


# Dependencies




# The API Documentation
If you are looking for information on a specific underlying function, class, or method, this part of the documentation is for you:


# Contributions






- scrit to install all libraries
- requests
- crypto
- 
