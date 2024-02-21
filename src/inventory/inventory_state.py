class InventoryState:
    def __init__(self, items, waiting_order=False):
        self.items = items
        self.waiting_order = waiting_order

    def receive_order(self, order):
        self.items += order
        self.waiting_order = False

    def place_order(self):
        self.waiting_order = True
    
    def demand(self, demand_quantity):
        self.items = max(0, self.items - demand_quantity)

    def is_order_outstanding(self):
        return self.waiting_order
    
    def copy(self):
        return InventoryState(self.items, self.waiting_order)