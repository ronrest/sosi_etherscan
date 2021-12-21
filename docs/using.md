# Using

```python
from sosi_etherscan import EtherscanClient
client = EtherscanClient()

wallet_address = "XXX"
transactions = client.address_transactions(wallet_address)
```