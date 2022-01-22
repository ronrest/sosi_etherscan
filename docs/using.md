# Using
## Connecting to Client


```python
from sosi_etherscan import EtherscanClient

# Use this if you already set the `ETHERSCAN_API_KEY` environment variable
client = EtherscanClient()

# Use the following if you want to pass the API key explicitly in code
# client = EtherscanClient(key=XXX)



```

## Basic usage


```
wallet_address = "XXX"
transactions = client.address_transactions(wallet_address)
```