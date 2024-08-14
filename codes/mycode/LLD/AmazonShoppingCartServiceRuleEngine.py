import heapq
from abc import abstractmethod, ABC


class User:
    def __init__(self, id: int, fname: str, lname: str, is_prime: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.is_prime_ = is_prime

    def is_prime(self):
        return self.is_prime_


class Item:
    def __init__(self, name, is_grocery, discounted_price):
        self.is_subscribed = None
        self.id = id
        self.name = name
        self.is_grocery = is_grocery
        self.discounted_price = discounted_price

    def set_discounted_price(self, price):
        self.discounted_price = price

    def subscribe(self):
        self.is_subscribed = True


class ShoppingCart:
    DEFAULT_SHIPPING_TIME = 7 * 24

    def __init__(self, user):
        self.items = []
        self.user = user
        self.shipping_offered_in_hours = ShoppingCart.DEFAULT_SHIPPING_TIME

    def set_user(self, user):
        self.user = user

    def add_item(self, item):
        self.items.append(item)

    def is_grocery_only(self):
        return all(map(lambda item: item.is_grocery, self.items))

    def get_total_price(self):
        return sum(map(lambda item: item.discounted_price, self.items))

    def get_user(self) -> User:
        return self.user

    def set_shipping_offered(self, hour):
        self.shipping_offered_in_hours = hour


class Rule(ABC):
    def __init__(self, p):
        self.priority = p

    @abstractmethod
    def evaluate(self, cart: ShoppingCart):
        pass

    @abstractmethod
    def fire_rule(self, cart: ShoppingCart):
        pass

    def __lt__(self, o):
        return self.priority - o.priority


class Rule1(Rule):
    """
    Prime user
    all grocery
    price>$100
    """

    def __init__(self, priority):
        super().__init__(priority)

    def evaluate(self, cart: ShoppingCart):
        if cart.get_user().is_prime() and cart.get_total_price() > 100 and cart.is_grocery_only():
            return True

    def fire_rule(self, cart: ShoppingCart):
        cart.set_shipping_offered(1)


class ExecuteOnlyFirstMatch(Rule):  # implement rule engine

    def __init__(self, p):
        super().__init__(p)
        self.rules_pq = []  # heap
        self.rule_to_execute = None

    def evaluate(self, cart: ShoppingCart):
        rules_copy = self.rules_pq[:]
        while rules_copy:
            rule = heapq.heappop(rules_copy)
            if rule.evaluate(cart):
                self.rule_to_execute = rule
                return True
        return False

    def fire_rule(self, cart: ShoppingCart):
        self.rule_to_execute.fire_rule(cart)

    def register(self, rule: Rule):
        heapq.heappush(self.rules_pq, rule)


class RuleEngine(ABC):
    @abstractmethod
    def register(self, rule: Rule):
        pass

    @abstractmethod
    def execute(self, cart: ShoppingCart):
        pass


class ShoppingCartRuleEngine(RuleEngine):
    def __init__(self):
        self.rules = []

    def register(self, rule: Rule):
        heapq.heappush(self.rules, rule)

    def execute(self, cart: ShoppingCart):
        rules_copy = self.rules[:]
        while rules_copy:
            rule = heapq.heappop(rules_copy)
            if rule.evaluate(cart):
                rule.fire_rule(cart)
