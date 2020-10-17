import requests
from base import Base
from pprint import pprint

class chain(Base):
    def __init__(self, url):
        super(chain, self).__init__(url)

    def get_info(self):
        # 获取与节点相关的最新信息
        return self.get("/v1/chain/get_info")

    def get_block(self, block_num_or_id):
        # 获取一个块的信息
        data_dict = {
            "block_num_or_id": block_num_or_id
        }
        return self.post("/v1/chain/get_block", data=data_dict)

    def get_account(self, account_name):
        # 获取账户的信息
        data_dict = {
            "account_name": account_name
        }
        return self.post("/v1/chain/get_account", data=data_dict)

    def get_code(self, account_name):
        # 获取智能合约代码
        data_dict = {
            "account_name": account_name,
            "code_as_wasm": "true"
        }
        return self.post("/v1/chain/get_code", data=data_dict)

    def get_table_rows(self, account_details):
        """
        Fetch smart contract data from an account.

        :param account_details: (str) account details, the format
        must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_table_rows'

        return self.post(path, data=account_details)

    def abi_json_to_bin(self, data):
        """
        Serialize json to binary hex. The resulting binary hex is usually
        used for the data field in push_transaction.

        :param data: (str) the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/abi_json_to_bin'
        return self.post(path, data=data)

    def abi_bin_to_json(self, data):
        """
        Serialize back binary hex to json.

        :param data:  (str) the format must be a string of a json
        :return:response object
        """
        path = '/v1/chain/abi_bin_to_json'
        return self.post(path, data=data)

    def push_transaction(self, transaction):
        """
        This method expects a transaction in JSON format and will
        attempt to apply it to the blockchain,

        :param transaction: (str) transaction, the format must be a
        string of a json
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.post(path, data=transaction)

    def push_transactions(self, transactions):
        """
        This method push multiple transactions at once.

        :param transactions: (str) list of transactions, the format must be a
        string of a list
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.post(path, data=transactions)

    def get_required_keys(self, transaction_data):
        """
        Get required keys to sign a transaction from list of your keys.

        :param transaction_data: (str) transaction data with a list of keys,
        the format must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_required_keys'
        return self.post(path, data=transaction_data)