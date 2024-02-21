from .inventory_state import InventoryState

class Inventory:
    def __init__(self, initial_items, max_inventory, reorder_point, order_cost, hold_cost):
        self.state = InventoryState(initial_items)
        self.max_inventory = max_inventory
        self.reorder_point = reorder_point
        self.order_cost = order_cost
        self.hold_cost = hold_cost
        # self.losses_by_ordering = 0
        # self.losses_by_holding = 0

    def receive_order(self, order):
        self.state.receive_order(order)
        # self.losses_by_ordering += self.order_cost(order)

    def place_order(self):
        self.state.place_order()

    def reorder_quantity(self):
        return self.max_inventory - self.state.items

    def under_stock(self):
        return self.state.items < self.reorder_point

    def demand(self, demand_quantity):
        self.state.demand(demand_quantity)
        if self.under_stock() and not self.state.is_order_outstanding():
            self.place_order()
            # self.max_inventory - self.state.items
        
    def holding_loss(self):
        return self.hold_cost * self.state.items

    def is_order_outstanding(self):
        return self.state.is_order_outstanding()
    
    