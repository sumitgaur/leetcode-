# "Design Splitwise - Expense sharing application.
# Let’s say there are 4 people. You and 3 of your friends (user1(you), user2, user3, user4). You pay 1000 Rs. for a meal. You have to split the money equally between all 4. Design an app that shows how much money everyone else owes to you.
#
# Phase 2 -
# Let’s say there’s another party and this time User 2 decided to pay 1000 Rs. Calculate the total sum everyone owes User1 and User2.
#
# Requirements -
# - anyone should be able to split the money equally or the exact amount. e.g.
# Rs. 1000 could be split into 25x4 or 200+300+250+250
#
#
# Input
# You can create a few users in your main method. No need to take it as input.
# There will be 3 types of input:
# - Expense in the format: EXPENSE
# - Show balances for all: SHOW
# - Show balances for a single user: SHOW
#
# Output
# When asked to show balance for a single user. Show all the balances that the user is part of:
# - Format: owes :
# Format: <user-id-of-x> owes <user-id-of-y>: <amount>
# - If there are no balances for the input, print No balances
from collections import defaultdict


class User:
    """
    represent a user
    """

    def __init__(self, id, name):
        self.u_id = id
        self.name = name

    pass


class Balance:
    """
    receiver will have +ve
    owes will have -ve
    """

    def __init__(self, amt):
        self.amount = amt

    pass


class Expense:
    """
    map user<->balance
    """

    def __init__(self, id):
        self.eid = id
        self.user_bal_map = {}
        # self.title
        # self.ts


class Transaction:
    def __init__(self, id, am, type):
        self.user_id = id
        self.amount = am
        self.type = type  # LENT/OWE


# class SplitTypeEnum:


# EXACT
# CUSTOM

class SplitwiseSystem:
    def __init__(self):
        self.transactions_for_users = defaultdict(list)

    def add_expense(self, paying_user, amount, users, split_type, split_amount=None):
        """

        paying_user = 1000
        {
        "user1":250
        user
        }
        :return:
        """
        if split_type == "EQUAL":

            amount_owed = amount / len(users)
            for user in users:
                if user == paying_user:
                    continue
                self.transactions_for_users[paying_user].append(Transaction(user, amount_owed, "LENT"))
                self.transactions_for_users[user].append(Transaction(user, amount_owed, "OWE"))

        if split_type == "EXACT":

            for user, amount_owed in zip(users, split_amount):
                if user == paying_user:
                    continue
                self.transactions_for_users[paying_user].append(Transaction(user, amount_owed, "LENT"))
                self.transactions_for_users[user].append(Transaction(user, amount_owed, "OWE"))

    def cal_transactions(self, user_id):
        if user_id not in self.transactions_for_users:
            print("No balance for user ", user_id)
            return []

        mtransaction = defaultdict(int)
        for transaction in self.transactions_for_users[user_id]:
            if transaction.type == "OWE":
                mtransaction[transaction.user_id] += transaction.amount
            if transaction.type == "LENT":
                mtransaction[transaction.user_id] -= transaction.amount

        user_in_debt = defaultdict(list)
        for other_user, amount in mtransaction.items():
            if amount < 0:
                user_in_debt[other_user].append((user_id, amount))
            if amount > 0:
                user_in_debt[user_id].append((other_user, amount))

        return user_in_debt

    def show(self, user_id=None):
        user_in_debt = defaultdict(list)
        if user_id:
            print("showing the transactions for user")
            user_in_debt = self.cal_transactions(user_id)
        else:
            # all
            for user_id in self.transactions_for_users.keys():
                for user_in_debt, owed_users in self.cal_transactions(user_id).items():
                    user_in_debt[user_in_debt] = list(set(user_in_debt[user_in_debt] + owed_users))

        if not user_in_debt:
            print("No balance")
        for user_in_debt, users_owed in user_in_debt.items():
            for users_owed, amt_owned in users_owed:
                print(f'{user_in_debt} owes {users_owed} : {abs(amt_owned)}')

    def edit_expense(self, eid):
        pass


if __name__ == '__main__':
    system = SplitwiseSystem()
    # system.show()
    # system.show('u1')
    system.add_expense('u1', 1000, ['u1', 'u2', 'u3', 'u4'], "EQUAL")
    system.add_expense('u2', 1000, ['u1', 'u2', 'u3', 'u4'], "EQUAL")
    system.show('u4')
    system.show('u3')
    system.show('u2')
    system.show('u1')

# u1->
