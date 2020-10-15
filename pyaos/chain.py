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

    def get_table_rows(self, scope, code, table, lower_bound=None, upper_bound=None, limit=None):


        data_dict = {
            "scope": scope,
            "code": code,
            "table": table,
            "json": "true",
        }
        if lower_bound:
            data_dict["lower_bound"] = lower_bound
        if upper_bound:
            data_dict["upper_bound"] = upper_bound
        if limit:
            data_dict["limt"] = limit

        return self.post("/v1/chain/get_table_rows", data=data_dict)

    def abi_json_to_bin(self,code, jsonargs):
        data_dict = {
            "code": code,
            "action": "transfer",
            "args": jsonargs
        }
        return self.post("/v1/chain/abi_json_to_bin", data=data_dict)

    def abi_bin_to_json(self, code, binargs):
        data_dict = {
            "code": code,
            "action": "transfer",
            "binargs": binargs
        }
        return self.post("/v1/chain/abi_bin_to_json", data=data_dict)


    def push_transactions(self, data_dict):
        return self.post("/v1/chain/push_transaction", data=data_dict)


    def get_required_keys(self, data_dict):
        # 获取必需的密钥，从密钥列表中签署交易。

        return self.post("/v1/chain/get_required_keys", data=data_dict)



a = chain("https://api.testnet.eos.io")

pprint(a.get_code("cydfginyhfsa"))

# data_dict = [{"ref_block_num":"101","ref_block_prefix":"4159312339","expiration":"2017-09-25T06:28:49","scope":["initb","initc"],"actions":[{"code":"currency","type":"transfer","recipients":["initb","initc"],"authorization":[{"account":"initb","permission":"active"}],"data":"000000000041934b000000008041934be803000000000000"}],"signatures":[],"authorizations":[]}, {"ref_block_num":"101","ref_block_prefix":"4159312339","expiration":"2017-09-25T06:28:49","scope":["inita","initc"],"actions":[{"code":"currency","type":"transfer","recipients":["inita","initc"],"authorization":[{"account":"inita","permission":"active"}],"data":"000000008040934b000000008041934be803000000000000"}],"signatures":[],"authorizations":[]}]
# pprint(a.push_transactions(data_dict))