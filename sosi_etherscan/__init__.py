import pkg_resources
__version__ = pkg_resources.get_distribution("sosi_etherscan").version

from .client import EtherscanClient
