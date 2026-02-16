"""
Design a Feature Flag system that:

Supports multiple rollout strategies

User-based

Percentage-based

Can evaluate flags at runtime

Is easy to extend with new strategies



Feature F  will have roll out strategy-----who gets access to feature
user based [ user 1, user 2, user 3 ]   --enabled the flag for the user
 % based 20% ----- 20% of the users should have this enabled


"""
import hashlib
import math
import datetime
from abc import ABC, abstractmethod


class RolloutStrategy(ABC):
    @abstractmethod
    def is_enabled(self, user):
        pass


class UserBasedRolloutStrategy(RolloutStrategy):
    def __init__(self, users):
        self.allowed_users = set(users)

    def is_enabled(self, user):
        return user in self.allowed_users


class PercentageBasedRolloutStrategy(RolloutStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def is_enabled(self, user: str):
        hash_value = int(hashlib.md5(user.encode()).hexdigest(), 16)
        return (hash_value % 100) < self.percentage


"""
Day 1 → 10%
Day 2 → 20%
Day 3 → 30%
...
"""


class GradualRolloutStrategy(RolloutStrategy):

    def __init__(self, initial_percentage, increment_per_day):
        self.rollout_day = datetime.datetime.today().day
        self.initial_percentage = initial_percentage
        self.increment_per_day = increment_per_day
        self.max_percentage = 100

    def is_enabled(self, user):
        ith_day = datetime.datetime.today().day - self.rollout_day + 1
        hash_value = int(hashlib.md5(user.encode()).hexdigest(), 16)
        current_rolledout_percentage = min(self.max_percentage,
                                           self.initial_percentage + ith_day * self.increment_per_day)
        return (hash_value % 100) < (current_rolledout_percentage * ith_day)


class FeatureFlagSystem:
    def __init__(self, feature, strategy: RolloutStrategy):
        self.strategy = strategy
        self.feature = feature

    def is_enabled(self, user):
        return self.strategy.is_enabled(user)

    def change_strategy(self, strategy):
        self.strategy = strategy


if __name__ == '__main__':
    f = FeatureFlagSystem(
        "new_checkout",
        PercentageBasedRolloutStrategy(30)
    )

    print(f.is_enabled('userB'))

    f.change_strategy(UserBasedRolloutStrategy(['userA']))
    print(f.is_enabled('userA'))

    f.change_strategy(GradualRolloutStrategy(30, 10))
    print(f.is_enabled('userC'))
