from .event import *
from .priority_queue import EventQueue
from inventory.inventory import Inventory
from distributions import poisson_distribution, uniform_distribution

class InventorySimulation:
    def __init__(self):
        self.time = 0
        self.queue = EventQueue()
        self.order_time = 3

        initial_items = 10 # initial inventory
        max_inventory = 20 # maximum inventory
        reorder_point = 10 # reorder point
        order_cost = lambda x: 2 * x + 5 # cost of ordering x items
        hold_cost = 1 # cost of holding an item
        self.inventory = Inventory(initial_items, max_inventory, reorder_point, order_cost, hold_cost)

        self.demand_distribution = uniform_distribution.DiscretUniformDistribution(1, 5)
        self.lead_time_distribution = poisson_distribution.PoissonDistribution(5)

        self.payment_list = []

    def demand(self, demand_quantity):
        is_order_outstanding = self.inventory.is_order_outstanding()
        self.inventory.demand(demand_quantity)
        if not is_order_outstanding and self.inventory.is_order_outstanding():
            self.place_order(self.inventory.reorder_quantity())

    def next_arrival(self):
        demand = self.demand_distribution.generate_sample()
        lead_time = self.lead_time_distribution.generate_sample()
        self.queue.push(Event(self.time + lead_time, EventType.ARRIVAL, lambda: self.demand(demand)))

    def daily_payment(self):
        self.queue.push(Event(self.time + 1, EventType.PAYMENT, lambda: self.payment_list.append(self.inventory.holding_loss())))

    def place_order(self, order_quantity):
        self.queue.push(Event(self.time + self.order_time, EventType.DELIVERY, lambda: self.inventory.receive_order(order_quantity)))

    def simulate(self):
        self.next_arrival()
        self.daily_payment()
        while self.time < 100:
            event = self.queue.pop()
            self.time = event.time
            event.action()
            if event.type == EventType.ARRIVAL:
                self.next_arrival()
            elif event.type == EventType.PAYMENT:
                self.daily_payment()
        return self.payment_list