"""
Etherscan.io API
    https://docs.etherscan.io/

    Endpoint URLS
        https://docs.etherscan.io/getting-started/endpoint-urls
        There are different endpoints, and doc pages for the different
        main/testnet networks.


LIMITS
-------
    - 5 calls per second
    - 100,000 calls per day
    - (Which makes it an absolute upper limit of 1.157 if making LOTS of requests)
    - Question: is this rate limit per account? or per IP Address?

"""
from sosi_api import BaseClient
from sosi_api.utils import dt as dtutils
import decouple
import datetime

env = decouple.AutoConfig(search_path="./.env")
# from urllib.parse import urlencode

class EtherscanClient(BaseClient):
    def __init__(self, key=None):
        super().__init__(
            base_url="https://api.etherscan.io",
            headers=None,
            max_requests_per_min=5*60,
            response_kind="json",
        )
        self.api_key = key if key is not None else env('ETHERSCAN_API_KEY', cast=str)
        assert self.api_key is not None, "Missing ETHERSCAN_API_KEY"

    def _process_list_response(self, response, limit=10000):
        # status =  response.get("status")  # eg 1
        # status_message = response.get("message") # eg "OK"
        items = response.get("result", [])
        n_received = len(items)
        if n_received > limit:
            print(f"WARNING: the results might have been clipped. Max limit for"
                  f"transactions endpoint is {limit}, received {n_received}.")

        # Create a datetime string field called `time`
        for item in items:
            item["time"] = dtutils.timestamp_to_datetime_str(item["timeStamp"], tz="UTC", unit="s")

        return items

    def transactions(self, address):
        """Get normal transactions for a given address.
        
        Notes: 
            This API endpoint returns a maximum of 10,000 records only.
        """
        # TODO: to pagination to handle addresses with lots of transactions
        endpoint = "/api"
        url = self.base_url + endpoint
        limit = 10000
        params = dict(
            module="account",
            action="txlist",
            address=address,
            sort="asc",
            startblock=0,
            # endblock=99999999,
            page=1,
            offset=0,
            apikey=self.api_key,
        )
        response = self.request(url=url, params=params, kind="get")
        items = self._process_list_response(response, limit=limit)
        return items

    def internal_transactions(self, address):
        """Get list of internal transactions for an address.

        Notes: 
            This API endpoint returns a maximum of 10,000 records only.
        """
        # TODO: pagination
        endpoint = "/api"
        url = self.base_url + endpoint
        limit = 10000
        params = dict(
            module="account",
            action="txlistinternal",
            address=address,  # from an address. Does it also show the ones to this address?
            sort="asc",
            startblock=0,
            # endblock=99999999,
            page=1,
            offset=0,
            apikey=self.api_key,
        )
        if token_address is not None:
            params["contractAddres"] = token_address

        response = self.request(url=url, params=params, kind="get")
        items = self._process_list_response(response, limit=limit)
        return items

    def erc20_transactions(self, address, token_address=None):
        """Get list of ERC20 token transactions for an address. Optionally filter 
        for only certain tokens by providing the token contract address.

        Notes: 
            It is not clear what the limit for this endpoint is. Assuming it is 
            same as other endpoints, of 10,000 records.
        """
        # TODO: pagination
        endpoint = "/api"
        url = self.base_url + endpoint
        limit = 10000   # WARNING: it is not clear what the default limit is for
                        # this endpoint. Naively assuming it is same as normal 
                        # transactions endpoint.
        params = dict(
            module="account",
            action="tokentx",
            address=address,  # from an address. Does it also show the ones to this address?
            sort="asc",
            startblock=0,
            # endblock=99999999,
            page=1,
            offset=0,
            apikey=self.api_key,
        )
        if token_address is not None:
            params["contractAddres"] = token_address

        response = self.request(url=url, params=params, kind="get")
        items = self._process_list_response(response, limit=limit)
        return items

    def erc721_transactions(self, address, token_address=None):
        """Get list of ERC721 (NFT) token transactions for an address. Optionally
        filter for only certain tokens by providing the token contract address.

        Notes: 
            It is not clear what the limit for this endpoint is. Assuming it is 
            same as other endpoints, of 10,000 records.
        """
        # TODO: pagination
        endpoint = "/api"
        url = self.base_url + endpoint
        limit = 10000   # WARNING: it is not clear what the default limit is for
                        # this endpoint. Naively assuming it is same as normal 
                        # transactions endpoint.
        params = dict(
            module="account",
            action="tokennfttx",
            address=address,  # from an address. Does it also show the ones to this address?
            sort="asc",
            startblock=0,
            # endblock=99999999,
            page=1,
            offset=0,
            apikey=self.api_key,
        )
        if token_address is not None:
            params["contractAddres"] = token_address

        response = self.request(url=url, params=params, kind="get")
        items = self._process_list_response(response, limit=limit)
        return items
