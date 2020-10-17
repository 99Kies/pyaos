import requests
from base import Base
from pprint import pprint

class wallet(Base):
    def __init__(self, url):
        super(wallet, self).__init__(url)

    def wallet_create(self, wallet_name):
        """
        Create a new wallet with the given name.

        :param wallet_name: (str) name of the wallet to be created
        :return: response object
        """
        path = '/v1/wallet/create'
        return self.post(path, data=wallet_name)

    def wallet_open(self, wallet_name):
        """
        Open an existing wallet of the given name.

        :param wallet_name: (str) name of the wallet to be opened
        :return: response object
        """
        path = '/v1/wallet/open'
        return self.post(path, data=wallet_name)

    def wallet_lock(self, wallet_name):
        """
        Lock a wallet of the given name

        :param wallet_name: (str) name of the wallet to be opened
        :return: response object
        """
        path = '/v1/wallet/lock'
        return self.post(path, data=wallet_name)

    def wallet_lock_all(self):
        """
        Lock all wallets.

        :return: response object
        """
        path = '/v1/wallet/lock_all'
        return self.get(path=path)

    def wallet_unlock(self, wallet_name_password):
        """
        Unlock a wallet with the given name and password

        :param wallet_name_passord: (str) list with name and password
        of the given wallet
        :return: response object
        """
        path = '/v1/wallet/unlock'
        return self.post(path, data=wallet_name_password)

    def wallet_import_key(self, wallet_name_privKey):
        """
        Import a private key to the wallet of the given name

        :param wallet_name_privKey: (str) list that contains the wallet
        name and private key
        :return: response object
        """
        path = '/v1/wallet/import_key'
        return self.post(path, data=wallet_name_privKey)

    def wallet_list(self):
        """
        List all wallets

        :return: response object
        """
        path = '/v1/wallet/list_wallets'
        return self.get(path)

    def wallet_list_keys(self):
        """
        List all key pairs across all wallets

        :return: response object
        """
        path = '/v1/wallet/list_keys'
        return self.get(path)

    def wallet_get_public_keys(self):
        """
        List all public keys across all wallets

        :return: response object
        """
        path = '/v1/wallet/get_public_keys'
        return self.get(path)

    def wallet_set_timeout(self, timeout):
        """
        Set wallet auto lock timeout (in seconds)

        :param timeout: (str) timeout in seconds
        :return: response object
        """
        path = '/v1/wallet/set_timeout'
        return self.post(path, data=timeout)

    def wallet_sign_trx(self, transaction_data):
        """
        Sign transaction given an array of transaction, require
        public keys, and chain id

        :param transaction_data: (str) list of transaction json and  public key
        :return: response key
        """
        path = '/v1/wallet/sign_transaction'
        return self.post(path, data=transaction_data)
