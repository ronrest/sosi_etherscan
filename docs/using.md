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


```python
wallet_address = "XXX"

# Get regular transactions
transactions = client.transactions(wallet_address)

# Get list of internal transactions
internal_transactions = client.internal_transactions(wallet_address)

# Get ERC-20 transactions
erc20_transactions = client.erc20_transactions(wallet_address)

# Get ERC-20 transactions, filtering for a specific token
token_contract_address="ZZZ"
erc20_transactions = client.erc20_transactions(wallet_address, token_address=token_contract_address)


# Get ERC-721 transactions
erc721_transactions = client.erc721_transactions(wallet_address)

token_contract_address="ZZZ"
erc721_transactions = client.erc721_transactions(wallet_address, token_address=token_contract_address)
```
