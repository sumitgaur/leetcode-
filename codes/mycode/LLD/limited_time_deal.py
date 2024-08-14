# Problem Statement
# You happen to be a budding entrepreneur and you have come up with an idea to build an e-commerce giant like Amazon, Flipkart, Walmart, etc. As part of this ambition, you want to build a platform to duplicate the concept of Limited Time Deals.

# Limited Time Deals
# A limited-time deal implies that a seller will put up an item on sale for a limited time period, say, 2 hours, and will keep a maximum limit on the number of items that would be sold as part of that deal.
# Users cannot buy the deal if the deal time is over
# Users cannot buy if the maximum allowed deal has already been bought by other users.
# One user cannot buy more than one item as part of the deal.

# The task is to create APIs to enable the following operations
# Create a deal with the price and number of items to be sold as part of the deal. itemId
# End a deal   itemId
# Update a deal to increase the number of items or end time
# Claim a deal
# Guidelines
# Document and communicate your assumptions in README.
# Create a working solution with production-quality code.
# Define and Create APIs to support the operations mentioned above
# Write a few unit tests for the most important code
# What are we looking for?
# Your approach to the solution
# How you write code in terms of readability and maintainability
# Usage of best practices
# Testing skills

# Out of scope: Handling at large scale

# OOPs Entities  real world entities -
# Product - {productId, name etc. }
# Deal - {productId, endTime (creation+Duration), number of units}
# Vendor extends User
# inmemory dbs - deals, hashmaps can be used for storage MVP
from collections import defaultdict
import time
import threading


class Product:
    def __init__(self, id):
        self.id = id


class User:
    def __init__(self, id):
        self.id = id


class Deal:
    deal_id = 0

    def __init__(self, p_id, units, duration):  # duration to be passed in seconds
        self.id = Deal.deal_id
        self.pid = p_id
        self.units = units
        self.end_time = int(time.time() + duration)  # epoch
        Deal.deal_id += 1


class Storage:
    pass


class InMemoryStorage(Storage):
    # aquiring the lock at lower level at product level at storage layer.  optimistic locking vs pessimistic locking.
    deal_data = defaultdict(Deal)
    user_to_deal = defaultdict(list)

    def insert(self, deal):
        InMemoryStorage.deal_data[deal.pid] = deal

    def update(self, deal):
        InMemoryStorage.deal_data[deal.pid] = deal

    def find_deal(self, pid):
        return InMemoryStorage.deal_data.get(pid, None)

    def remove_deal(self, deal):
        del InMemoryStorage.deal_data[deal.pid]

    def get_deals_by_user(self, uid):
        return InMemoryStorage.user_to_deal[uid]

    def claim(self, deal, user_id):
        deal.units -= 1
        InMemoryStorage.user_to_deal[user_id].append(deal)


class DealManager:
    def __init__(self):
        self.storage = InMemoryStorage()

    def create_deal(self, pid, units, duration):
        print("Creating deal for product", pid)
        deal = Deal(pid, units, duration)
        self.storage.insert(deal)
        print("Created deal for product %s with %d units for %d seconds " % (pid, units, duration))

    def update_deal(self, pid, units, duration):
        deal = self.storage.find_deal(pid)
        deal.units += units
        deal.end_time += duration
        self.storage.update(deal)

    def end_deal(self, pid):
        print("Ending the deal for %s" % (pid))
        deal = self.storage.find_deal(pid)
        self.storage.remove_deal(deal)

    def claim_deal(self, pid, user_id):
        # not thread safe make this synchronised,
        # Make only one thread can enter this method by using locks
        # above will make the control flow very slow
        deal_to_be_claimed = self.storage.find_deal(pid)
        user_deals = self.storage.get_deals_by_user(user_id)
        if deal_to_be_claimed is None:
            print("No deal running for the product ", pid)
            return
        if int(time.time()) > deal_to_be_claimed.end_time:
            print("Deal already ended, cannot claim")
            return
        if any(True for d in user_deals if deal_to_be_claimed.id == d.id):
            print("Deal has already been claimed by the user", user_id)
            return
        if deal_to_be_claimed.units == 0:
            print("All the items are sold out under the deal")
            return

        self.storage.claim(deal_to_be_claimed, user_id)
        print("Deal is claimed by user:", user_id)


if __name__ == '__main__':
    deal_manager = DealManager()
    deal_manager.create_deal("iphone11", 2, 5 * 60)
    deal_manager.create_deal("samsung", 2, 10 * 60)
    deal_manager.create_deal("pen", 2, 15 * 60)
    deal_manager.create_deal("laptop", 2, 15 * 60)

    # Test1 deal claimed by multiple user Success
    # deal_manager.claim_deal("pen","sumit")
    # deal_manager.claim_deal("pen","amit")
    # deal_manager.claim_deal("pen","kumar")

    # Test2. Deal timed out  Failure
    # deal_manager.claim_deal("pen","sumit")
    # time.sleep(1)
    # deal_manager.claim_deal("pen","kumar")

    # Test3 Deal ended  Failure
    # deal_manager.claim_deal("pen","sumit")
    # deal_manager.end_deal("pen")
    # deal_manager.claim_deal("pen","sumit")

    # Test4 Deal claimed by same person Failure
    # deal_manager.claim_deal("pen","sumit")
    # deal_manager.claim_deal("pen","sumit")

    # Test5 same user trying to claim deal on other product
    # deal_manager.claim_deal("pen","sumit")
    # deal_manager.claim_deal("iphone11","sumit")

# locking

# ship to production system

# REST  http methods
# POST / api / v1 / create - deal  # idempotent
# {
#     "product-id": < product_id >,
# "units": < units >,
# "duration": < duration >
# }
#
# PUT / api / v1 / claim
# {
#     "pid",
#     "user_id"
# }
#
