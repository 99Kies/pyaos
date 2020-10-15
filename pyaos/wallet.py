import requests
from base import Base
from pprint import pprint

class wallet(Base):
    def __init__(self, url):
        super(wallet, self).__init__(url)

    def wallet_create(self):
        return self.post("/v1/wallet/create", data={"default": ""})


a = wallet("https://api.testnet.eos.io")
pprint(a.wallet_create())