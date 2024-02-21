from enum import Enum

class EventType(Enum):
    PAYMENT = 1
    DELIVERY = 2
    ARRIVAL = 3

class Event:
    def __init__(self, time, type: EventType, action):
        self.time = time
        self.type = type
        self.action = action

    def __lt__(self, other):
        if self.time == other.time:
            return self.type.value < other.type.value
        return self.time < other.time
    
    def __le__(self, other):
        if self.time == other.time:
            return self.type.value <= other.type.value
        return self.time <= other.time
    
    def __gt__(self, other):
        if self.time == other.time:
            return self.type.value > other.type.value
        return self.time > other.time
    
    def __ge__(self, other):
        if self.time == other.time:
            return self.type.value >= other.type.value
        return self.time >= other.time
    
    def __eq__(self, other):
        return self.time == other.time and self.type.value == other.type.value

    def __ne__(self, other):
        return self.time != other.time or self.type.value != other.type.value
