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

    def address_transactions(self, address):
        """
        Note: This API endpoint returns a maximum of 10,000 records only.
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
        # status =  response.get("status")  # eg 1
        # status_message = response.get("message") # eg "OK"
        transactions = response.get("result")
        n_received = len(transactions)
        if n_received > limit:
            print(f"WARNING: the results might have been clipped. Max limit for"
                  f"transactions endpoint is {limit}, received {n_received}.")

        # Create a datetime string field called `time`
        for item in transactions:
            item["time"] = dtutils.timestamp_to_datetime_str(item["timeStamp"], tz="UTC", unit="s")

        return transactions
