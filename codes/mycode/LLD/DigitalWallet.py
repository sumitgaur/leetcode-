import uuid
from abc import ABC, abstractmethod
from collections import defaultdict


class Wallet:
    def __init__(self, inital_amt):
        self.account_no = str(uuid.uuid4())
        self.amount = inital_amt


class User:
    def __init__(self, name, money):
        self.id = str(uuid.uuid4())
        self.name = name
        self.wallet = Wallet(money)


class Amount:
    CURRENCY = "F₹"

    def __init__(self, amt):
        self.currency = Amount.CURRENCY
        self.amount = amt

    def __str__(self):
        return "{}{}".format(self.currency, self.amount)


class Transaction:
    def __init__(self, from_acc: int, to_account: int, amount: Amount):
        self.from_ = from_acc
        self.to_ = to_account
        self.amount = amount

    def __str__(self):
        return "Transaction of amount {} from {} to {}".format(self.amount, self.from_, self.to_)


class DBManager(ABC):
    @abstractmethod
    def insert_user(self, name, money):
        pass

    @abstractmethod
    def update_wallet_money(self, wallet: Wallet, money: Amount):
        pass

    @abstractmethod
    def insert_transaction(self, transaction: Transaction):
        pass


class InMemoryDBManager(DBManager):
    def __init__(self):
        self.users = []
        self.transactions_credit = defaultdict(list)
        self.transactions_debit = defaultdict(list)

    def insert_user(self, name, money):
        user = User(name, money)
        self.users.append(user)
        return user.wallet.account_no

    def update_wallet_money(self, acc_number, money: Amount):
        wallet = self._fetch_wallet_by_account_number(acc_number)
        wallet.amount += money

    def insert_transaction(self, transaction: Transaction):
        self.transactions_credit[transaction.to_].append(transaction)
        self.transactions_debit[transaction.from_].append(transaction)

    def _fetch_wallet_by_account_number(self, account_id):
        for u in self.users:
            if u.wallet.account_no == account_id:
                return u.wallet
        return None

    def current_balance(self, account_id):
        return self._fetch_wallet_by_account_number(account_id).amount

    def fetch_transactions(self, account_id, last_days=None):
        if last_days is None:
            last_days = 30
        return [self.transactions_credit[account_id][-last_days:], self.transactions_debit[account_id][-last_days:]]


class AccountService(ABC):

    @abstractmethod
    def transfer_money(self, from_account, to_account, amount):
        pass

    @abstractmethod
    def overview(self, account_id):
        pass


class WalletAccountService(AccountService):

    def __init__(self):
        self.db_manager = InMemoryDBManager()

    def transfer_money(self, from_account, to_account, amount):
        # @todo: acquire the lock on the account Ids
        self.db_manager.update_wallet_money(from_account, -amount)
        self.db_manager.update_wallet_money(to_account, amount)
        self.db_manager.insert_transaction(Transaction(from_account, to_account, amount))

    def overview(self, account_id, last_days=None):
        bal = self.db_manager.current_balance(account_id)
        credits, debits = self.db_manager.fetch_transactions(account_id, last_days)
        print("Current Balance of account ID - {}".format(bal))
        for c in credits:
            print(c)
        for d in debits:
            print(d)

    def create_wallet(self, username, money):
        return self.db_manager.insert_user(username, money)


class Driver:
    def __init__(self):
        self.wallet_account_service = WalletAccountService()

    def run(self):
        print("\nOPTIONS:")
        print("1. Create wallet")
        print("2. Transfer Amount")
        print("3. Account Statement")
        print("4. Overview")
        print("5. Exit")
        while True:
            case = int(input())
            if case == 1:
                name = input("Enter Name")
                money = int(input("Enter Initial Money"))
                account_no = self.wallet_account_service.create_wallet(name, money)
                print("Wallet created for the user {} with inital money {}, Account number {}".format(name, money,
                                                                                                      account_no))

            elif case == 2:
                from_ = input("Enter account number of the transferrer")
                to_ = input("Enter account number of the transferee")
                amt = int(input("Amount to transfer"))
                self.wallet_account_service.transfer_money(from_, to_, amt)
                print("Transferred money from {} to {}".format(from_, to_))
            elif case == 3:
                acc_no = input("Enter account number of the account to check overview")
                self.wallet_account_service.overview(acc_no)
            elif case == 5:
                break


if __name__ == '__main__':
    Driver().run()
